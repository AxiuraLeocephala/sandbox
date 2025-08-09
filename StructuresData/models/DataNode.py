from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class DataNode:
    id: int = 0

    def __init__(self, data: Any):
        self.id: int = DataNode.id
        self.data: Any = data
        DataNode.id += 1

    def __call__(self) -> Dict:
        return vars(self)

    def __str__(self) -> str:
        return str(self())