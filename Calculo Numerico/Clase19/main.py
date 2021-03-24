import numpy as np
import matplotlib.pyplot as plt

def paso_flexible(f, w_p, t_p, t_max, tol, teta):
    t_rel = tol * max(np.linalg.norm(w_p, np.inf), teta)
    h = t_max - t_p
    s_1, s_2 = 0, 0

    e_h = 1
    flag = True
    while flag:
        s_1 = f(t_p, w_p)
        s_2 = f(t_p + h, w_p + h * s_1)
        s_3 = f(t_p + 0.5 * h, w_p + 0.5 * h * (s_1 + s_2))

        e_h = h * (s_1 - 2 * s_3 + s_2) / 3

        if np.linalg.norm(e_h, np.inf) < t_rel:
            flag = False
        else:
            h *= 0.5

    t_f = t_p + h
    w_f = w_p + 0.5 * h * (s_1 + s_2)
    h_sug = 2 * h
    return t_f, w_f, h_sug


def mRK23(f, u_0, I, h_max, tol, teta):
    """
    :param teta: angle
    :param f: function handle (rhs of ODE).
    :param u_0: initial value.
    :param I: [t_0, T].
    :param h_max: longest allowed step.
    :param tol: tolerance (relative).
    :return: t_s: vector of times (M + 1), w_s: matrix (n x M + 1) where n
             = length(u_0)
    """
    t_s = np.matrix([I[0], I[0]]).T
    print(t_s)
    w_s = np.matrix([u_0, u_0]).T
    print(w_s)
    t = I[1]
    h_sug = h_max

    _ = 0
    flag = True
    while flag:
        t_max = min(t, t_s[_] + h_sug)
        t_f, w_f, h_sug = paso_flexible(f, w_s[:, _], t_s[_], t_max, tol, teta)
        h_sug = min(h_max, h_sug)
        t_s.append(t_f)
        w_s[:].append(w_f)

        if t_f == t:
            flag = False
        else:
            _ += 1
    return t_s, w_s

def main():
    r = 1
    R = 5

    def sol(t):
        return np.matrix([r * np.cos(t), R * np.sin(t)]).T

    def f(t, u):
        return np.matrix([-r / R * u[1], R / r * u[0]]).T

    I = [0, 2 * np.pi]
    u_0 = sol(I[0])
    h_max = 1
    tol = 1e-3
    teta = 1 / 4
    t_s, w_s = mRK23(f, u_0, I, h_max, tol, teta)

    t_ss = np.linspace(I[0], I[1], 257)
    vsol =np.vectorize(sol)
    u_s = vsol(t_ss)
    plt.plot(u_s[0, :], u_s[1, :], '*')
    plt.plot(w_s[0, :], w_s[1, :])
    plt.show()


if __name__ == '__main__':
    main()