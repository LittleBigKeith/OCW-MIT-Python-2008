import math

def nth_prime(n):
    count = 0
    nomin = 1
    while count < n:
        nomin += 1
        for denom in range(2, math.floor(math.sqrt(nomin)) + 1):
            if nomin % denom == 0:
                break
        else:
            count += 1
    return nomin
