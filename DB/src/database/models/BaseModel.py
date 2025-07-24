from typing import List, Tuple

from src.database.MySQL import MySQL

class BaseModel:
    @classmethod
    def all(cls) -> List[Tuple]:
        return MySQL.get("SELECT * FROM %s", cls.TABLE_NAME)

    def save(self) -> None: 
        fields = ", ".join(self.__dict__.keys())
        values = ", ".join(["%s"] * len(self.__dict__))
        query = f"INSERT INTO {self.TABLE_NAME} ({fields}) VALUES ({values})"
        MySQL.insert(query, tuple(self.__dict__.values()))

    def change(self, **kwargs) -> None:
        string_assignment = " = %s, ".join(kwargs.keys()) + " = %s"
        query = f"UPDATE {self.TABLE_NAME} SET {string_assignment} WHERE {self.NAME_ID_RECORD} = {self.id}"
        MySQL.update(query, string_assignment)


    def delete(self) -> None: 
        query = f"DELETE FROM {self.TABLE_NAME} WHERE {self.NAME_ID_RECORD} = {self.id}"
        MySQL.delete(query)