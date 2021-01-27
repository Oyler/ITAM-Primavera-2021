from numpy import *


def utilidad(riqueza, ganancias, costos, func):
    w = riqueza + ganancias - costos
    if func == 0:
        return w
    elif func == 1:
        return sqrt(w)
    elif func == 2:
        return log(w)
    else:
        return w ** 2


riqueza = 500
ganancia_renta_paga = 600
costo_renta = 360 + 10

ut_no_rentar = utilidad(riqueza, 0, 0, 2)
ut_rentar = 0.75 * utilidad(riqueza, ganancia_renta_paga, costo_renta, 2) + 0.25 * utilidad(riqueza, ganancia_renta_paga, costo_renta, 2)
print(f'Utilidad de no rentar: {ut_no_rentar}')
print(f'Utilidad de rentar: {ut_rentar}')









conveniencia = 'conviene' if ut_rentar >= ut_no_rentar else 'no conviene'
print(conveniencia)