from array import array
from typing import Any, List, Iterable, SupportsIndex, Tuple, TypeVar, Type
from math import floor
from random import randrange

from _generate_random_numbers import generate_random_numbers

_T = TypeVar("_T")

# Classic array: static length, only one type of elements
class Array(list):
    __type_elements: Tuple[Type]

    def __init__(self, *args: Any, type_elements: Tuple[Type], length: int = None):
        self.__type_elements = (type_elements,)
        if not all(arg in self.__type_elements for arg in args):
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
            if self[dicrement] in self.__type_elements:
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
    
    @property
    def is_sorted(self):
        if self[0] > self[1]:
            for i in range(len(self) - 1):
                if self[i] < self[i + 1]:
                    return False
        else:
            for i in range(len(self) - 1):
                if self[i] > self[i + 1]:
                    return False
        
        return True

    def bubble_sort(self, reverse: bool = False) -> None:
        n = len(self)

        def from_less_to_more(i, j):
            if self[i] > self[j]:
                self[i], self[j] = self[j], self[i]

        def from_more_to_less(i, j):
            if self[i] < self[j]:
                self[i], self[j] = self[j], self[i]

        perform_comparison = from_more_to_less if reverse else from_less_to_more

        for i in range(n - 1):
            for j in range(i + 1, n):
                perform_comparison(i, j)

    def inserting_sort(self, reverse: bool = False) -> None:
        n = len(self)

        def from_less_to_more(key, i_elem):
            return key < self[j]

        def from_more_to_less(key, i_elem):
            return key > self[j]
        
        perform_comparison = from_more_to_less if reverse else from_less_to_more

        for i in range(1, n):
            key = self[i]
            j = i - 1

            while j >= 0 and perform_comparison(key, self[j]):
                self[j + 1] = self[j]
                j -= 1

            self[j + 1] = key

    def selection_sort(self, reverse: bool = False) -> None:
        n = len(self)

        def from_less_to_more(extereme_elem, j_elem):
            return extereme_elem > j_elem

        def from_more_to_less(extereme_elem, j_elem):
            return extereme_elem < j_elem

        perform_comparison = from_more_to_less if reverse else from_less_to_more

        for i in range(n - 1):
            extreme_idx = i

            for j in range(i + 1, n):
                if perform_comparison(self[extreme_idx], self[j]):
                    extreme_idx = j
            
            self[extreme_idx], self[i] = self[i], self[extreme_idx]

    def linear_search(self, target: Any) -> int:
        if type(target) not in self.__type_elements: 
            raise ValueError("the type of the element you are looking for must match the type of the array elements")

        for i in range(len(self)):
            if self[i] == target:
                return i
            
        return -1

    def binary_search(self, target: Any) -> int:
        if type(target) not in self.__type_elements: 
            raise ValueError("the type of the element you are looking for must match the type of the array elements")
        if not self.is_sorted:
            raise ValueError("Sort the array before using binary search")
        
        start = 0
        end = len(self) - 1

        while start <= end:
            middle = (start + end) // 2

            if self[middle] == target:
                return middle
            elif self[middle] < target:
                start = middle + 1
            else:
                end = middle

        return -1


class DynamicArray(list):
    __type_elements: Tuple[Type]

    def __init__(self, *args, type_elements: Tuple[Type]):
        self.__type_elements = (type_elements,)

        if not all(arg in self.__type_elements for arg in args):
            raise ValueError("all array elements must be of the same type")
        
        super().__init__(args)

    def append(self, elem: _T, /) -> None:
        if type(elem) not in self.__type_elements: 
            raise ValueError("the type of the element you are looking for must match the type of the array elements")
        
        super().append(elem)

    @property
    def is_empty(self) -> bool:
        return False if self else True 


if __name__ == "__main__":
    length = 10

    user_array = Array(type_elements=int, length=length)
    # array: List = [None] * 10
    for i in range(length):
        user_array[i] = generate_random_numbers(mode_return="one")

    print(user_array)
    user_array.selection_sort(reverse=False)
    print(user_array)
    print(f"is sorted: {"\033[42m{}\033[0m".format(user_array.is_sorted)}")
    target_elem = user_array[randrange(length)]
    print(f"Element: {target_elem}, its index: {user_array.binary_search(target_elem)}")

    array_num = array('i', [0, 1, 2, 3, 4])
    print(array_num)