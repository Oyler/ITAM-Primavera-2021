import numpy as np


def uniform_freq(n):
    S = [np.random.uniform(0,1) for _ in range(n)]
    C = []
    for j in range(10):
        count = 0
        for s in S:
            if j / 10 <= s < (j + 1) / 10:
                count += 1
        C.append(count)

    C = [c / n for c in C]
    i = 0

    print(f"\nPrueba para {n} observaciones:\n")
    for c in C:
        print("[{0:.2f}, {1:.2f}): {2:.2f}%".format(i, i + 0.1, c * 100))
        i += 0.1


if __name__ == '__main__':
    uniform_freq(100)
    uniform_freq(500)
    uniform_freq(1000)
    uniform_freq(10000)
    uniform_freq(100000)
    uniform_freq(1200000)
