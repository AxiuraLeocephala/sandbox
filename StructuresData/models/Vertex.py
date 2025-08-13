from dataclasses import dataclass
from typing import Any, Union
from uuid import UUID

@dataclass
class Vertex:
    id: Union[UUID, int]
    data: Any
    prev: "Vertex" = None
    next: "Vertex" = None

    def __eq__(self, other):
        if not isinstance(other, Vertex):
            return NotImplemented
        return self.id == other.id 