import numpy as np
import matplotlib.pyplot as plt


def exp_den(lam, n, x):
    return lam * np.e ** (-lam * (x - n))


def gen_exp2(lam, n, size, bounds):
    x = np.linspace(bounds[0], bounds[1], size)
    y = exp_den(lam, n, x)
    pmin = 0
    pmax = y.max()

    accept = 0
    trials = 0

    S = []
    while accept < size:
        x = np.random.uniform(bounds[0], bounds[1])
        y = np.random.uniform(pmin, pmax)

        if y < exp_den(lam, n, x):
            S.append(x)
            accept += 1

        trials += 1

    return S


def compare_exp_samp(lam, n, size, bounds):
    exp_samp = gen_exp2(lam, n, size, bounds)
    t = np.linspace(bounds[0], bounds[1], size)
    f = exp_den(lam, n, t)
    exponential = plt.figure()
    plt.hist(exp_samp, density=True, bins=30, rwidth=0.75, range=bounds, label='Simulation')
    plt.plot(t, f, label='Density')
    exponential.suptitle('Exponential sample\nn = {0:.5f}, \u03BB = {1:.5f}'.format(n, lam), fontsize=16)
    plt.legend(loc='best')
    plt.show()


def main():
    tests = 4
    size = 10000
    N = np.random.uniform(0, 5, tests)
    L = np.random.uniform(1, 5, tests)
    B = [(n, 5) for n in N]
    for i in range(tests):
        compare_exp_samp(L[i], N[i], size, B[i])


if __name__ == '__main__':
    main()
