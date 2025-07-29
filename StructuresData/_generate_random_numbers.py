from random import randrange, randint
from typing import List, Literal, Union

MIN_NUM = 54
MAX_NUM = 2032

def generate_random_numbers(
        mode_return: Literal["all", "one"] = "all", 
        *, 
        number_of_numbers: int,
        min_num: int = MIN_NUM,
        max_num: int = MAX_NUM
        ) -> Union[List[int], int]:
    if mode_return == "all":
        return [randrange(min_num, max_num) for i in range(number_of_numbers)]
    elif mode_return == "one":
        return randint(min_num, max_num)
    else:
        raise ValueError("Unknown mode_return value")
    