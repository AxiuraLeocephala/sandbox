from typing import Any, Tuple, Type
import logging

from Array import DynamicArray
from ProhibitedMethodsDSQ import ProhibitedMethodsDSQ

class Queue(DynamicArray, ProhibitedMethodsDSQ):
    def __init__(self, type_elements: Tuple[Type]):
        super().__init__(type_elements=type_elements)

    def pop(self) -> Any:
        return super(DynamicArray, self).pop(0)

    def get(self) -> Any:
        return self[0]

if __name__ == "__main__":
    queue = Queue(type_elements = int)
