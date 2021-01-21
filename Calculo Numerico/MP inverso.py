# El metodo de potencia inverso es una modificacion del metodo de potencia
# que da una convergencia mas rapida. Se usa para determinar el eigenvalor de A
# mas cercano a un numero especifico q

from numpy import *
from MPot import __find_p


def inverse_pm(A, tol, imax):
    n = A.shape[0]
    x = ones(n)
    I = eye(n)
    mu = 0

    q = dot(x, dot(A, x)) / dot(x, x)
    p = __find_p(x)
    x = x / x[p]

    err = 1
    i = 0
    flag = True

    while flag:
        y = linalg.solve( A - q * I, x)
        mu = y[p]
        p = __find_p(y)
        err = linalg.norm(x - y / y[p], inf)
        x = y / y[p]
        mu = 1. / mu + q
        flag = i < imax and err >= tol

    return mu, x


A = array([[0, 1, 0], [0, 0, 1], [-1, 1.5, 1.5]])
mu, x = inverse_pm(A, 1e-12, 1000)
print(mu)
print(x)