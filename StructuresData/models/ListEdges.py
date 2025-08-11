from dataclasses import dataclass
from typing import Union, List
from uuid import UUID

from Edge import Edge

@dataclass
class ListEdges:
    def __init__(self, id: Union[UUID, int]):
        self.id = id
        self.list_edges: List[Edge] = []