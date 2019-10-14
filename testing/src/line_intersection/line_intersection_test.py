
################################################################################
# Tests
################################################################################

from pytest import approx

def test_intersect_axes():
    assert intersect((-1,0), (1,0), (0,-1), (0,1)) == approx((0,0))

def test_intersect_non_trivial():
    assert intersect((2,1), (4,2), (3,1), (5,3)) == approx((4,2))

def test_intersect_parallel():
    assert intersect((0,0), (1,0), (0,1), (1,1)) is None

def test_intersect_same():
    assert intersect((0,0), (1,0), (0,0), (1,0)) is None

# The next two tests cover the cases of lines degenerated to points.
# I'm not sure if they should be part of the specification (and hence also be tested).

def test_intersect_points_different():
    assert intersect((0,0), (0,0), (1,0), (1,0)) is None

def test_intersect_points_same():
    assert intersect((0,0), (0,0), (0,0), (0,0)) is None

# The next tests might lend themselves for a hint to property based testing.

def test_intersect_commute_points():
    assert intersect((1,2), (3,4), (5,6), (8,7)) == \
           intersect((3,4), (1,2), (8,7), (5,6))

def test_intersect_commute_lines():
    assert intersect((1,2), (3,4), (5,6), (8,7)) == \
           intersect((5,6), (8,7), (1,2), (3,4))
