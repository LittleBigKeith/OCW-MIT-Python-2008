from src.ps2 import *
from src.ps2a import *

for n in range(50, 56):
    combinations = find_mcnugget_combination_for_generic(n, (6, 9, 20))
    print(n, combinations)

print("Largest number of McNuggets that cannot be bought in exact quantity:", find_largest_unbuyable_mcnuggets())