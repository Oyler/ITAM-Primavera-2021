import numpy as np

def coin_toss(num_tosses):
    tosses = []
    freq_eagle = 0
    freq_sol = 0
    for _ in range(num_tosses):
        x = np.random.uniform(0, 1)
        if x <= 0.5:
            tosses.append((x, 'Aguila'))
            freq_eagle += 1
        else:
            tosses.append((x, 'Sol'))
            freq_sol += 1
    return tosses, (freq_eagle / num_tosses, freq_sol / num_tosses)


if __name__ == '__main__':

    num_tosses = 10000
    test, averages = coin_toss(num_tosses)

    print(f"\nNumero de observaciones: {num_tosses}\n")
    for sample in test:
        print("x: {0:.4f} | result: {1}".format(sample[0], sample[1]))

    print(f"\nFrequencia Aguila: {averages[0] * 100}% | Frequencia Sol: {averages[1] * 100}%\n")

