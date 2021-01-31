# https://adventofcode.com/2019/day/4 (part 1)
# How many different passwords within the range
# 284639-748759
# meet these criteria?
#
# - It is a six-digit number.
# - The value is within the range given in your puzzle input.
# - Two adjacent digits are the same (like 22 in 122345).
# - Going from left to right, the digits never decrease; 
#   they only ever increase or stay the same (like 111123 or 135679).
# 
# Other than the range rule, the following are true:
#
# - 111111 meets these criteria (double 11, never decreases).
# - 223450 does not meet these criteria (decreasing pair of digits 50).
# - 123789 does not meet these criteria (no double).

from typing import List


def password_count(start:int, stop:int) -> int:
    return [is_password(i) for i in range(start, stop)].count(True)
   
def is_password(number:int) -> bool:
    number_iterable = list(map(int, str(number)))
    if (len(number_iterable) != 6):
        return False
    if not has_equal_adjacent_digits(number_iterable):
        return False
    if not decreases(number_iterable):
        return False
    return True


def has_equal_adjacent_digits(number:List[int]) -> bool:
    for key, digit in enumerate(number):
        if key+1 in range(0,len(number)):
            if number[key] == number[key+1]:
                return True
    return False

def decreases(number:List[int]) -> bool:
    for key, digit in enumerate(number):
        if key+1 in range(0,len(number)):
            if number[key] > number[key+1]:
                return False
    return True

