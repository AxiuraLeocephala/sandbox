from abc import ABC, abstractmethod
from typing import Dict, List, Union, Tuple

class InterfaceDB(ABC):
    @abstractmethod
    def get(self, query: str, params: Union[List, Dict, Tuple]): pass

    @abstractmethod
    def insert(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def delete(self): pass