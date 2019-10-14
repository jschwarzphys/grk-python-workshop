#!/usr/bin/env python3

################################################################################
# Implementations
################################################################################

# Takes two lines, represented by two points each, and returns their
# intersection point, if it exists and is unique, and otherwise `None`.
def intersect_correct(p1, p2, q1, q2):
    nominator   = (p1[0] - q1[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - q1[1]) * (q1[0] - q2[0])
    denominator = (p1[0] - p2[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - p2[1]) * (q1[0] - q2[0])
    if denominator != 0:
        t = nominator / denominator
        return (
            p1[0] + t * (p2[0] - p1[0]),
            p1[1] + t * (p2[1] - p1[1]),
        )

# Error: Missing check for zero division.
# Violates `parallel`, `same`, `commute_*` tests.
def intersect_wrong_1(p1, p2, q1, q2):
    nominator   = (p1[0] - q1[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - q1[1]) * (q1[0] - q2[0])
    denominator = (p1[0] - p2[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - p2[1]) * (q1[0] - q2[0])
    t = nominator / denominator
    return (
        p1[0] + t * (p2[0] - p1[0]),
        p1[1] + t * (p2[1] - p1[1]),
    )

# Violates `non_trivial` and `commute_*` tests.
def intersect_wrong_2_1(p1, p2, q1, q2):
    # Error: Addition instead of subtraction  ------v
    nominator   = (p1[0] - q1[0]) * (q1[1] - q2[1]) + \
                  (p1[1] - q1[1]) * (q1[0] - q2[0])
    denominator = (p1[0] - p2[0]) * (q1[1] - q2[1]) + \
                  (p1[1] - p2[1]) * (q1[0] - q2[0])
    if denominator != 0:
        t = nominator / denominator
        return (
            p1[0] + t * (p2[0] - p1[0]),
            p1[1] + t * (p2[1] - p1[1]),
        )

# Violates `non_trivial` and `commute_*` tests.
def intersect_wrong_2_2(p1, p2, q1, q2):
    nominator   = (p1[0] - q1[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - q1[1]) * (q1[0] - q2[0])
    denominator = (p1[0] - p2[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - p2[1]) * (q1[0] - q2[1])
    # Error: Wrong index -----------------------^
    if denominator != 0:
        t = nominator / denominator
        return (
            p1[0] + t * (p2[0] - p1[0]),
            p1[1] + t * (p2[1] - p1[1]),
        )

# Error: Swapped definitions of `denominator` and `nominator`.
# Violates `axes` (but not `non_trivial`), `parallel`, and `commute_*` tests.
def intersect_wrong_3(p1, p2, q1, q2):
    denominator = (p1[0] - q1[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - q1[1]) * (q1[0] - q2[0])
    nominator   = (p1[0] - p2[0]) * (q1[1] - q2[1]) - \
                  (p1[1] - p2[1]) * (q1[0] - q2[0])
    if denominator != 0:
        t = nominator / denominator
        return (
            p1[0] + t * (p2[0] - p1[0]),
            p1[1] + t * (p2[1] - p1[1]),
        )

def intersect(p1, p2, q1, q2):
    # return intersect_wrong_1(p1, p2, q1, q2)
    # return intersect_wrong_2_1(p1, p2, q1, q2)
    # return intersect_wrong_2_2(p1, p2, q1, q2)
    # return intersect_wrong_3(p1, p2, q1, q2)
    return intersect_correct(p1, p2, q1, q2)
