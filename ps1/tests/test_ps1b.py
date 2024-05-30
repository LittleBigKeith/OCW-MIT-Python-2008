import math
from ps1.src.ps1b import *
import pytest

def test_sum_of_log_of_prime_up_to_3():
    assert pytest.approx(sum_of_log_of_prime_up_to_n(3)) == math.log(2)

def test_sum_of_log_of_prime_up_to_4():
    assert pytest.approx(sum_of_log_of_prime_up_to_n(4)) == math.log(2) + math.log(3)

def test_sum_of_log_of_prime_up_to_6():
    assert pytest.approx(sum_of_log_of_prime_up_to_n(6)) == math.log(2) + math.log(3) + math.log(5)

def test_sum_of_log_of_prime_up_to_12():
    assert pytest.approx(sum_of_log_of_prime_up_to_n(12)) == math.log(2) + math.log(3) + math.log(5) + math.log(7) + math.log(11)

def test_sum_of_log_of_prime_up_to_20():
    assert pytest.approx(sum_of_log_of_prime_up_to_n(20)) == math.log(2) + math.log(3) + math.log(5) + math.log(7) + math.log(11) + math.log(13) + math.log(17) + math.log(19)

