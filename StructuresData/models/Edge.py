from dataclasses import dataclass

from models.Vertex import Vertex

@dataclass
class Edge:
    def __init__(self, outgoing_vertex: Vertex, incoming_vertex: Vertex):
        self.outgoing_vertex = outgoing_vertex
        self.incoming_vertex = incoming_vertex