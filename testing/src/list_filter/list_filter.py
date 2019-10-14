def list_filter (x, xs):
    return [ y for y in xs if y < x ]

##############################
## testing
##############################

def test_empty():
    assert list_filter (4, []) == []

def test_sharp1():
    assert list_filter (4, [4]) == [4]

def test_sharp2():
    assert list_filter (4, [3]) == [3]

def test_sharp3():
    assert list_filter (4, [5]) == []

def test_uniform1():
    assert list_filter (4, [1,3,5]) == [1,3]

def test_uniform2():
    assert list_filter (4, [1,5,4]) == [1,4]
