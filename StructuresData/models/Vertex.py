from dataclasses import dataclass

@dataclass
class Vertex:
    def __init__(self, data, *, next = None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next
