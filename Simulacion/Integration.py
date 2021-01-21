from math import exp


def power(x, t):
    return x ** t


def int_power(a, b, n):
    rie_sum = 0
    for k in range(1, n + 1):
        rie_sum += exp(a + (b - a) * k / n) / (a + (b - a) * k / n)
    return ((b - a) / n) * rie_sum


print(int_power(1, 100, 1000000))