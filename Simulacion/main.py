import numpy as np
import matplotlib.pyplot as plt


def roll_dice(n):
    return [np.random.randint(1, 7) + np.random.randint(1, 7) for i in range(n)]


dices = roll_dice(10000)
plt.hist(dices)
plt.show()