import numpy as np
import matplotlib.pyplot as plt

def main():
    trials = 10000
    size = 1000
    S = []
    for k in range(trials):
        arr = np.random.binomial(1, 0.09245, size)
        gam = np.random.gamma(7000, 1, size)
        sum = 0
        for j in range(size):
            if arr[j] == 1:
                sum += gam[j]
        S.append(sum)

    count = 0
    for s in S:
        if s > 500000:
            count += 1

    plot = plt.figure()
    plt.hist(S, density=True, bins=30, rwidth=0.75)
    plot.suptitle("Probabilidad de tener $x en reclamos", fontsize=16)
    plt.xlabel('Cantidad ($) total')
    plt.ylabel('Probabilidad')
    plt.show()
    print(f'The probability is {count / trials}')


if __name__ == "__main__":
    main()
