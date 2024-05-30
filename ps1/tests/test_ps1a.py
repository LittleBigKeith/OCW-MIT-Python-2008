from ps1.src.ps1a import *

def test_1st_prime():
    assert nth_prime(1) == 2

def test_2nd_prime():
    assert nth_prime(2) == 3

def test_3rd_prime():
    assert nth_prime(3) == 5

def test_4th_prime():
    assert nth_prime(4) == 7

def test_5th_prime():
    assert nth_prime(5) == 11

def test_6th_prime():
    assert nth_prime(6) == 13

def test_7th_prime():
    assert nth_prime(7) == 17

def test_8th_prime():
    assert nth_prime(8) == 19

def test_9th_prime():
    assert nth_prime(9) == 23

def test_10th_prime():
    assert nth_prime(10) == 29

def test_100th_prime():
    assert nth_prime(100) == 541

def test_1000th_prime():
    assert nth_prime(1000) == 7919

def test_100_000th_prime():
    assert nth_prime(100_000) == 1299709