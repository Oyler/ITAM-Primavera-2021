import matplotlib.pyplot as plt
from math import gcd, sqrt
import numpy as np

# Function to generate a list of pseudorandom numbers for plotting


def fast_glc(seed, m, a, c):
    Z = np.zeros(int(m), dtype=np.longdouble)
    Z[0] = seed
    k = 1.0
    while k < m:
        z = (a * Z[int(k) - 1] + c) % m
        if z == seed:
            Z[int(k)] = z
            break
        else:
            Z[int(k)] = z
        k += 1.0
    return Z


# Function to make a scatter plot of the glc.


def glc_plot(data, s):
    x = np.arange(np.longdouble(len(data)))
    plt.scatter(x, data, s=s)
    plt.show()


# Function that generates a list of the prime factors of n


def prime_factors(n):
    factors = [1]
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n = int(n / 2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n = int(n / i)
    if n > 2:
        factors.append(n)
    return factors


# Function that shows if a GLC will have a complete cycle


def has_complete_cycle(mod, mult, c):
    flag = True
    reason = "Has complete cycle"
    if gcd(mod, c) != 1:
        flag = False
        reason = f"gcd({mod}, {c}) is not 1"

    if flag:
        for f in prime_factors(mod):
            if (mult - 1) % f != 0:
                flag = False
                reason = f"factor {f} does not divide {mult} - 1"
                break
    if flag:
        if mod % 4 == 0 and mult % 4 != 1:
            flag = False
            reason = f"4 divides {mod} but not {mult} - 1"
    return flag, reason

'''
# Ejemplo de periodo completo
test = [[16, 13, 13], [16, 12, 13], [2 ** 10, 25437, 35421], [13, 1, 12],
        [2 ** 48, 2814749767109, 59482661568307]]
for sample in test:
    flag, reason = has_complete_cycle(sample[0], sample[1], sample[2])
    print([flag, reason])


# Test plots
test_0 = np.array([1024, 401, 101], dtype=np.longdouble)
test_1 = np.array([2 ** 12, 1664525, 1013904223], dtype=np.longdouble)
test_2 = np.array([2 ** 25, 1664525, 1013904223], dtype=np.longdouble)
data_0 = fast_glc(5, test_0[0], test_0[1], test_0[2])
data_1 = fast_glc(3, test_1[0], test_1[1], test_1[2])
data_2 = fast_glc(3, test_2[0], test_2[1], test_2[2])

plt.figure(figsize=(10, 10))
glc_plot(data_0, 8)
plt.figure(figsize=(10, 10))
glc_plot(data_1, 2)
plt.figure(figsize=(18, 18))
glc_plot(data_2, 0.0001)
'''