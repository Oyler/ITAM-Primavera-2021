# ====================================================================================================================
#                                             PARCIAL 2: PREGUNTA 2.
#
#       Autor: Ismael Ancona Tellez.                     CU: 171911                              Fecha: 18/04/2021
# --------------------------------------------------------------------------------------------------------------------
# Para un proyecto de construcción en el cual se cobra una penalización de \$1,000 USD por cada día (y prorata por
# fracción de día) que la duración del proyecto excede $K$ días. Se pide calcular el costo esperado del retraso.
# =====================================================================================================================

import numpy as np

# Funciones para generar medias y varianzas (se utilizan en mone_carlo() y condicionamiento_RB()).
def gen_parameters(size):
    """
    Genera medias usando mu ~ N(100, 16) y varianzas usando sigma^2 ~ exp(1/4) ambas de tamaño "size".
    :param size: El tamaño de las muestras.
    :return:
    """
    '''
    # Inicializamos una uniforme u~U(0,1) y una normal estandar z~N(0,1)
    u = np.random.uniform(0, 1, size)
    z = np.random.standard_normal(size)
    # Creamos la varianza y media de forma aleatoria.
    sigma_sqr = -4 * np.log(u)
    mu = 100 + 4 * z
    '''
    # Correr usando esto en lugar de lo anterior para ver algo interesante.
    sigma_sqr = np.random.exponential(1/4, size)
    mu = np.random.normal(100, 4, size)

    return sigma_sqr, mu

# Metodo de monte carlo crudo.
def monte_carlo(num_sim, num_dias, penalizacion):
    """
    Esta funcion utiliza el método de Monte Carlo crudo  para simular  la variable aleatoria que representa el número
    de días que dura el proyecto y calcular el costo de penalizacion esperado.

    :param num_sim: Numero de simulaciones.
    :param num_dias: Numero de dias para el proyecto.
    :param penalizacion: Monto a pagar por el atrazo.
    :return: (Costo esperado, varianza).
    """
    # Generamos nuestras medias y sigmas cuadradas.
    sigma_sqr, mu = gen_parameters(num_sim)

    # Inicializamos un vector para el numero de dias.
    x = [np.random.normal(loc=mu[i], scale=np.sqrt(sigma_sqr[i]), size=1) for i in range(num_sim)]
    x = np.array(x)

    # Calculamos el costo que se pagara por atraso en cada simulacion.
    costos = penalizacion * np.maximum(0, x - num_dias)

    # Calculamos el costo esperado como la media del arreglo de costos y la varianza como var(costo)/n
    costo_esperado = np.mean(costos)
    varianza = np.var(costos) / num_sim

    return costo_esperado, varianza

# Metodo de condicionamiento.
def condicionamiento_RB(num_sim, num_dias, penalizacion):
    sigma_sqr, mu = gen_parameters(num_sim)
    costos = penalizacion * np.maximum(0, mu - num_dias)
    costo_esperado = np.mean(costos)
    varianza = np.var(costos) / num_sim

    return costo_esperado, varianza

if __name__ == '__main__':
    np.random.seed(171911)
    c, v = monte_carlo(int(2**20), 100, 10000)
    c_other, v_other = condicionamiento_RB(int(2**20), 100, 10000)
    print("Costo: {0:.2f}, varianza: {1:.2f}".format(c, v))
    print("Costo: {0:.2f}, varianza: {1:.2f}".format(c_other, v_other))
