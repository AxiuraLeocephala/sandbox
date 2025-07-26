from typing import Any, List, Optional, Iterable, SupportsIndex, Union, TypeVar, Type
from math import floor
from random import random, randint

_T = TypeVar("_T")

# Classic array: static length, only one type of elements
class Array(list):
    __type_elements: Type

    def __init__(self, *args: Any, type_elements: Type, length: int = None):
        self.__type_elements = type_elements
        if not all(isinstance(arg, self.__type_elements) for arg in args):
            raise ValueError(f"All array arguments must be of the same type, {self.__type_elements}")
        
        super().__init__(args)
        
        if length:
            if length < 0:
                raise ValueError("Length is less than zero was passed. Are you seriously?")
            if length < len(args):
                raise ValueError("The array length is less than the number of array elements passed")
            
            super().extend([None] * (length - len(args)))

    def __call__(self):
        return self

    def append(self, object: _T, /) -> None:
        raise ValueError("Is not possible to append an element to the array")
    
    def extend(self, iterable: Iterable[_T], /) -> None:
        dicrement = len(self) - 1
        num_None = 0
        available_seats = False
        pointer = 0

        while dicrement > 0:
            if isinstance(self[dicrement], self.__type_elements):
                if num_None: available_seats = True
                break
            else:
                num_None += 1

            dicrement -= 1

        if not available_seats:
            raise ValueError("There are no free spaces in the source array")
        if num_None < len(iterable): 
            raise ValueError("The number of free spaces in the original array is less than the number of elements in the passed array")
        
        for i in range(dicrement + 1, len(self)):
            self[i] = iterable[pointer]
            pointer += 1

    def pop(self, index: SupportsIndex = -1) -> _T:
        object = super().pop(index)
        super().insert(index, None)
        return object
    
    def bubble_sort(self) -> None:
        for i in range(len(self) - 1):
            for j in range(i + 1, len(self)):
                if self[i] > self[j]:
                    elem = self[i]
                    self[i] = self[j]
                    self[j] = elem

    def inserting_sort(self) -> None:
        n = len(self)
        for i in range(1, n):
            key = self[i]
            j = i - 1
            while j >= 0 and key < self[j]:
                self[j + 1] = self[j]
                j -= 1
            self[j + 1] = key

    def selection_sort(self) -> None:
        n = len(self)

        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                if self[j] < self[min_idx]:
                    min_idx = j
            
            self[i], self[min_idx] = self[min_idx], self[i]

class DynamicArray(List):
    __type_elements: Type

    def __init__(self, *args, type_elements: Type):
        self.__type_elements = type_elements
        if not all(isinstance(arg, self.__type_elements) for arg in args):
            raise ValueError("all array elements must be of the same type")
        
        super().__init__(args)

def is_worked(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return "Not sorted"
    return "Sorted"

if __name__ == "__main__":
    array = Array(type_elements=int, length=10)
    # array: List = [None] * 10
    min_number = 56
    max_number = 6583

    for i in range(len(array)):
        array[i] = floor((random() * (max_number - min_number + 1)) + min_number)

    print(array)
    array.selection_sort()
    print(array)
    print(is_worked(array))