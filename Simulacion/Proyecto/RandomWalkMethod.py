import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import time

# Definimos una funcion que nos permita simular un dado de cuatro caras.
def d4():
    return np.random.choice([1, 2, 3, 4])

# Definimos una funcion que nos permita escoger una direccion aleatoria.
def rnd_direction():
    n = d4()
    if n == 1:
        return np.array([1, 0])
    elif n == 2:
        return np.array([0, 1])
    elif n == 3:
        return np.array([-1, 0])
    elif n == 4:
        return np.array([0, -1])

# Definimos una funcion que cree una "cuadricula" con el valor de phi en la frontera.
def make_grid(rows, columns, boundary=5):
    grid = np.zeros((rows, columns))
    grid[0, :] = boundary
    return grid

# Definimos una funcion que cree una "malla" para graficar despues.
def make_mesh(rows, columns):
    x_temp = np.arange(0, rows, 1)
    y_temp = np.arange(0, columns, 1)
    x, y = np.meshgrid(x_temp, y_temp)
    return x, y

# Definimos una funcion que resuelva laplace para un solo punto.
def _point_solve(grid, p_0, num_walks):
    grid_boundary = []
    for i in range(num_walks):
        point = np.array([p_0[0], p_0[1]])
        while True:
            point += rnd_direction()

            if point[0] % (grid.shape[0] - 1) == 0 or point[1] % (grid.shape[1] - 1) == 0:
                grid_boundary.append(grid[point[0], point[1]])
                break
    grid[p_0[0], p_0[1]] = np.mean(np.array(grid_boundary))
    return grid[p_0[0], p_0[1]]

# Definimos una funcion que resuelva para todos los puntos en la cuadricula.
def area_solve(grid, num_walks):
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            _point_solve(grid, (i, j), num_walks)
    x, y = make_mesh(grid.shape[0], grid.shape[1])
    f = lambda s, t: grid[s, t]
    z = f(x, y)

    return x, y, z

# Definimos una funcion que nos permita graficar la solucion en un area.
def plot_solution(grid, num_walks, show=False):
    x, y, z = area_solve(grid, num_walks)
    fig = plt.figure(figsize=(18, 10))
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(x, y, z)
    ax.set_title('Solucion por caminatas aleatorias')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel(r'$V(x,y)$')
    if show:
        plt.show()

# Definimos una funciones que nos permita analizar el tiempo de maquina para ambas funciones.

def time_point_solve(grid, p_0, show=False):
    T_sim = []
    walks = [5 * n for n in range(1, 250)]
    for walk in walks:
        tic = time.time()
        _point_solve(grid, p_0, walk)
        toc = time.time()
        T_sim.append(toc - tic)
    f = lambda n: T_sim[-1] / walks[-1] * n
    T_expected = f(np.array(walks))
    plt.plot(walks, T_sim, label='Simulacion')
    plt.plot(walks, T_expected, '-r', label='Estimacion')
    plt.legend(loc='best')
    plt.xlabel('Iteraciones (numero de caminatas)')
    plt.ylabel('Tiempo (segundos)')
    if show:
        plt.show()

def time_area_solve(grid, show=False):
    T_sim = []
    walks = [5 * n for n in range(1, 250)]
    for walk in walks:
        tic = time.time()
        area_solve(grid, walk)
        toc = time.time()
        T_sim.append(toc - tic)
    f = lambda n: T_sim[-1] / walks[-1] * n
    T_expected = f(np.array(walks))
    plt.scatter(walks, T_sim, label='Simulacion')
    plt.plot(walks, T_expected, '-r', label='Estimacion')
    plt.legend(loc='best')
    plt.xlabel('Iteraciones (numero de caminatas)')
    plt.ylabel('Tiempo (segundos)')
    if show:
        plt.show()