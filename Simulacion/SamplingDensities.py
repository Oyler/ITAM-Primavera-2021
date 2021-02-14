# ---------------------------------------------------------------------------------------------------------------------
# In this file we will generate samples of several random variables of different density functions using the Inverse
# Function Theorem.
#
# The step to generate variables in such way are as follow,
#   -Get the CDF of the random variable
#   -Find its inverse
#   -Generate a uniform random variable U on (0, 1)
#   -Apply the inverse CDF to U
#   -Repeat N times to get an N sized sample.
#
# For each random variable we will have a generated one gen_name(), the actual mass function f_name() and a
# name_comparison_plot() that will plot the generated sample and the PMF to compare them.
#
# Finally we will create a function to calculate the estimation of the distribution, that we will use for all of the
# generated samples.
# ---------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# The Standard Cauchy has a PMF f(x) = 1 / (pi * (1 + x ** 2)) and a CDF F(x) = 1 / pi * arctan(x) + 1 / 2
# its inverse CDF is F_inv(x) = tan(pi * (x - 1 / 2)), alternatively we can generate two uniform variables U1 and U2,
# and split the sample in two, having U1 select a sign and using U2 to generate the sample.


def gen_cauchy(size):
    S = np.zeros(size)
    for i in range(size):
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        c = np.tan(np.pi * (u2 / 2))
        S[i] = c if u1 >= 1 / 2 else -c
    return S


def f_cauchy(size, bounds):
    t = np.linspace(bounds[0], bounds[1], size)
    f = 1 / (np.pi * (1 + t ** 2))
    return t, f


def cauchy_comp_plot(sample_size, pmf_bounds):
    cauchy_sim = gen_cauchy(sample_size)
    t, f = f_cauchy(sample_size, pmf_bounds)
    cauchy = plt.figure(0)
    plt.hist(cauchy_sim, density=True, bins=30, rwidth=0.75, range=pmf_bounds, label='Simulation')
    plt.plot(t, f, label='Density')
    cauchy.suptitle('Cauchy sample', fontsize=16)
    plt.legend(loc='best')
    plt.show()

# The Standard Gumbel has a PMF f(x) = e ** -(x + e ** (-x)) and a CDF F(x) = e ** (-e ** (-x)), thus the inverse CDF
# would be F_inv(x) = ln(1 / ln(1 / x)). Using this and following the steps explained at the beginning, we can simulate
# a sample of this random variable. Because of 1 / x we will have to set the bounds of our uniform variable U to
# (epsilon, 1) where epsilon is near zero but not zero.


def gen_gumbel(size):
    S = np.zeros(size)
    for i in range(size):
        u = np.random.uniform(0.0000001, 1)
        g = np.log(1 / np.log(1 / u))
        S[i] = g
    return S


def f_gumbel(size, bounds):
    t = np.linspace(-3, 10, 100000)
    g = np.e ** -(t + np.e ** (-t))
    return t, g


def gumbel_comp_plot(sample_size, pmf_bounds):
    gumbel_sim = gen_gumbel(sample_size)
    t, f = f_gumbel(sample_size, pmf_bounds)
    gumbel = plt.figure(1)
    plt.hist(gumbel_sim, density=True, bins=30, rwidth=0.75, range=pmf_bounds, label='Simulation')
    plt.plot(t, f, label='Density')
    gumbel.suptitle('Gumbel sample', fontsize=16)
    plt.legend(loc='best')
    plt.show()

# The Standard Logistic distribution has a PMF given by f(x) = e ** (-x) / (1 + e ** (-x)) ** 2 and a CDF given by
# F(X) = 1 / (1 + e ** (-x)), thus its inverse CDF is given by F_inv(x) = ln(x / (1 - x)) for x in [0, 1). This time
# because of 1 / (1 - x) we will set the bounds of U to be [0, 1) not including 1. Following the steps explained at
# the beginning we will simulate a logistic distribution.


def gen_logistic(size):
    S = np.zeros(size)
    for i in range(size):
        u = np.random.uniform(0, 1)
        l = np.log(u / (1 - u))
        S[i] = l
    return S


def f_logistic(size, bounds):
    t = np.linspace(bounds[0], bounds[1], size)
    l = np.e ** (-t) / ((1 + np.e ** (-t)) ** 2)
    return t, l


def log_comp_test(sample_size, pmf_bounds):
    log_sim = gen_logistic(sample_size)
    t, l_f = f_logistic(sample_size, pmf_bounds)
    logistic = plt.figure(2)
    plt.hist(log_sim, density=True, bins=30, rwidth=0.75, range=pmf_bounds, label='Simulation')
    plt.plot(t, l_f, label='Density')
    logistic.suptitle('Logistic sample', fontsize=16)
    plt.legend(loc='best')
    plt.show()

# The Pareto distribution has a PMF given by f(x) = (a * c ** a) / (x ** (a + 1)) for a, c > 0 and x > c. For this
# sample we will be setting c = 1 and a = 2. Thus f(x) = 2 / x ** 3. Thus the CDF is given by F(X) = 1 - (x ** (-2))
# thus its inverse CDF is F_inv(x) = sqrt(1 / (1 - x)). Using the steps mentioned at the beginning we generate a sample.


def gen_pareto(size):
    S = np.zeros(size)
    for i in range(size):
        u = np.random.uniform(0, 1)
        p = (1 / (1 - u)) ** 0.5
        S[i] = p
    return S


def f_pareto(size, bounds):
    t = np.linspace(bounds[0], bounds[1], size)
    p = 2 / (t ** 3)
    return t, p


def pareto_comp_test(sample_size, pmf_bounds):
    pareto_sim = gen_pareto(sample_size)
    t, p = f_pareto(sample_size, pmf_bounds)
    pareto = plt.figure(3)
    plt.hist(pareto_sim, density=True, bins=30, rwidth=0.75, range=pmf_bounds, label='Simulation')
    plt.plot(t, p, label='Density')
    pareto.suptitle('Pareto sample', fontsize=16)
    plt.legend(loc='best')
    plt.show()

# *********************************************************************************************************************
# Now we use the functions defined above to generate random samples of size 5000 and get the estimator for the values
# n = 50, 100, 150, ..., 5000 of each random variable. We will also be graphing this estimators.
# *********************************************************************************************************************


def main():
    # Starting parameters
    size = 5000
    n_vals = [50 * (k + 1) for k in range(100)]

    # Plotting the samples
    cauchy_comp_plot(size, (-5, 5))
    gumbel_comp_plot(size, (-3, 10))
    log_comp_test(size, (-5, 5))
    pareto_comp_test(size, (1, 5))

    # Generating an array of estimators for each random variable:
    cauchy_est = [sum(gen_cauchy(n)) / n for n in n_vals]
    gumbel_est = [sum(gen_gumbel(n)) / n for n in n_vals]
    log_est = [sum(gen_logistic(n)) / n for n in n_vals]
    pareto_est = [sum(gen_pareto(n)) / n for n in n_vals]

    # Printing the arrays:
    print('Cauchy:')
    print(cauchy_est)
    print('\nGumbel')
    print(gumbel_est)
    print('\nLogistic')
    print(log_est)
    print('\nPareto')
    print(pareto_est)

    # Graphing each one of them.
    cauchy_est_plt = plt.figure(4)
    plt.hist(cauchy_est, density=True, bins=30, rwidth=0.75, range=(-5, 5))
    cauchy_est_plt.suptitle('Cauchy estimator sample', fontsize=16)
    plt.show()

    gumbel_est_plt = plt.figure(5)
    plt.hist(gumbel_est, density=True, bins=30, rwidth=0.75)
    gumbel_est_plt.suptitle('Gumbel estimator sample', fontsize=16)
    plt.show()

    log_est_plt = plt.figure(6)
    plt.hist(log_est, density=True, bins=30, rwidth=0.75)
    log_est_plt.suptitle('Logistic estimator sample', fontsize=16)
    plt.show()

    pareto_est_plt = plt.figure(7)
    plt.hist(pareto_est, density=True, bins=30, rwidth=0.75)
    pareto_est_plt.suptitle('Pareto estimator sample', fontsize=16)
    plt.show()

    return 'Process completed'


if __name__ == "__main__":
    main()


