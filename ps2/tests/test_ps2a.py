from ps2.src.ps2a import *

def test_six_consecutive_buyable():
    array = [1, 3, 4, 5, 6, 7, 8]
    assert check_six_consecutive_solutions(array, 14) == True

def test_not_six_consecutive_buyable():
    array = [1, 3, 4, 5, 6, 7, 8]
    assert check_six_consecutive_solutions(array, 13) == False