#!/usr/bin/env python3

################################################################################
# Implementations
################################################################################

def lerp_correct(v1, v2, f):
    return (
        v1[0] * (1 - f) + v2[0] * f,
        v1[1] * (1 - f) + v2[1] * f,
    )

# Behaves as lerp(v1, v2, 1 - f).
# Violates `x`, `y`, `xy`, and `*_bound` tests.
def lerp_wrong_1(v1, v2, f):
    return (
        v1[0] * f + v2[0] * (1 - f),
        v1[1] * f + v2[1] * (1 - f),
    )

# Behaves as weighted sum.
# Violates `same`, and `*_bound` tests.
def lerp_wrong_2(v1, v2, f):
    return (
        v1[0] * f + v2[0] * f,
        v1[1] * f + v2[1] * f,
    )

# Wrong index for y-coordinate.
# Violates `same`, `x`, `y`, and `right_bound`.
def lerp_wrong_3(v1, v2, f):
    return (
        v1[0] * (1 - f) + v2[0] * f,
        v1[1] * (1 - f) + v2[0] * f,
    )

# Wrong index for y-coordinate.
# Violates `y`, `xy`, and `right_bound`.
# The correctness of test `x` suggests that there is a problem in the treatment
# of the `y`-coordinate.
def lerp_wrong_4(v1, v2, f):
    return (
        v1[0] * (1 - f) + v2[0] * f,
        v1[1] * (1 - f) + v1[1] * f,
        #                 ^-- should be v2
    )

def lerp(v1, v2, f):
    # return lerp_wrong_1(v1, v2, f)
    # return lerp_wrong_2(v1, v2, f)
    # return lerp_wrong_3(v1, v2, f)
    # return lerp_wrong_4(v1, v2, f)
    return lerp_correct(v1, v2, f)

################################################################################
# Tests
################################################################################

from pytest import approx

def test_lerp_same():
    assert lerp((1,2), (1,2), 0.234) == approx((1,2))

def test_lerp_x():
    assert lerp((0,0), (1,0), 0.234) == approx((0.234,0))

def test_lerp_y():
    assert lerp((0,0), (0,1), 0.234) == approx((0,0.234))

def test_lerp_xy():
    assert lerp((0,0), (1,1), 0.234) == approx((0.234,0.234))

def test_lerp_left_bound():
    assert lerp((1,2), (3,4), 0) == approx((1,2))

def test_lerp_right_bound():
    assert lerp((1,2), (3,4), 1) == approx((3,4))
