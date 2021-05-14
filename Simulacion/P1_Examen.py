import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


def delta_cauchy(x, m):
    theta = np.random.standard_cauchy(m)
    h_1 = np.array([np.pi * np.exp(-0.5 * (x - t) ** 2) for t in theta])
    h_2 = np.array([t * np.pi * np.exp(-0.5 * (x - t) ** 2) for t in theta])
    denom = np.mean(h_1)
    nom = np.mean(h_2)
    delta = nom / denom
    return {'nominador': nom, 'denominador': denom, 'delta': delta}


def delta_normal(x, m):
    theta = np.random.normal(x, 1, m)
    h_1 = np.array([np.sqrt(2 * np.pi) / (1 + t ** 2) for t in theta])
    h_2 = np.array([t * np.sqrt(2 * np.pi) / (1 + t ** 2) for t in theta])
    denom = np.mean(h_1)
    nom = np.mean(h_2)
    delta = nom / denom
    return {'nominador': nom, 'denominador': denom, 'delta': delta}


if __name__ == '__main__':
    n_samples = 5000    # Numero de valores simulados.
    x_vals = [0, 2, 4]  # valores de x.
    delta_C = []    # Lista vacia para las soluciones de los estimadores usando cauchy.
    delta_N = []    # Lista vacia para las soluciones de los estimadores usando normal.
    delta_exact = []    # Lista vacia para las soluciones exactas usando integrate.quad().

    for x in x_vals:
        delta_C.append(delta_cauchy(x, n_samples))  # Agregamos las soluciones a sus respectivas listas
        delta_N.append(delta_normal(x, n_samples))
        f = lambda s: (np.exp(-0.5 * (s - x) ** 2)) / (1 + x ** 2)    # Generamos funciones para integrar.
        g = lambda s: s * f(s)
        nom = integrate.quad(g, -np.inf, np.inf)[0]     # Integramos usando quad
        denom = integrate.quad(f, -np.inf, np.inf)[0]
        temp_dict = {'nominador': nom, 'denominador': denom, 'delta': nom / denom}  # Creamos un diccionario temporal
        delta_exact.append(temp_dict)   # Agregamos las soluciones exactas a su lista.

    # Convertimos las listas de soluciones a diccionarios para mejor acceso.
    delta_C = dict(zip(x_vals, delta_C))
    delta_N = dict(zip(x_vals, delta_N))
    delta_exact = dict(zip(x_vals, delta_exact))

    for x in x_vals:
        print(f"Solucion para x = {x}\n------------------------------------------------------------------------------"
              f"----------------------\n")
        print(f"Cauchy: {delta_C[x]}")
        print(f"Normal: {delta_N[x]}")
        print(f"Exacta: {delta_exact[x]}")
        print("----------------------------------------------------------------------------------------------------")

    nom_varC = []
    denom_varC = []
    nom_varN = []
    denom_varN = []

    for x in x_vals:
        nom_varC.append(delta_C[x]['nominador'])
        nom_varN.append(delta_N[x]['nominador'])
        denom_varC.append(delta_C[x]['denominador'])
        denom_varN.append(delta_N[x]['denominador'])
    print(f"Varianza nominador Cauchy: {np.var(nom_varC)}")
    print(f"Varianza denominador Cauchy: {np.var(denom_varC)}")
    print(f"Varianza nominador Normal: {np.var(nom_varN)}")
    print(f"Varianza denominador Normal: {np.var(denom_varN)}")