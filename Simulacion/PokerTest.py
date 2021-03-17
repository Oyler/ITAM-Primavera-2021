from scipy.special import comb
import numpy as np
from collections import Counter
import math


def PokerTest(s, m):
    """
    Function that applies a poker test to a number of n digits with
    m degrees of freedom
    :param s: The number in string format
    :param m: The degrees of freedom
    :return: (The p value, bool flag, str indicating if seq is random)
    """
    X2theoretical = [3.84, 5.99, 7.81, 9.48, 11.07, 12.59, 14.06]
    k = len(s) // m
    l = list(np.arange(0, k))
    s1 = s
    st = ''
    flag = False
    for i in range(0, k):
        while len(s1) > 0:
            l[i] = s1[:m]
            s1 = s1[m:]
            break
    n = l
    for j, i in enumerate(l):
        try:
            n[j] = Counter(i)['1']
        except:
            n[j] = Counter(i)['0']

    n.sort()
    niDict = dict(Counter(n))
    # we create a dummy dictionary with keys
    k = [i for i in range(0, m + 1)]
    dummydict = dict(zip(k, [0] * len(k)))

    def check_existance(i, collection: iter):
        return i in collection

    if dummydict.keys() == niDict.keys():
        print('ok')
    else:
        for i in dummydict.keys():
            if not check_existance(i, niDict.keys()):
                niDict[i] = 0
    b = []

    for i in niDict.keys():
        numerator = math.pow(niDict[i] - comb(m, i) * len(s) / ((2 ** m) * m), 2)
        denominator = comb(m, i) * len(s) / ((2 ** m) * m)
        S = numerator / denominator
        b.append(S)

    X2 = sum(b)
    if X2 < X2theoretical[m - 1]:
        st = 'The sequence is random'
        flag = not flag
    else:
        st = 'The sequence is not random'
    return X2, flag, st


def convert2bin(number):
    n = str(number)
    binary = ""
    for digit in n:
        new_dig = bin(int(digit))[2:]
        binary += new_dig
    return binary

def main():
    no_tests = 10
    numbers = [np.random.randint(100000, 999999) for i in range(no_tests)]
    numbers_new = [convert2bin(n) for n in numbers]
    for n in zip(numbers_new, numbers):
        X2, flag, st = PokerTest(n[0], 5)
        print('number = {0}\np-val = {1:.5f}'
              '\nrandom = {2}\n{3}\n'.format(n[1], X2, flag, st))


if __name__ == '__main__':
    main()
