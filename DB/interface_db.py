from abc import ABC, abstractmethod

class Interface_db(ABC):
    @abstractmethod
    def create_pool_connection(): pass

    @abstractmethod
    def close_connection(): pass

