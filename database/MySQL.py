import logging
import mysql.connector  

class MySQL:
    def __init__(self):
        pass

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="127.0.0.1",
                port="3305",
                database="webappmenu",
                user="root",
                password="root"
            )
            
            logging.info("Create connection to database")
        except Exception as error:
            logging.info("Error when connecting to the database:", error)

    def query(self):
        