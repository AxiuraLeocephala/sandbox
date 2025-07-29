from typing import Any, Tuple, Type

from Queue import Queue
from Stack import Stack
from ProhibitedMethodsDSQ import ProhibitedMethodsDSQ

class Deka(Queue, Stack, ProhibitedMethodsDSQ):
    def __init__(self, type_elements = Tuple[Type]):
        super().__init__(type_elements=type_elements)

    def pop_first(self) -> Any:
        return Queue.pop(self)
    
    def get_first(self) -> Any:
        return self[0]
    
    def pop_last(self) -> Any:
        return Stack.pop(self)
    
    def get_last(self) -> Any:
        return self[-1]

if __name__ == "__main__":
    deka = Deka()
    deka.extend([1, 2, 3, 4, 5])
    print(deka)
    print(deka.pop_first())
    print(deka)
    print(deka.pop_last())
    print(deka)