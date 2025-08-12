from dataclasses import dataclass
from typing import Any

@dataclass
class Vertex:
    data: Any
    prev: "Vertex" = None
    next: "Vertex" = None