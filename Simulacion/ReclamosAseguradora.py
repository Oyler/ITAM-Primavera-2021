import numpy as np
import scipy.stats as sp

def raw_sim(func, size):
    g = []
    for i in range(21):
        u = np.random.uniform(0, 1, size)
        y = func(u, i)
        g.append(np.mean(y))
    temp = [1/np.math.factorial(i) * g[i] for i in range(len(g))]
    return 1 - sum(temp)

def estimate_1(func, size):
    u = np.random.uniform(0, 1, size)
    x_u = np.array([np.random.poisson(func(t)) for t in u])
    opt = sp.linregress(x_u, u)
    u2 = np.random.uniform(0, 1, size)
    x = np.array([np.random.poisson(func(t)) for t in u2])
    v = x + opt * (u2 - 0.5)
    return sum(v <= 20) / size

def estimate_2(func, n):
    g = []
    for i in range(21):
        u = np.random.uniform(0, 1, n)
        y_1 = func(u, i)
        y_2 = func(1 - u, i)
        g.append((np.mean(y_1) + np.mean(y_2)) / 2)
    temp = [1 / np.math.factorial(i) * g[i] for i in range(len(g))]
    return 1 - sum(temp)


if __name__ == '__main__':
    f = lambda x, y: np.exp(-15 / (0.5 + x)) * (15 / (0.5 + x)) ** y
    p = raw_sim(f, 10000)
    print(p)
    f1 = lambda x: np.exp(-15 / (0.5 + x)) * (15 / (0.5 + x))
    # p1 = estimate_1(f1, 10000)
    p2 = estimate_2(f, 10000)
    print(p2)
