from typing import Any, List, Optional, Iterable, SupportsIndex, TypeVar, Type

_T = TypeVar("_T")

# Classic array: static length, only one type of elements
class Array(List):
    def __init__(self, *args: int, length: Optional[int]):
        if not all(isinstance(arg, int) for arg in args):
            raise ValueError("All array arguments must be of the same type")
        
        super().__init__(args)

        if length:
            if length < 0:
                raise ValueError("Length is less than zero was passed. Are you seriously?")
            if length < len(args):
                raise ValueError("The array length is less than the number of array elements passed")
            
            super().extend([None] * (length - len(args)))

    def __call__(self):
        return list(self)

    def append(self, object: _T, /) -> None:
        raise ValueError("Is not possible to append an element to the array")
    
    def extend(self, iterable: Iterable[_T], /) -> None:
        raise ValueError("Is not possible to extend original array")

    def pop(self, index: SupportsIndex = -1) -> _T:
        object = super().pop(index)
        super().insert(index, None)
        return object
    
    def insert(self, index: SupportsIndex, object: _T, /) -> None:
        raise ValueError("Is not possible to insert an element to the array")
    
class DynamicArray(List):
    def __init__(self, *args):
        if not all(isinstance(arg, type(args[0])) for arg in args):
            raise ValueError("all array elements must be of the same type")
        
        super().__init__(args)

if __name__ == "__main__":
    array = Array(0, 1, 2, 3, 4, length=6)
    print(array[0])