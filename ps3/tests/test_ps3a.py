from ps3.src.ps3a import *

def test_trololololo_contains_4_olo():
    assert countSubStringMatch("trololololo", "olo") == 4
    assert countSubStringMatchRecursive("trololololo", "olo") == 4

def test_102102102_contains_3_102():
    assert countSubStringMatch("102102102", "102") == 3
    assert countSubStringMatchRecursive("102102102", "102") == 3

def test_atgacatgcacaagtatgcat_contains_4_ca():
    assert countSubStringMatch("atgacatgcacaagtatgcat", "ca") == 4
    assert countSubStringMatchRecursive("atgacatgcacaagtatgcat", "ca") == 4

def test_atgacatgcacaagtatgcat_contains_3_tg():
    assert countSubStringMatch("atgacatgcacaagtatgcat", "tg") == 3
    assert countSubStringMatchRecursive("atgacatgcacaagtatgcat", "tg") == 3

def test_atgacatgcacaagtatgcat_contains_4_at():
    assert countSubStringMatch("atgacatgcacaagtatgcat", "at") == 4
    assert countSubStringMatchRecursive("atgacatgcacaagtatgcat", "at") == 4

def test_atgacatgcacaagtatgcat_contains_0_ct():
    assert countSubStringMatch("atgacatgcacaagtatgcat", "ct") == 0
    assert countSubStringMatchRecursive("atgacatgcacaagtatgcat", "ct") == 0

def test_atgacatgcacaagtatgcat_contains_1_gt():
    assert countSubStringMatch("atgacatgcacaagtatgcat", "gt") == 1
    assert countSubStringMatchRecursive("atgacatgcacaagtatgcat", "gt") == 1

def test_atgacatgcacaagtatgcat_contains_22_():
    assert countSubStringMatch("atgacatgcacaagtatgcat", "") == 22
    assert countSubStringMatchRecursive("atgacatgcacaagtatgcat", "") == 22

def test_atgacatgcacaagtatgcat_contains_9_a():
    assert countSubStringMatch("atgacatgcacaagtatgcat", "a") == 8
    assert countSubStringMatchRecursive("atgacatgcacaagtatgcat", "a") == 8

def test_atgaatgcatggatgtaaatgcag_contains_2_ca():
    assert countSubStringMatch("atgaatgcatggatgtaaatgcag", "ca") == 2
    assert countSubStringMatchRecursive("atgaatgcatggatgtaaatgcag", "ca") == 2

def test_atgaatgcatggatgtaaatgcag_contains_5_tg():
    assert countSubStringMatch("atgaatgcatggatgtaaatgcag", "tg") == 5
    assert countSubStringMatchRecursive("atgaatgcatggatgtaaatgcag", "tg") == 5

def test_atgaatgcatggatgtaaatgcag_contains_5_at():
    assert countSubStringMatch("atgaatgcatggatgtaaatgcag", "at") == 5
    assert countSubStringMatchRecursive("atgaatgcatggatgtaaatgcag", "at") == 5

def test_atgaatgcatggatgtaaatgcag_contains_0_ct():
    assert countSubStringMatch("atgaatgcatggatgtaaatgcag", "ct") == 0
    assert countSubStringMatchRecursive("atgaatgcatggatgtaaatgcag", "ct") == 0

def test_atgaatgcatggatgtaaatgcag_contains_1_gt():
    assert countSubStringMatch("atgaatgcatggatgtaaatgcag", "gt") == 1
    assert countSubStringMatchRecursive("atgaatgcatggatgtaaatgcag", "gt") == 1

def test_atgaatgcatggatgtaaatgcag_contains_25_():
    assert countSubStringMatch("atgaatgcatggatgtaaatgcag", "") == 25
    assert countSubStringMatchRecursive("atgaatgcatggatgtaaatgcag", "") == 25

def test_atgaatgcatggatgtaaatgcag_contains_9_a():
    assert countSubStringMatch("atgaatgcatggatgtaaatgcag", "a") == 9
    assert countSubStringMatchRecursive("atgaatgcatggatgtaaatgcag", "a") == 9