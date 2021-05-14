import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import seaborn as sb

def student_mcm(num_sim, stationary, df):
    X = [stationary]
    for i in range(num_sim):
        y = sp.t.rvs(1, df)
        rho = sp.t.pdf(y, 1) * sp.t.pdf(X[i], df) / (sp.t.pdf(X[i], 1) * sp.t.pdf(y, df))
        X.append(X[i] + (y - X[i]) * (np.random.uniform(0, 1) < rho))

    return np.array(X)

def normal_mcm(num_sim, stationary):
    X = [stationary]
    for i in range(num_sim):
        y = sp.norm.rvs(1)
        rho = sp.t.pdf(y, 1) * sp.norm.pdf(X[i]) / (sp.t.pdf(X[i], 1) * sp.norm.pdf(y))
        X.append(X[i] + (y - X[i]) * (np.random.uniform(0, 1) < rho))
    return np.array(X)


if __name__ == '__main__':
    # Primero empecemos con un valor grande de x como x = 5, Haremos 10000 Simulaciones.
    data_0 = normal_mcm(10000, 5)
    fig_0= sb.histplot(data_0, stat='density')
    plt.show()
    fig_01 = sb.lineplot(data=data_0)
    plt.show()

    # Ahora tomemos un numero aun mayor, x = 10
    data_1 = normal_mcm(10000, 10)
    fig_1 = sb.histplot(data_1, stat='density')
    plt.show()
    fig_11 = sb.lineplot(data=data_1)
    plt.show()

    # Ahora en lugar de q normal usamos una student con df=1/2
    s = sp.t.rvs(1, 1)
    data_2 = student_mcm(10000, s, 0.5)
    fig_2 = sb.histplot(data_2, stat='density')
    fig_2.set_xlim(-10, 10)
    plt.show()
    fig_21 = sb.lineplot(data=data_2)
    plt.show()

    # Ahora df = 3
    data_3 = student_mcm(10000, s, 3)
    fig_3 = sb.histplot(data_3, stat='density')
    plt.show()
    fig_31 = sb.lineplot(data=data_3)
    plt.show()

    # Ahora Calcula P(X<3) usando una cadena que utiliza q normal o q, t con 0.5 grados.
    s = sp.t.rvs(1, 1)
    data_normal = normal_mcm(10000, s)
    data_t = student_mcm(10000, s, 0.5)
    data_normal = np.cumsum(data_normal < 3) / range(1, len(data_normal) + 1)
    data_t = np.cumsum(data_t < 3) / range(1, len(data_t) + 1)
    sb.lineplot(data=data_t, legend='brief', label='T(1/2)')
    sb.lineplot(data=data_normal, legend='brief', label='normal')
    plt.show()
    print("La probabilidad de que P(X<3) cuando q es una T student es: {0:.5f}".format(sp.t.pdf(3, 1)))