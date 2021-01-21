from random import *
from numpy import *
import matplotlib.pyplot as plt


def roll(iterations):
    P9 = iterations * [0]
    P10 = iterations * [0]
    for i in range(iterations):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        die3 = randint(1, 6)
        sum = die1 + die2 + die3
        if sum == 9:
            P9[i] = 1
        elif sum == 10:
            P10[i] = 1

    p_9 = cumsum(P9)
    p_10 = cumsum(P10)
    p9 = [i / j for i, j in zip(p_9, range(1, iterations))]
    p10 = [i / j for i, j in zip(p_10, range(1, iterations))]

    return p9, p10


x, y = roll(10000)
plt.plot(y, color='tab:orange', label='P(S=10) aprox')
plt.axhline(y=(0.1 + 0.05 / 2), color='k', linestyle='--', label='P(S=10) real')
plt.plot(x, color='tab:blue', label='P(S=9) aprox')
plt.axhline(y=0.1127, color='tab:gray', linestyle='--', label='P(S=9) real')
plt.legend(loc='best')
plt.show()





