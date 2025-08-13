from dataclasses import dataclass

from models.Vertex import Vertex

@dataclass
class Edge:
    outgoing_vertex: "Vertex"
    incoming_vertex: "Vertex"