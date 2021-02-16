import matplotlib.pyplot as plt
import numpy as np
import RejectionSampling as rs

# For the first unknown density we are told its mass function is given by f(t) = 3t^2/2. Integrating we get a CDF
# given by F(t) = t^3/2, which has an inverse F_inv(t) = (2t)^(1/3). To generate a sample we will use the Inverse
# Transform Method, with a slight alteration. Our target function is even and thus symetric around 0, because of the way
# the algorithm works, we would only be able to graph the positive side of the function (as U is in [0,1]). However,
# we can create a second uniform random variable to randomly (with the same uniform distribution) change the sign of
# our target value, thus sampling the whole density.


def gen_density1(size):
    S = np.zeros(size)
    for i in range(size):
        u = np.random.uniform(0, 1)
        aux = np.random.uniform(0, 1)
        t = (2 * u) ** (1 / 3)
        S[i] = t if aux >= 0.5 else -t

    return S


def f_density1(size, bounds):
    t = np.linspace(bounds[0], bounds[1], size)
    f = (3 * t ** 2) / 2
    return f

# The next unknown density is a picewise monstrosity to choose an appropiate method, we first need to plot the function
# from the looks of it, inversion won't work so we might need to use the accept-reject method. The function itself seems
# to be contained within the interval (0, 1) and seems to contain another parameter a which is contained in (0, 1/2).
# To properly test our algorithm we wil be showing two cases, one for a = 0.125 and another for a = 0.375. Since this
# is a picewise function we need to first define f as a single value output and then program it as before.


def __f2__(t):
    a = 0.25
    f = 0
    if 0 <= t < a:
        f = t / (a * (1 - a))
    elif a <= t < 1 - a:
        f = 1 / (1 - a)
    elif 1 - a <= t <= 1:
        f = (1 - t) / (a * (1 - a))
    else:
        f = 0
    return f


def f_density2(size, bounds):
    vfun = np.vectorize(__f2__) # <-- Vectorising the function
    t = np.linspace(bounds[0], bounds[1], size)
    f = vfun(t)
    return f

# Now we move on to do rejection sampling which is further explained in my RejectionSampling.py file.


def gen_density2(size, bounds):
    vfun = np.vectorize(__f2__)
    return rs.rejection_sampling(vfun, size, bounds)

# The following function will be used to compare the target plot to the generated sample. The parameters are gen_sample
# which is the generated sample, target_func which is the list of values of the target function and bounds which is a
# tuplet containing the range of the function.


def plot_compare(gen_sample, target_func, bounds):
    size = len(target_func)
    t = np.linspace(bounds[0], bounds[1], size)
    plot = plt.figure()
    plt.hist(gen_sample, density=True, bins=20, rwidth=0.75, range=bounds, label='Simulation')
    plt.plot(t, target_func, label='Target Density')
    plot.suptitle('Uknown Density', fontsize=16)
    plt.legend(loc='best')
    plt.show()

# Now we write a program that will allow us to do what we need


def main():
    size = 5000
    bounds_1 = (-1, 1)
    bounds_2 = (0, 1)

    density1 = gen_density1(size)
    func1 = f_density1(size, bounds_1)

    density2 = gen_density2(size, bounds_2)
    func2 = f_density2(size, bounds_2)

    plot_compare(density1, func1, bounds_1)
    plot_compare(density2, func2, bounds_2)

if __name__ == '__main__':
    main()

