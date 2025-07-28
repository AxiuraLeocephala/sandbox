from typing import Any, Tuple, Type

from Queue import Queue

class Stack(Queue):
    def __init__(self, type_elements: Tuple[Type]):
        super().__init__(type_elements=type_elements)

    def pop(self) -> Any:
        return super().pop(-1)