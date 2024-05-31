from ps3.src.ps3b import *

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
target3 = 'messy assess compass sss'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key31 = 's'
key32 = 'ss'

def test_target1_key10_returns_0_3_5_9_11_12_15_19():
    assert subStringMatchExact(target1, key10) == (0, 3, 5, 9, 11, 12, 15, 19)

def test_target1_key11_returns_0_5_15():
    assert subStringMatchExact(target1, key11) == (0, 5, 15)

def test_target1_key12_returns_5_15():
    assert subStringMatchExact(target1, key12) == (5, 15)

def test_target1_key13_returns_5_15():
    assert subStringMatchExact(target1, key13) == (5, 15)


def test_target2_key10_returns_0_3_4_8_12_16_17_18_22():
    assert subStringMatchExact(target2, key10) == (0, 3, 4, 8, 12, 16, 17, 18, 22)

def test_target2_key11_returns_0_4_8_12_18():
    assert subStringMatchExact(target2, key11) == (0, 4, 8, 12, 18)

def test_target2_key12_returns_4_18():
    assert subStringMatchExact(target2, key12) == (4, 18)

def test_target2_key13_returns_4_18():
    assert subStringMatchExact(target2, key13) == (4, 18)

def test_target3_key31_returns_2_3_7_8_10_11_18_19_21_22_23():
    assert subStringMatchExact(target3, key31) == (2, 3, 7, 8, 10, 11, 18, 19, 21, 22, 23)

def test_target3_key32_returns_2_7_10_18_21_22():
    assert subStringMatchExact(target3, key32) == (2, 7, 10, 18, 21, 22)