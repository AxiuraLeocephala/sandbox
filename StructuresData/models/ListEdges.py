from dataclasses import dataclass, field
from typing import List

from models.Edge import Edge

@dataclass
class ListEdges:
    # Для избежания установки общего значения для всех экземпляров 
    # используется функция field c параметром default_factory
    list_edges: List[Edge] = field(default_factory=list)