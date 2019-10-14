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

################################################################################
# Tests
################################################################################

def test_leap_reject_regular():
    # Not divisible by 4 => not divisible by 100 and 400 => regular non-leap year
    assert not leap(1601)
    assert not leap(1602)
    assert not leap(1603)
    assert not leap(1605)

def test_leap_accept_regular():
    # Divisible by 4, but not by 100 => not divisible by 400 => regular leap year.
    assert leap(1604)
    assert leap(1608)
    assert leap(1612)
    assert leap(1616)

def test_leap_reject_irregular():
    # divisible by 4 and 100, but not by 400 => irregular non-leap year
    assert not leap(1700)
    assert not leap(1800)
    assert not leap(1900)
    assert not leap(2100)

def test_leap_accept_irregular():
    # Divisible by 4, 100, and 400 => irregular leap year.
    assert leap(1600)
    assert leap(2000)
    assert leap(2400)
    assert leap(2800)
