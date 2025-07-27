from typing import Any, List, Iterable, SupportsIndex, Union, TypeVar, Type
from math import floor
from random import random

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
    
    def bubble_sort(self, reverse: bool = False) -> None:
        n = len(self)

        def from_less_to_more(i, j):
            if self[i] > self[j]:
                self[i], self[j] = self[j], self[i]

        def from_more_to_less():
            if self[i] < self[j]:
                self[i], self[j] = self[j], self[i]

        perform_comparison = from_more_to_less if reverse else from_less_to_more

        for i in range(n - 1):
            for j in range(i + 1, n):
                perform_comparison(i, j)

    def inserting_sort(self, reverse: bool = False) -> None:
        n = len(self)

        def from_less_to_more(key, j_elem): 
            return key < j_elem

        def from_more_to_less(key, j_elem): 
            return key > j_elem

        preform_comparison = from_more_to_less if reverse else from_less_to_more

        for i in range(1, n):
            key = self[i]
            j = i - 1

            while j >= 0 and preform_comparison(key, self[j]):
                self[j + 1] = self[j]
                j -=1

            self[j + 1] = key
 
    def selecting_sort(self, reverse: bool = False) -> None:
        n = len(self)

        def from_less_to_more(extreme_elem, j_elem):
            return extreme_elem > j_elem

        def from_more_to_less(extreme_elem, j_elem):
            return extreme_elem < j_elem

        perform_comparison = from_more_to_less if reverse else from_less_to_more

        for i in range(n - 1):
            extereme = i

            for j in range(i + 1, n):
                if perform_comparison(self[extereme], self[j]):
                    extereme = j

            self[extereme], self[i] = self[i], self[extereme]

    

class DynamicArray(List):
    __type_elements: Type

    def __init__(self, *args, type_elements: Type):
        self.__type_elements = type_elements
        if not all(isinstance(arg, self.__type_elements) for arg in args):
            raise ValueError("all array elements must be of the same type")
        
        super().__init__(args)

def is_sorted(arr, reverse: bool = False):
    answer = "Sorted"
    ansi = "\033[37m\033[42m{}\033[0m"

    for i in range(len(arr) - 1):
        if (reverse and arr[i] < arr[i + 1]) or (not reverse and arr[i] > arr[i + 1]):
            answer = "Not sorted"
            ansi = "\033[37m\033[41m{}\033[0m"

    print(ansi.format(answer))

if __name__ == "__main__":
    array = Array(type_elements=int, length=10)
    # array: List = [None] * 10
    min_number = 56
    max_number = 6583

    for i in range(len(array)):
        array[i] = floor((random() * (max_number - min_number + 1)) + min_number)

    print(array)
    array.selecting_sort(reverse=True)
    print(array)
    is_sorted(array, reverse=True)