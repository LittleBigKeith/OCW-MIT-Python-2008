from ps3.src.ps3d import *

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

def test_find_near_match_of_key11_in_target1_returns_11():
    assert subStringMatchExactlyOneSub(target1, key11) == (11,)

def test_find_near_match_of_key12_in_target1_returns_0():
    assert subStringMatchExactlyOneSub(target1, key12) == (0,)

def test_find_near_match_of_key13_in_target1_returns_():
    assert subStringMatchExactlyOneSub(target1, key13) == ()

def test_find_near_match_of_key14_in_target1_returns_7_17():
    assert subStringMatchExactlyOneSub(target1, key14) == (7, 17)

def test_find_near_match_of_key15_in_target1_returns_7_13():
    assert subStringMatchExactlyOneSub(target1, key15) == (7, 13)

def test_find_near_match_of_key16_in_target1_returns_17():
    assert subStringMatchExactlyOneSub(target1, key16) == (17, )

def test_find_near_match_of_key17_in_target1_returns_():
    assert subStringMatchExactlyOneSub(target1, key17) == ()

def test_find_near_match_of_key18_in_target1_returns_():
    assert subStringMatchExactlyOneSub(target1, key18) == ()

def test_find_near_match_of_key11_in_target2_returns_():
    assert subStringMatchExactlyOneSub(target2, key11) == ()

def test_find_near_match_of_key12_in_target2_returns_0_8_12():
    assert subStringMatchExactlyOneSub(target2, key12) == (0, 8, 12)

def test_find_near_match_of_key13_in_target2_returns_0_8_12():
    assert subStringMatchExactlyOneSub(target2, key13) == (0, 8, 12)

def test_find_near_match_of_key14_in_target2_returns_2_6_10_20():
    assert subStringMatchExactlyOneSub(target2, key14) == (2, 6, 10, 20)

def test_find_near_match_of_key15_in_target2_returns_14():
    assert subStringMatchExactlyOneSub(target2, key15) == (14,)

def test_find_near_match_of_key16_in_target2_returns_2_6_10_14():
    assert subStringMatchExactlyOneSub(target2, key16) == (2, 6, 10, 14)

def test_find_near_match_of_key17_in_target2_returns_2_6_10():
    assert subStringMatchExactlyOneSub(target2, key17) == (2, 6, 10)

def test_find_near_match_of_key18_in_target2_returns_():
    assert subStringMatchExactlyOneSub(target2, key18) == ()