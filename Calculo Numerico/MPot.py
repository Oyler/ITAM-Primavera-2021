# El metodo de potencias se usa para encontrar el eigenpar dominante de una matriz A
from numpy import *


def __find_p(x):
    return argwhere(isclose(abs(x), linalg.norm(x, inf))).min()


def __iterate(A, x, p):
    y = dot(A, x)
    mu = y[p]
    p = __find_p(y)
    err = linalg.norm(x - y / y[p], inf)
    x = y / y[p]

    return err, p, mu, x


def power_method(A, tol, imax):
    mu = 0
    n = A.shape[0]
    x = ones(n)
    p = __find_p(x)
    err = 1
    x = x / x[p]
    i = 0
    flag = True
    while flag:
        err, p, mu, x = __iterate(A, x, p)
        i += 1
        flag = i < imax and err >= tol
    return mu, x


A = array([[0, 1, 0], [0, 0, 1], [-1, 1.5, 1.5]])
mu, x = power_method(A, 1e-10, 1000)
print(mu)
print(x)