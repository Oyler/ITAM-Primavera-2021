# =====================================================================================================================
# Las siguientes funciones nos permite analizar cual es el riesgo de perder dinero en su negocio al cual un afianzador
# se enfrenta al cubrir N polizas cobrando $X por fianza. Dado que es RIESGO, queremos que se mantenga cercano a 0.0
# =====================================================================================================================

import numpy as np
import scipy.stats as stats

def mu_aprox(n, c, p):
    """
    Esta funcion nos permite aproximar la media de la distribucion normal (poco confiable)
    :param n: El numero de polizas.
    :param c: La suma asegurada.
    :param p: La probabilidad de que el cliente pague.
    :return: La media.
    """

    return n * c * p


def sigma_aprox(n, c, p):
    """
    Esta funcion nos permite aproximar la desviacion estandar de la distribucion normal (poco confiable)
    :param n: El numero de polizas.
    :param c: La suma asegurada.
    :param p: La probabilidad de que el cliente pague.
    :return: La desviacion estandar
    """

    return np.sqrt(n * (c ** 2) * p * (1 - p))


def riesgo_afianzador(p_fianza, n, c, p):
    """
    Esta funcion nos permite calcular el riesgo del afianzador al cubrir n polizas a un precio X cada una.
    :param p_fianza: El precio por fianza que cobra el afianzador.
    :param n: El numero de polizas.
    :param c: La suma asegurada.
    :param p: La probabilidad de que el cliente pague.
    :return:
    """
    total = n * p_fianza
    mu = mu_aprox(n, c, p)
    sigma = sigma_aprox(n, c, p)

    q = stats.norm(loc=mu, scale=sigma).cdf(total)

    return 1 - q

if __name__ == '__main__':

    x = []
    x.append(riesgo_afianzador(15307432, 1500, 42500, 0.22))
    x.append(riesgo_afianzador(10204.95, 1500, 42500, 0.22))
    x.append(riesgo_afianzador(11234.98, 1500, 42500, 0.22))
    x.append(riesgo_afianzador(10567.67, 1500, 42500, 0.22))
    print(x)

    p = stats.norm(loc=5, scale=9).cdf(10)
    print(p)