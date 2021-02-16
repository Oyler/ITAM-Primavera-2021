# ---------------------------------------------------------------------------------------------------------------------
# The Epanechnikov rescaled kernel has a symmetric PMF given by f_e(x) = (3 / 4) * (1 - x ** 2) for x in [-1, 1].
# The following algorithm generates samples of this distribution, we are to code it and prove that they are indeed
# similar if not the same. The algorithm is as follows,
#   -Generate three iid uniform variables U1, U2, U3 on (-1, 1)
#   - if |U3| >= |U2| and |U3| >= |U1| choose U2, otherwise choose U3.
# ---------------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# First we create a function that generates a sample of the Epanechnikov distribution using the algorithm mentioned


def gen_epanechnikov(size):
    S = np.zeros(size)
    for i in range(size):
        u1 = np.random.uniform(-1, 1)
        u2 = np.random.uniform(-1, 1)
        u3 = np.random.uniform(-1, 1)
        S[i] = u2 if abs(u3) >= abs(u2) and abs(u3) >= abs(u1) else u3
    return S

# Then we create a function for the actual probability mass function of the given kernel, namely
# f_e(x) = (3 / 4) * (1 - x ** 2)


def f_epanechnikov(size, bounds):
    t = np.linspace(bounds[0], bounds[1], size)
    f = (3 / 4) * (1 - t ** 2)
    return t, f

# Now we create a function that creates a histogram for the generated sample and plots the kernel.


def ep_comp_plot(sample_size, pmf_bounds):
    ep_sim = gen_epanechnikov(sample_size)
    t, f = f_epanechnikov(sample_size, pmf_bounds)
    ep = plt.figure(0)
    plt.hist(ep_sim, density=True, bins=30, rwidth=0.75, range=pmf_bounds, label='Simulacion')
    plt.plot(t, f, label='Density')
    ep.suptitle('Epanechnikov sample', fontsize=16)
    plt.legend(loc='best')
    plt.show()

# Running the program


def main():
    sample_size = 10000
    pmf_bounds = (-1, 1)
    ep_comp_plot(sample_size, pmf_bounds)


if __name__ == "__main__":
    main()