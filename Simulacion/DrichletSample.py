import numpy as np
import matplotlib.pyplot as plt
from matplotlib import tri

# ----------------------------------------------------------------------------------------------------------------------
# Metodo: Usando distribuciones Gamma podemos generar muestras de una Dirichlet multivariable. Sin embargo, no podemos
# generar muestras de una Dirichlet de una sola variable usando este metodo, ya que la muestra seria un arreglo de
# unos.
# ----------------------------------------------------------------------------------------------------------------------


def dirichlet_samp(params, size):
    """
    Generates a sample from a multivariate Dirichlet using Gammas
    :param params: The parameters [a1, ..., ak] from the distribution
    :param size: The size of the Sample
    :return: The length 'size' sample of the distribution.
    """

    S = []
    for i in range(size):
        gammas = [np.random.gamma(a, 1) for a in params]
        sample = [v / sum(gammas) for v in gammas]
        S.append(sample)
    return np.array(S)


# Graficando el contorno de las distribuciones.


def plot_points(X, barycentric=True, border=True, **kwargs):
    """
    Plots a set of points in the simplex.
    :param X:: A 2xN array (if in Cartesian coords) or 3xN array
    (if in barycentric coords) of points to plot.
    :param barycentric: (bool): Indicates if `X` is in barycentric coords.
    :param border:  If True, the simplex border is drawn.
    :param kwargs: Keyword args passed on to `plt.plot`.
    """

    _corners = np.array([[0, 0], [1, 0], [0.5, 0.75 ** 0.5]])
    _triangle = tri.Triangulation(_corners[:, 0], _corners[:, 1])

    if barycentric is True:
        X = X.dot(_corners)
    plt.plot(X[:, 0], X[:, 1], 'o', ms=1, **kwargs)
    plt.axis('equal')
    plt.xlim(0, 1)
    plt.ylim(0, 0.75**0.5)
    plt.axis('off')
    if border is True:
        plt.triplot(_triangle, linewidth=1)


def dirichlet_compare(params, size):
    """
    Compares the plot of the generated sample with the actual distribution
    using the function above to plot the points into a triangle.
    :param params: The parameters of the distribution
    :param size: The size of the sample
    """

    plot = plt.figure()
    plot_points(dirichlet_samp(params, size), label='Generated')
    plot_points(np.random.dirichlet(params, size), label='Target')
    plot.suptitle(f'Dirichlet sample \nParameters = {params}', fontsize=16)
    plt.legend(loc='best')
    plt.show()


# Ejecutando el programa

def main():
    p_0 = [0.999, 0.999, 0.999]
    p_1 = [5, 5, 5]
    p_2 = [1, 2, 2]
    p_3 = [2, 15, 15]
    P = [p_0, p_1, p_2, p_3]
    size = 5000
    for p in P:
        dirichlet_compare(p, size)


if __name__ == '__main__':
    main()

