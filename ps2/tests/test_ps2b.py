from ps2.src.ps2b import *

def test_max_unbuyable_for_6_9_20_is_43():
    packages = (6,9,20)   # variable that contains package sizes
    assert find_max_unbuyable_under_200(packages) == 43

def test_max_unbuyable_for_1_2_3_is_0():
    packages = (1,2,3)
    assert find_max_unbuyable_under_200(packages) == 0

def test_max_unbuyable_for_3_5_7_is_4():
    packages = (3,5,7)
    assert find_max_unbuyable_under_200(packages) == 4

def test_max_unbuyable_for_5_7_9_is_13():
    packages = (5,7,9)
    assert find_max_unbuyable_under_200(packages) == 13

def test_max_unbuyable_for_5_11_19_is_28():
    packages = (5,11,19)
    assert find_max_unbuyable_under_200(packages) == 28

def test_max_unbuyable_for_7_13_19_is_50():
    packages = (7,13,19)
    assert find_max_unbuyable_under_200(packages) == 50

def test_max_unbuyable_for_11_15_18_is_79():
    packages = (11,15,18)
    assert find_max_unbuyable_under_200(packages) == 79

def test_max_unbuyable_for_2_4_6_is_199():
    packages = (2,4,6)
    assert find_max_unbuyable_under_200(packages) == 199

def test_max_unbuyable_for_3_6_9_is_199():
    packages = (3,6,9)
    assert find_max_unbuyable_under_200(packages) == 199
