from typing import Any, Tuple, Type

from Array import DynamicArray
from ProhibitedMethodsDSQ import ProhibitedMethodsDSQ

class Stack(DynamicArray, ProhibitedMethodsDSQ):
    def __init__(self, type_elements: Tuple[Type]):
        super().__init__(type_elements=type_elements)

    def pop(self) -> Any:
        return super(DynamicArray, self).pop(-1)
    
    def get(self) -> Any:
        return self[-1]
    
if __name__ == "__main__":
    stack = Stack(int)

