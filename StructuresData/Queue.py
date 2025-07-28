from typing import Any, Tuple, Type

from Array import DynamicArray

class Queue(DynamicArray):
    def __init__(self, type_elements: Tuple[Type]):
        super().__init__(type_elements=type_elements)

    def pop(self) -> Any:
        return super().pop(0)
    
    def insert(self, index, object) -> None:
        raise ValueError("it is not possible to insert a new element into the array, use the append method")
    
    def remove(self, value) -> None:
        raise ValueError("it is not possible to delete a specific item from the queue. use the pop method")
    
    def sort(self, *, key, reverse) -> None:
        raise ValueError("the queue cannot be sorted")

if __name__ == "__main__":
    queue = Queue(type_elements = int)
    print(queue)
