#!/usr/bin/env python3

def implies(x: bool, y: bool) -> bool:
    return not x or y

################################################################################
# Implementations
################################################################################

def leap_correct_1(year: int) -> bool:
    assert year > 1582
    return year % 4 == 0 and implies(year % 100 == 0, year % 400 == 0)

def leap_correct_2(year: int) -> bool:
    assert year > 1582
    return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)

# Violates test `reject_irregular`.
def leap_wrong_1(year: int) -> bool:
    return year % 4 == 0

# Violates test `accept_irregular`.
def leap_wrong_2(year: int) -> bool:
    return year % 4 == 0 and not year % 100 == 0

# Violates test `accept_regular`.
def leap_wrong_3(year: int) -> bool:
    return year % 8 == 0 and implies(year % 100 == 0, year % 400 == 0)

# Violates test `reject_regular`.
def leap_wrong_4(year: int) -> bool:
    return year % 2 == 0 and implies(year % 100 == 0, year % 400 == 0)

# Violates tests `reject_regular`, `accept_regular` and `accept_irregular`.
def leap_wrong_5(year: int) -> bool:
    return year % 4 != 0 and implies(year % 100 == 0, year % 400 == 0)

# Choose implementation for testing.
def leap(year: int) -> bool:
    return leap_correct_1(year)
