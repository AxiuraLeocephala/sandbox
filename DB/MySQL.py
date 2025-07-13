import os
import sys
from signal import signal, SIGINT, SIGTERM
import logging
from typing import Tuple, Any, Union, Dict, Literal

import mysql.connector
from mysql.connector.pooling import PooledMySQLConnection
from dotenv import load_dotenv

from interface_db import Interface_db
from Data.custom_exceptions import FallingAsleepError
from Data.data_system_parameters import SystemParameters

class MySQL(Interface_db):
    __allowed_transaction = True

    def __init__(self) -> None:
        self.__register_handle_shutdown() if load_dotenv(dotenv_path="../mysql.env") else sys.exit("Error loading environment variables: there are no variables")

    def __register_handle_shutdown(self) -> None:
        signal(SIGINT, self.__handle_shutdown)
        signal(SIGTERM, self.__handle_shutdown)
        
        logging.info("Shutdown handlers are registered")

    def __handle_shutdown(self) -> None:
        self.__allowed_transaction = False
        # Здесь ожидание завершения всех транзакций
        self.close_connection()

    def create_pool_connection(self) -> None:
        try:
            self.__cnx_pool = mysql.connector.pooling.MySQLConnectionPool(pool_size = int(os.getenv("DB_POOL_SIZE")),
                                                                        pool_name = os.getenv("DB_POOL_NAME"),
                                                                        pool_reset_session=True,
                                                                        host = os.getenv("DB_HOST"),
                                                                        port = os.getenv("DB_PORT"),
                                                                        user = os.getenv("DB_USER"),
                                                                        password = os.getenv("DB_PASSWORD"),
                                                                        database = os.getenv("DB_NAME"),)
        except Exception as error:
            logging.error(f"Error creation pool", error)
            raise error

    def close_connection(self) -> None:
        self.__cnx_pool = None

    def __get_connection(self) -> PooledMySQLConnection:
        try:
            cnx = self.__cnx_pool.get_connection()
            cursor = cnx.cursor()

            return cnx, cursor
        except Exception as error:
            logging.error("Error getting connection from pool: ", error)
            raise error

    def __execute_query(self, sql: str, params: dict=None) -> Union[Tuple, Dict, None]:
        if self.__allowed_transaction:
            cnx, cursor = self.__get_connection()
        else:
            raise FallingAsleepError("In preparation for shutdown")
        
        try:
            cursor.execute(operation=sql, params=params)
            return cursor.fetchone()
        except Exception as error:
            logging.error("Error execution query: ", error)
            raise error
        finally:
            cursor.close()
            cnx.close()

    def __execute_non_query(self, sql: str, params: dict=None) -> None:
        if self.__allowed_transaction:
            cnx, cursor = self.__get_connection()
        else:
            raise FallingAsleepError("In preparation for shutdown")
        
        try:
            cursor.execute(operation=sql, params=params)
            cnx.commit()
        except Exception as error:
            logging.error("Error execution NON query: ", error)
            raise error
        finally:
            cursor.close()
            cnx.close()

    def get_system_parameters(self, 
                              fields: list[str] = ["*"], 
                              operands_of_condition: dict[Union[str, int], Tuple[Any, str]] = None
                              ):
        '''
        Args:
            fields: Cписок, элементы которого - поля для выборки
            operands_of_condition: Cловарь, набор пар ключ/значение. Ключ - первый операнд сравнения, должен иметь тип либо string, либо int.
                                   Значение - второй операнд сравнени, должен иметь либо любой тип, если сравнение одинарное, либо кортеж,
                                   если сравнение множественное, второй элемент которого - логический оператор.
        '''

        string_fields = ", ".join(fields)
        
        string_condition = ""
        if operands_of_condition:
            string_condition = " WHERE"
            for k, v in operands_of_condition.items():
                string_condition += " " + str(k) + " = " + (str(v[0]) if isinstance(v, tuple) else str(v)) + (str(v[1]).upper() if isinstance(v, tuple) else "")
            
        string_query = "SELECT %s FROM system_parameters%s;" % (string_fields, string_condition)

        return self.__execute_query(string_query)

db = MySQL()
db.create_pool_connection()
system_parameters = db.get_system_parameters()
db.close_connection()