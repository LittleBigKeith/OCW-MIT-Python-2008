from .ps2 import *

def find_max_unbuyable_under_200(packages):
    bestSoFar = 0     # variable that keeps track of largest number
                    # of McNuggets that cannot be bought in exact quantity

    for n in range(1, 200):
        combinations = find_mcnugget_combination_for_generic(n, packages)
        if len(combinations) == 0:
            bestSoFar = n

    return bestSoFar