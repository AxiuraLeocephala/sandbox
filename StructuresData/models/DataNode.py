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

data_node1 = DataNode("213")
data_node2 = DataNode("213")
data_node3 = DataNode("213")
data_node4 = DataNode("213")

print(data_node1.id)
print(data_node2.id)
print(data_node3.id)
print(data_node4)