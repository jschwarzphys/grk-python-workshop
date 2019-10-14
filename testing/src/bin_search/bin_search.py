def search(item, seq):
    """binary search"""
    left = 0
    right = len(seq)
    while left < right:
        middle = (left + right) // 2
        middle_element = seq[middle]
        if middle_element == item:
            return middle
        elif middle_element < item:
            left = middle + 1
        else:
            right = middle
    raise ValueError("Value not in sequence")

######################################################################
## testing

def test_left_end ():
    r = search (1, [1,2,3])
    assert r == 0
    r = search (1, [1,2,3,4])
    assert r == 0

def test_right_end ():
    r = search (3, [1,2,3])
    assert r == 2
    r = search (4, [1,2,3,4])

def test_empty ():
    import pytest
    with pytest.raises (ValueError):
        r = search (42, [])
    with pytest.raises (ValueError):
        r = search (0, [1,3,5])
    with pytest.raises (ValueError):
        r = search (4, [1,3,5])
    with pytest.raises (ValueError):
        r = search (60, [1,3,5])

