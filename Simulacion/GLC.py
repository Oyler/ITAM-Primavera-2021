import matplotlib.pyplot as plt
from math import gcd, sqrt

# Function to generate a list of pseudorandom numbers for plotting


def glc(seed, mod, mult, c):
    Z = [[0],[seed]]
    for i in range(1, mod + 1):
        z = (mult * Z[1][i - 1] + c) % mod
        if z in Z[1]:
            break
        else:
            Z[0].append(i)
            Z[1].append(z)
    return Z


# Function to plot the pseudorandom numbers


def glc_plot(seed, mod, mult, c):
    x, y = glc(seed, mod, mult, c)
    plt.scatter(x, y)
    plt.show()


# Function to print the list of pseudorandom numbers


def print_list(lst):
    for k in range(len(lst)):
        print(lst[k])


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
'''
# GLC, grafica de dispersion
# glc_plot(5, 1024, 401, 101)
