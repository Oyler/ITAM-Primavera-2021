# En este archivo analizamos nuestra solucion a la ecuacion de laplace y comparamos con el metodo de Jacobi
import Proyecto.RandomWalkMethod as rwm
import Proyecto.JacobiMethod as jm
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # Ponemos una semilla para poder recrear los resultados en el futuro.
    np.random.seed(42069)
    # Colocamos los parametros iniciales para reusar en cada prueba.
    grid = rwm.make_grid(16, 16)
    n_iter = 5000
    # Primero graficamos la solucion en area del metodo propuesto y comparamos con el metodo de jacobi
    # rwm.plot_solution(grid, n_iter, show=True)
    # jm.plot_solution(n_iter, show=True)

    # Ahora analizamos el tiempo de maquina de ambos metodos, primero por separado y luego en conjunto.
    # rwm.time_area_solve(grid, show=True)
    jm.time_Jacobi(show=True)


    # Ahora analizamos el tiempo de maquina para un solo punto escogido al azar.
    #xcord = np.random.randint(0, 16)
    #ycord = np.random.randint(0, 16)
    #rwm.time_point_solve(grid, (xcord, ycord), show=True)
    #jm.time_Jacobi(show=True)
