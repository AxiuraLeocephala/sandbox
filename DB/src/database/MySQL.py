import os 
import logging
from signal import signal, SIGINT, SIGTERM
import sys
import time
from typing import Callable, Dict, List, Union, Tuple

import mysql.connector
from dotenv import load_dotenv

from src.interface.InterfaceDB import InterfaceDB

class MySQL(InterfaceDB):
    __cnx_pool: mysql.connector.pooling.MySQLConnectionPool = None
    __delay_attempts_get_connection: float = 3
    __number_attempts_get_connection: int = 2
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    def __init__(self) -> None:
        if load_dotenv("src/config/config_db.env"):
            self.__delay_attempts_get_connection = float(os.getenv("DELAY_ATTEMPTS_GET_CONNECTION"))
            self.__number_attempts_get_connection = int(os.getenv("NUMBER_ATTEMPTS_GET_CONNECTION"))
            self.__register_handler_shutdown() 
        else:
            sys.exit("Error loading variables enviroment: there are no variables or unvalid path to enviroment")

    def __del__(self, *args, **kwargs):
        self.__instance = None

    def __register_handler_shutdown(self):
        signal(SIGINT, self.__handle_shutdown)
        signal(SIGTERM, self.__handle_shutdown)

    def __handle_shutdown(self) -> None:
        # here awaiting all active transaction
        self.__close_pool_connection()

    def create_pool_connection(self) -> None:
        self.__cnx_pool = mysql.connector.pooling.MySQLConnectionPool(pool_size=int(os.getenv("POOL_ZIZE")),
                                                                      pool_name=os.getenv("POOL_NAME"),
                                                                      pool_reset_session=True,
                                                                      host = os.getenv("HOST"),
                                                                      port=os.getenv("PORT"),
                                                                      user=os.getenv("USER"),
                                                                      password=os.getenv("PASSWORD"),
                                                                      database=os.getenv("DATABASE"))

    def close_pool_connection(self) -> None: 
        self.__cnx_pool = None

    def __get_connection(self) -> Tuple[mysql.connector.pooling.PooledMySQLConnection, Callable]:
        for i in range(self.__number_attempts_get_connection):
            try:
                cnx = self.__cnx_pool.get_connection()
                cursor = cnx.cursor()

                return cnx, cursor
            except mysql.connector.errors.PoolError as error:
                logging.info(error.msg)
                print(f"A new attemp will be made in {self.__number_attempts_get_connection} second")

                time.sleep(self.__delay_attempts_get_connection)
        
        raise Exception("The number of repetitions of receiving a connection has been exceeded")

    def __execute_query(self, query: str, params: Union[List, Dict, Tuple]) -> List[Tuple]:
        cnx, cursor = self.__get_connection()
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Exception as error:
            logging.error(f"Error executing query to database: {error}")
            raise error
        finally:
            cursor.close()
            cnx.close()
        
    def __execute_non_query(self, query: str, params: Union[List, Dict, Tuple]) -> None:
        cnx, cursor = self.__get_connection()
        try:
            cursor.execute(query, params)
            cnx.commit()
        except Exception as error:
            logging.error(f"Error executind non-query to database: {error}")
            raise error
        finally:
            cursor.close()
            cnx.close()

    @classmethod
    def get(self, query: str, params: Union[List, Dict, Tuple]) -> List[Tuple]:
        self.__execute_query(query, params)

    @classmethod
    def insert(self, query: str, params: Union[List, Dict, Tuple]) -> None:
        self.__execute_non_query(query, params)

    @classmethod
    def update(self, query: str, params: Union[List, Dict, Tuple]) -> None:
        self.__execute_non_query(query, params)

    @classmethod
    def delete(self, query: str, params: Union[List, Dict, Tuple]) -> None:
        self.__execute_non_query(query, params)
    