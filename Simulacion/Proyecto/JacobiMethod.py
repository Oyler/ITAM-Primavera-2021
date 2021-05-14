import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time

# Este codigo es tomado de https://www.compphy.com/laplace-equation/

def Jacobi_Solution(N_iter):
    Rmax = 16  ##number of rows
    Cmax = 16  # number of columns
    V = np.zeros((Rmax, Cmax))  ## Creating Potential function array
    V0 = 5
    V[0, :] = V0  # SETTING UP BOUNDARY CONDITIONS i.e. making zeroth row equal to 100 unit
    for iter in range(N_iter):
        ##creating auxiliary array same as Earlier
        aux = np.zeros((Rmax, Cmax))
        aux[0, :] = V0
        #########################################33333

        ##Visiting each lattice points excluding boundary , leave them alone !
        for i in range(1, (Rmax - 1)):
            for j in range(1, (Cmax - 1)):
                ##calculating potential at each point and storing them
                ##in auxiliary array but not udpdating the main potential array
                aux[i, j] = 0.25 * (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1])

        V = aux  ## Updating Potential function array after visiting each site
    #########################################################33


    ##Code for plotting in 3D

    x = range(0, Rmax, 1)  ## calculating descrete lattice
    y = range(0, Cmax, 1)
    X, Y = np.meshgrid(x, y)  ##creating 2D mesh


    def f():
        z = V[X, Y]  ##giving value to each point of mesh
        return z


    Z = f()
    return X, Y, Z

# Definimos una funcion que nos permita visualizar la solucion para un area:
def plot_solution(N_iter, show=False):
    x, y, z = Jacobi_Solution(N_iter)
    fig = plt.figure(figsize=(18, 10))
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(x, y, z)
    ax.set_title('Solucion por Jacobi')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel(r'$V(x,y)$')
    if show:
        plt.show()

# Definimos una funcion que nos permita analizar el tiempo de maquina
# (el algoritmo es el mismo para un area que para un punto)

def time_Jacobi(show=False):
    T_sim = []
    walks = [5 * n for n in range(1, 250)]
    for walk in walks:
        tic = time.time()
        Jacobi_Solution(walk)
        toc = time.time()
        T_sim.append(toc - tic)
    f = lambda n: T_sim[-1] / walks[-1] * n
    T_expected = f(np.array(walks))
    plt.scatter(walks, T_sim, label='Simulacion (Jacobi)')
    plt.plot(walks, T_expected, '-r', label='Estimacion (Jacobi)')
    plt.legend(loc='best')
    plt.xlabel('Iteraciones')
    plt.ylabel('Tiempo (segundos)')
    if show:
        plt.show()