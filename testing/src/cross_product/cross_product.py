#!/usr/bin/env python3

################################################################################
# Implementations
################################################################################

def cross_correct(v1, v2):
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0],
    )

# Swapped lhs and rhs of subtraction.
# Violates all `unit_*` tests.
def cross_wrong_1(v1, v2):
    return (
         v1[2] * v2[1] - v1[1] * v2[2],
         v1[0] * v2[2] - v1[2] * v2[0],
         v1[1] * v2[0] - v1[0] * v2[1],
    )

# v1 used exclusively in lhs of subtraction, and v2 in rhs of subtraction.
# violates all `zero_*` and `unit_*` tests.
def cross_wrong_2(v1, v2):
    return (
        v1[1] * v1[2] - v2[2] * v2[1],
        v1[2] * v1[0] - v2[0] * v2[2],
        v1[0] * v1[1] - v2[1] * v2[0],
    )

# Wrong index at bottom right.
# violates `same_2` and `anti_comm` tests.
def cross_wrong_3(v1, v2):
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[1],
        #                          ^- should be v2[0]
    )

# Second and last line are identical.
# violates `unit_1` and `unit_3` tests.
def cross_wrong_4(v1, v2):
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[2] * v2[0] - v1[0] * v2[2], # <-- same line as previous line
    )

def cross(v1, v2):
    # return cross_wrong_1(v1, v2)
    # return cross_wrong_2(v1, v2)
    # return cross_wrong_3(v1, v2)
    # return cross_wrong_4(v1, v2)
    return cross_correct(v1, v2)

################################################################################
# Tests
################################################################################

from pytest import approx

def test_cross_zero_l():
    assert cross((0,0,0),(1,2,3)) == approx((0,0,0))
def test_cross_zero_r():
    assert cross((1,2,3),(0,0,0)) == approx((0,0,0))

def test_cross_unit_1():
    assert cross((1,0,0),(0,1,0)) == approx((0,0,1))
def test_cross_unit_2():
    assert cross((0,1,0),(0,0,1)) == approx((1,0,0))
def test_cross_unit_3():
    assert cross((0,0,1),(1,0,0)) == approx((0,1,0))

def test_cross_same_1():
    assert cross((1,0,0),(1,0,0)) == approx((0,0,0))
def test_cross_same_2():
    assert cross((0,1,0),(0,1,0)) == approx((0,0,0))
def test_cross_same_3():
    assert cross((0,0,1),(0,0,1)) == approx((0,0,0))

# to motivate property based testing?
def test_cross_anti_comm():
    def neg(t):
        return (-t[0], -t[1], -t[2])
    assert cross((1,2,3),(4,5,6)) == approx(neg(cross((4,5,6),(1,2,3))))

# We could also check for
# - Distributivity over +
# - Compatibility with scalar mult
# - Jacobi identity
# but then we would need to define addition and scalar mult on points
# or use something like numpy
