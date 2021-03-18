import numpy as np
from sys import exit as zamknijProgram


def pobieranie_wartosci(n):
    macierz_do_A = np.loadtxt('rownania.txt', usecols=range(n), dtype=float)
    # sprawdzenie warunku zbieznosci macierzy A
    suma_wartosci_przekatnej = np.sum(np.absolute(np.diagonal(macierz_do_A)))
    suma_wartosci_z_nad_przekatnej = np.sum(np.absolute(np.triu(macierz_do_A, 1)))
    suma_wartosci_z_pod_przekatnej = np.sum(np.absolute(np.tril(macierz_do_A, -1)))
    if suma_wartosci_przekatnej <= suma_wartosci_z_pod_przekatnej + suma_wartosci_z_nad_przekatnej:
        print("Nie zostal spelniony warunek zbieznosci metody Jacobiego!!!")
    macierz_do_B = np.loadtxt('rownania.txt', usecols=range(n, n+1), dtype=float)
    return macierz_do_A, macierz_do_B
