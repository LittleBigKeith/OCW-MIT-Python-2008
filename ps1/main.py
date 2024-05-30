import matplotlib.pyplot as plt
import numpy as np
from src.ps1b import sum_of_log_of_prime_up_to_n

xpoints = np.array(range(1, 10000))
ypoints = np.array([sum_of_log_of_prime_up_to_n(n) / n for n in range(1, 10000)])

plt.plot(xpoints, ypoints)
plt.title("ratio of (sum of primes up to n / n) : n")
plt.xlabel("n")
plt.ylabel("sum of primes up to n divided by n")
plt.show()

