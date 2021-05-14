import numpy as np
import matplotlib.pyplot as plt

def normal(x, mu, sigma):
    numerator = np.exp((-(x - mu) ** 2)/(2 * sigma ** 2))
    denominator = sigma * np.sqrt(2 * np.pi)
    return numerator / denominator

def rand_coin(p):
    u = np.random.uniform(0, 1)
    return True if u < p else False

def gaussian_mcmc(hops, mu, sigma):
    states = []
    burn_in = int(hops * 0.2)
    current = np.random.uniform(-5 * sigma + mu, 5 * sigma + mu)
    for i in range(hops):
        states.append(current)
        movement = np.random.uniform(-5 * sigma + mu, 5 * sigma + mu)

        curr_prob = normal(x=current, mu=mu, sigma=sigma)
        move_prob = normal(x=movement, mu=mu, sigma=sigma)

        acceptance = min(move_prob / curr_prob, 1)
        if rand_coin(acceptance):
            current = movement
    return states[burn_in:]


if __name__ == '__main__':
    lines = np.linspace(-4, 4, 1000)
    normal_curve = [normal(t, mu=0, sigma=1) for t in lines]
    dist = gaussian_mcmc(100000, mu=0, sigma=1)
    plt.hist(dist, density=True, bins=30, rwidth=0.75, range=(-4, 4))
    plt.plot(lines, normal_curve)
    plt.show()