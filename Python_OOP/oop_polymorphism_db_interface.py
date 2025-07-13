from abc import ABC, abstractmethod

class db_interface(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def close(self): pass

    @abstractmethod
    def get_system_paramaters(self): pass