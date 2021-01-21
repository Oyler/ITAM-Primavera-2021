# ---------------------------------------------------------------------------------------------------------------------
#   Simulacion Tarea 1: Dados de Galileo.
#   Descripcion: Si se lanzan tres dados, ¿Que es mas probable sacar 9 o 10?
#
#   Ismael Ancona Tellez           Fecha:  21 / 01 / 21
# ---------------------------------------------------------------------------------------------------------------------

from random import *
from numpy import *
import matplotlib.pyplot as plt

# Primero crearemos una funcion que nos permita
# simular el resultado de lanzar tres dados


def roll():

    d1 = randint(1, 6)
    d2 = randint(1, 6)
    d3 = randint(1, 6)

    # Devolvemos la suma de los 3 dados
    return d1 + d2 + d3

# Ahora creamos una simulacion que simule el experimento n veces,
# aproxime P(sum=9) y P(sum=10) y los grafique.


def die_simulation(num_trials):
    # Usaremos estos dos arreglos auxiliares para registrar
    # en cuales ensayos el resultado fue 9 y en cuales 10.

    sum_is_9 = num_trials * [False]
    sum_is_10 = num_trials * [False]

    for i in range(num_trials):
        r = roll()
        if r == 9:
            sum_is_9[i] = True
        elif r == 10:
            sum_is_10[i] = True

    # Aqui generamos dos arreglos donde en cada entrada se aproximan los
    # valores de P(sum=9) y P(sum=10)
    p9 = [i / j for i, j in zip(cumsum(sum_is_9), range(1, num_trials))]
    p10 = [i / j for i, j in zip(cumsum(sum_is_10), range(1, num_trials))]

    # Creamos la grafica
    plt.axhline(y=0.125, color='k', linestyle='--', label='P(S=10) real')
    plt.axhline(y=0.1127, color='tab:gray', linestyle='--', label='P(S=9) real')
    plt.plot(p9, color='tab:blue', label='P(S=9) aprox')
    plt.plot(p10, color='tab:orange', label='P(S=10) aprox')
    plt.legend(loc='best')
    plt.show()


# Para la prueba vamos a repetir el experimento 10,000 veces.
num_trials = 10000
die_simulation(num_trials)

