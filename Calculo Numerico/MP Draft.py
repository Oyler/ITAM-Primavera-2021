import numpy as np
# El siguiente algoritmo presenta una funcion que usa el metodo de potencias para aproximar el eigenpar dominante de la
# matriz A a partir de una solucion inicial q0 (eigenpar: [u, sig]


def mPot(A, imax, tol, q0):
    # A is a matrix
    # q0 the initial vector
    # imax an upper bound for the number of iterations
    # tol is a relative tolerance
    global sig
    u = q0 / np.sqrt(q0.dot(q0))    # para mejorar velocidad calculamos la norma asi
    i = 1
    flag0 = True
    while flag0:
        x = A.dot(u)
        sig = np.dot(u, x) / np.sqrt(u.dot(u))
        u = x / np.sqrt(x.dot(x))
        err = np.sqrt((x - sig * u).dot((x - sig * u)))
        i += 1
        flag0 = (err > tol) or i < imax

    stop = 'tol' if i < imax else 'imax'
    return u, sig, stop


A = [[0, 1, 0], [0, 0, 1], [-1, 1.5, 1.5]]
A = np.array(A)
q0 = np.ones(3)

lam, sig, flag = mPot(A, 100, 1e-12, q0)
print(lam)
print(sig)
print(flag)
print(1e-12)

