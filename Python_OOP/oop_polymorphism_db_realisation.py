import logging
from typing import Union, Tuple, Dict, Any
import atexit
import signal

import mysql.connector

from oop_polymorphism_db_interface import db_interface

class db_mysql(db_interface):
    data_for_connection = {
        "host": "127.0.0.1",
        "port": 3305,
        "user": "root",
        "password": "root",
        "database": "webappmenu-meridian"
    }

    def __init__(self):
        self.__register_handle_shutdown()

    def __register_handle_shutdown(self):
        atexit.register(self.__handle_shutdown)
        signal.signal(signal.SIGINT, self.__handle_shutdown)
        signal.signal(signal.SIGTERM, self.__handle_shutdown)

    def __handle_shutdown(self):
        self.close()

    def connect(self):
        try:
            self.__cnx = mysql.connector.connect(**self.data_for_connection)
        except Exception as e:
            logging.error("Error connection to the database. Message of error: ", e)
            raise e

    def close(self):
        self.__cnx.close()

    def __execute_query(self, query: str, params: dict=None) -> Union[Tuple, Dict, None]:
        cursor = self.__cnx.cursor()
        try:
            cursor.execute(query, params)
            return cursor.fetchone()
        except Exception as error:
            logging.error("Error executoin query. Message of error: ", error)
            raise error
        
    def __execute_non_query(self, query: str, params: dict=None) -> None:
        cursor = self.__cnx.cursor()
        try:
            cursor.execute(query, params)
            cursor.commit()
        except Exception as error:
            logging.error("Error execution non-query. Message of error: ", error)
            raise error
        