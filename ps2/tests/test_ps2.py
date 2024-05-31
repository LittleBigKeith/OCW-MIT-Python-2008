from ps2.src.ps2 import *

default_packages = (6, 9, 20)

def test_6_mcnuggets_combination_is_001():
    assert find_mcnugget_combination_for_generic(6, default_packages) == {(1, 0, 0)}

def test_9_mcnuggets_combination_is_010():
    assert find_mcnugget_combination_for_generic(9, default_packages) == {(0, 1, 0)}

def test_12_mcnuggets_combination_is_200():
    assert find_mcnugget_combination_for_generic(12, default_packages) == {(2, 0, 0)}

def test_15_mcnuggets_combination_is_110():
    assert find_mcnugget_combination_for_generic(15, default_packages) == {(1, 1, 0)}

def test_20_mcnuggets_combination_is_001():
    assert find_mcnugget_combination_for_generic(20, default_packages) == {(0, 0, 1)}

def test_35_mcnuggets_combination_is_111():
    assert find_mcnugget_combination_for_generic(35, default_packages) == {(1, 1, 1)}