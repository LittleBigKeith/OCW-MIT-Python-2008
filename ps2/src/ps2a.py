from .ps2 import *

def check_six_consecutive_solutions(array, n):
    if n - array[-1] >= 6:
        return True
    return False


def find_largest_unbuyable_mcnuggets():
    combinations, unbuyable = set(), list()
    mcnuggets = 1
    while True:
        combinations = find_mcnugget_combination_for_generic(mcnuggets, (6, 9, 20))
        if len(combinations) == 0:
            unbuyable.append(mcnuggets)
        if check_six_consecutive_solutions(unbuyable, mcnuggets):
            return unbuyable[-1]
        mcnuggets += 1