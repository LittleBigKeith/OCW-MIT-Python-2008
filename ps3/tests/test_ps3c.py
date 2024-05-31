from ps3.src.ps3c import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key14 = 'gta'
key15 = 'gtac'
key16 = 'gtat'
key17 = 'gtatg'
key18 = 'gtatgat'

def test_find_near_match_of_key11_in_target1_returns_0_5_11_15():
    assert subStringMatchOneSub(target1, key11) == (0, 5, 11, 15)

def test_find_near_match_of_key12_in_target1_returns_0_5_15():
    assert subStringMatchOneSub(target1, key12) == (0, 5, 15)

def test_find_near_match_of_key13_in_target1_returns_5_15():
    assert subStringMatchOneSub(target1, key13) == (5, 15)

def test_find_near_match_of_key14_in_target1_returns_7_13_17():
    assert subStringMatchOneSub(target1, key14) == (7, 13, 17)

def test_find_near_match_of_key15_in_target1_returns_7_13():
    assert subStringMatchOneSub(target1, key15) == (7, 13)

def test_find_near_match_of_key16_in_target1_returns_13_17():
    assert subStringMatchOneSub(target1, key16) == (13, 17)

def test_find_near_match_of_key17_in_target1_returns_13():
    assert subStringMatchOneSub(target1, key17) == (13,)

def test_find_near_match_of_key18_in_target1_returns_():
    assert subStringMatchOneSub(target1, key18) == ()

def test_find_near_match_of_key11_in_target2_returns_0_4_8_12_18():
    assert subStringMatchOneSub(target2, key11) == (0, 4, 8, 12, 18)

def test_find_near_match_of_key12_in_target2_returns_0_4_8_12_18():
    assert subStringMatchOneSub(target2, key12) == (0, 4, 8, 12, 18)

def test_find_near_match_of_key13_in_target2_returns_0_4_8_12_18():
    assert subStringMatchOneSub(target2, key13) == (0, 4, 8, 12, 18)

def test_find_near_match_of_key14_in_target2_returns_2_6_10_14_20():
    assert subStringMatchOneSub(target2, key14) == (2, 6, 10, 14, 20)

def test_find_near_match_of_key15_in_target2_returns_14():
    assert subStringMatchOneSub(target2, key15) == (14,)

def test_find_near_match_of_key16_in_target2_returns_2_6_10_14():
    assert subStringMatchOneSub(target2, key16) == (2, 6, 10, 14)

def test_find_near_match_of_key17_in_target2_returns_2_6_10():
    assert subStringMatchOneSub(target2, key17) == (2, 6, 10)

def test_find_near_match_of_key18_in_target2_returns_():
    assert subStringMatchOneSub(target2, key18) == ()