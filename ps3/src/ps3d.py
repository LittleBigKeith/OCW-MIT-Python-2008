from .ps3b import *
from .ps3c import *

def subStringMatchExactlyOneSub(target,key): 
    exact_matches = subStringMatchExact(target, key)
    max_one_off_matches = subStringMatchOneSub(target, key)
    return tuple(sorted(list(set(max_one_off_matches).difference(set(exact_matches)))))