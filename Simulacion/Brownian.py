# =====================================================================================================================
# Brownian motion, or pedesis, is the randomized motion of molecular-sized particles suspended in a fluid. It results
# from the stochastic collisions of the particles with the fast-moving molecules in the fluid (energized due to the
# internal thermal energy). The aforementioned fluid is supposed to be at the so-called thermal equilibrium, where no
# preferential direction of flow exists (as opposed to various transport phenomena).
# ---------------------------------------------------------------------------------------------------------------------
# The core equation at the heart of generating data points following a Brownian motion dynamics is rather simple,
#
#               W(i / n) = W((i - 1) / n) + Y_i / sqrt(n)
# where Yi could be a basic stochastic process like Random Walk or sample from a Normal distribution.
# ---------------------------------------------------------------------------------------------------------------------
# In this python file we define a Brownian() class with a few useful methods:
#
# > gen_random_walk(): Generates motion from the Random Walk process.
# > gen_normal(): Generates motion by drawing from the Normal Distribution.
# > stock_price(): Models a stock price using the so-called 'Geometric Brownian Motion' formula.
#
# =====================================================================================================================

import numpy as np
import matplotlib.pyplot as plt

class Brownian():
    def __init__(self, x_0=0):
        """
        Init class.

        :param x_0: The initial value.
        """
        assert(type(x_0) == float or type(x_0) == int or x_0 is None), "Expected a float or None for the initial value"
        self.x_0 = float(x_0)

    # Getters and setters.

    def get_init_value(self):
        return self.x_0

    def set_init_value(self, x_0):
        self.x_0 = x_0

    def gen_random_walk(self, n_steps=100):
        """
        Generate motion by random walk.

        :param n_steps: Number of steps.
        :return: A numpy array with 'n_steps' points.
        """

        # WARNING about small number of steps.
        if n_steps < 30:
            print("WARNING! The number of steps is small. It may not generate a good stochastic process sequence!")
        w = np.ones(n_steps) * self.x_0

        for i in range(1, n_steps):
            # Sampling from the Normal distribution with probability 1/2.
            y_i = np.random.choice([1, -1])

            # Weiner process
            w[i] = w[i - 1] + (y_i / np.sqrt(n_steps))

        return w

    def gen_normal(self, n_steps=100):
        """
        Generate motion by drawing from a normal distribution.

        :param n_steps: Number of steps.
        :return: A numpy array with 'n_steps' points.
        """

        # WARNING about small number of steps.
        if n_steps < 30:
            print("WARNING! The number of steps is small. It may not generate a good stochastic process sequence!")

        w = np.ones(n_steps) * self.x_0

        for i in range(1, n_steps):

            # Sampling from the Normal distribution
            y_i = np.random.normal()

            # Weiner process
            w[i] = w[i - 1] + (y_i / np.sqrt(n_steps))

        return w

    def stock_price(self, s_0=100, mu=1, sigma=1, delta_t=52, dt=0.1):
        """
        Models a stock price S(t) using the Weiner process W(t) as`S(t) = S(0).exp{(mu-(sigma^2/2).t)+sigma.W(t)}`.

        :param s_0: Initial stock price, default = 100.
        :param mu: 'Drift' of the stock (upwards or downwards), default = 1.
        :param sigma: 'Volatility' of the stock, default = 1.
        :param delta_t: The time period for which the future prices are computed, default 52 (as in 52 weeks).
        :param dt: The granularity of the time-period, default = 0.1.
        :return: s: A NumPy array with the simulated stock prices over the time-period delta_t.
        """

        n_steps = int(delta_t / dt)
        time_v = np.linspace(0, delta_t, num=n_steps)

        # stock variation.
        stock_var = (mu - (sigma ** 2/2)) * time_v

        # Forcefully set the initial value to zero for the stock price simulation.
        self.set_init_value(0)

        # Weiner process (calls the `gen_normal` method)
        weiner_process = sigma * self.gen_normal(n_steps)

        # Add two time series, take exponent, and multiply by the initial stock price
        s = s_0 * (np.exp(stock_var + weiner_process))

        return s
