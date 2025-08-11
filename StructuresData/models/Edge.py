from dataclasses import dataclass

from StructuresData.models.Vertex import Node

@dataclass
class Edge:
    def __init__(self, outgoing_node: Node, incoming_node: Node):
        self.outgoing_node = outgoing_node
        self.incoming_node = incoming_node