import numpy as np


def pobieranie_wartosci(n):
    macierz_do_A = np.loadtxt('rownania.txt', usecols=range(n), dtype=float)
    macierz_do_B = np.loadtxt('rownania.txt', usecols=range(n, n+1), dtype=float)
    return macierz_do_A, macierz_do_B
