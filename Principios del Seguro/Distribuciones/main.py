from RiskAnalysis import riesgo_afianzador

def main():
    c = 36000
    p = 0.25
    riesgo = [0, 0, 0, 0, 0, 0]
    riesgo[0] = riesgo_afianzador(1000, 1000, c, p)
    riesgo[1] = riesgo_afianzador(15000, 1000, c, p)
    riesgo[2] = riesgo_afianzador(15000, 10, c, p)
    riesgo[3] = riesgo_afianzador(100000, 5, c, p)
    riesgo[4] = riesgo_afianzador(1000, 1000000, c, p)
    riesgo[5] = riesgo_afianzador(10000, 1000, c, p)

    for i in range(6):
        print("Ej {0}: El riesgo del afianzador es {1:.3f}".format(i + 1, riesgo[i]))


if __name__ == '__main__':
    main()