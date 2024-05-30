import math

def sum_of_log_of_prime_up_to_n(n):
    nomin = 2
    sum_of_log = 0
    while nomin < n:
        for denom in range(2, math.floor(math.sqrt(nomin)) + 1):
            if nomin % denom == 0:
                nomin += 1
                break
        else:
            sum_of_log += math.log(nomin)
            nomin += 1
            
    return sum_of_log
