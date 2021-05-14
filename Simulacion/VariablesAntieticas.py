import numpy as np
import matplotlib.pyplot as plt

def solve_integral(func, steps):
    u_1 = np.random.uniform(0, 1, steps)
    u_2 = np.random.uniform(0, 1, steps)
    U = np.array(list(zip(u_1, u_2)))
    theta_1 = np.array([func(u[0], u[1]) for u in U])
    theta_2 = np.array([func(1 - u[0], 1 - u[1]) for u in U])
    T = np.array(list(zip(theta_1, theta_2)))
    theta = np.array([(t[0] + t[1]) / 2 for t in T])
    theta_cap = np.mean(theta)
    std_theta = np.std(theta)
    return  theta_cap, std_theta


if __name__ == '__main__':
    f = lambda x, y: np.exp((x + y) ** 2)
    int_f, std = solve_integral(f, 10000)
    print(int_f)
    print(std)

