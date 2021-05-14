# =====================================================================================================================
#                           A series of examples using the Brownian() class.
# =====================================================================================================================

from Brownian import Brownian
import matplotlib.pyplot as plt

def main():

    # Example 1: Process with an initial value of zero and using random walk.
    # We can use a basic stochastic process such as Random Walk, to generate the data points for Brownian motion.
    b_1 = Brownian()
    example_1 = plt.figure(0)
    for i in range(4):
        plt.plot(b_1.gen_random_walk(1000))
    example_1.suptitle('Generation via Random Walk.', fontsize=16)
    plt.show()

    # Example 2: Process with an initial value of 20 and using Normal distribution
    # We can generate Brownian motion data by drawing from Normal distribution.
    b_2 = Brownian(20)
    example_2 = plt.figure(1)
    for i in range(4):
        plt.plot(b_2.gen_normal(1000))
    example_2.suptitle('Generation via Normal Distribution.', fontsize=16)
    plt.show()

    # Example 3: We implemented the Geometric Brownian Motion model in the class as a method. In the demo, we simulate
    # multiple scenarios with for 52 time periods (imagining 52 weeks a year). Note, all the stock prices start at the
    # same point but evolve randomly along different trajectories.
    b_3 = Brownian()

    # We define a utility function for plotting first.

    def plot_stock_price(mu, sigma, delta_t=52, dt=0.1):
        """
        Plots stock price for multiple scenarios
        """
        example_3 = plt.figure(figsize=(9, 4))
        for _ in range(5):
            plt.plot(b_3.stock_price(mu=mu, sigma=sigma, delta_t=delta_t, dt=dt))
        plt.legend(['Scenario-' + str(_) for _ in range(1, 6)], loc='upper left')
        plt.hlines(y=100, xmin=0, xmax=520, linestyle='--', color='k')
        example_3.suptitle(f'Stock price simulation\n\u03BC: {mu}, \u03C3: {sigma}', fontsize=16)
        plt.show()

    # Note that, although the scenarios look sufficiently stochastic, they have a downward trend. This is because even
    # with a positive mean, we have a slightly high spread or volatility.
    plot_stock_price(mu=0.2, sigma=0.7)

    # A slight change in the volatility
    # We simulate the stock price again with slightly less volatility (but with the same mean as before) and get a
    # completely different outcome this time. The trend looks neutral i.e. some scenario shows an increase in the stock
    # price after the 52-week time period, whereas some show a decrease.
    plot_stock_price(mu=0.2, sigma=0.6)

    # Lowering the volatility further down
    # If we lower the volatility, even more, we get a clear positive trend.
    plot_stock_price(mu=0.2, sigma=0.6)

    # Example 4: Consider a stock that does not pay dividends with mu = 15% and sigma = 30%. With time t = 0 at price
    # S_0 = 100.
    plot_stock_price(mu=0.15, sigma=0.3)

    # Example 5: Consider three independent realizations of a stock with initial value S_0 = 100, drift = 0.1 and
    # volatility = 0.3
    plot_stock_price(mu=0.1, sigma=0.3)

    b_3.twoD_plot(1000)


if __name__ == '__main__':
    main()