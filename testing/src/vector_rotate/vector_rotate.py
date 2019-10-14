from math import pi, sin, cos, sqrt

def vector_rotate (p, a):
    (x, y) = p
    phi = a * pi / 180
    return (x * cos (phi) - y * sin (phi), x * sin (phi) + y * cos (phi))

def dot_product (v, w):
    (vx, vy) = v
    (wx, wy) = w
    return vx * wx + vy * wy

def vector_length (v):
    return sqrt (dot_product (v, v))

######################################################################
### testing

from pytest import approx

def test_rot_origin():
    assert vector_rotate ((0,0), 42) == (0, 0)

def test_rot0():
    assert vector_rotate ((10,10), 0) == (10,10)

def test_rot90():
    # assert vector_rotate ((1,0), 90) == (0,1)
    assert vector_rotate ((1,0), 90) == approx((0,1))

def test_length():
    v = (2, 3)
    a = 47
    w = vector_rotate (v, a)
    assert vector_length (v) == vector_length (w)

def test_angle():
    v = (-4, 1)
    a = 31
    w = vector_rotate (v, a)
    phi = a * pi / 180
    assert cos (phi) == dot_product (v, w) / dot_product (v, v)

