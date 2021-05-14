import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = [9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 10, 8, 9, 9, 8, 9, 9, 9, 10, 10, 10, 10, 10]
    no_cards_by_psa = dict(Counter(data))
    print(no_cards_by_psa)
    # plt.hist(data, density=True)
    mean = 9
    std = 1 / (3.5 * np.sqrt(2 * np.pi))
    variance = np.square(std)
    x = np.arange(-10, 40, .01)
    f = np.exp(-np.square(x - mean) / 2 * variance) / (np.sqrt(2 * np.pi * variance))

    plt.plot(x, f)
    plt.ylabel('gaussian distribution')
    plt.show()
