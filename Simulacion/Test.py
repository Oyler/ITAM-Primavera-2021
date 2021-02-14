import matplotlib.pyplot as plt
from math import gcd, sqrt
import numpy as np

def neumann(seed, bound):
    Z = []
    Z.append(str(seed))
    for k in range(1, bound):
        aux = int(Z[k - 1]) ** 2
        if aux == 0:
            Z.append(str(00))
            break
        else:
            if aux < 10:
                aux = str(aux)
                aux = "000" + aux
            elif 10 <= aux < 100:
                aux = str(aux)
                aux = "00" + aux
            elif 100 <= aux < 1000:
                aux = str(aux)
                aux = "0" + aux
            else:
                aux = str(aux)
            Z.append(aux[1:3])
    return Z

data = neumann(8, 10)
print(data)

