import numpy as np
from sys import exit as zamknijProgram


def pobieranie_wartosci():
    print()
    print("""Podaj litere przykladu ktory chcesz rozwiazac:
a, b, c, d, e, f, g, h, i, j""")
    wybor_uzytkownika = str(input("""
    Wybór: """))
    if wybor_uzytkownika not in 'abcdefghij' and wybor_uzytkownika not in 'template':
        print("""Wybrano nieprawidlowa opcje!""")
        while wybor_uzytkownika not in 'abcdefghij' and wybor_uzytkownika not in 'template':
            wybor_uzytkownika = int(input("""
    Wybór: """))
    with open(f"przyklady/{wybor_uzytkownika}.txt", mode="r") as plik:
        n = sum(1 for linia in plik)
    macierz_do_A = np.loadtxt(f"przyklady/{wybor_uzytkownika}.txt", usecols=range(n), dtype=float)
    # sprawdzenie warunku zbieznosci macierzy A
    suma_wartosci_przekatnej = np.sum(np.absolute(np.diagonal(macierz_do_A)))
    suma_wartosci_z_nad_przekatnej = np.sum(np.absolute(np.triu(macierz_do_A, 1)))
    suma_wartosci_z_pod_przekatnej = np.sum(np.absolute(np.tril(macierz_do_A, -1)))
    if suma_wartosci_przekatnej <= suma_wartosci_z_nad_przekatnej + suma_wartosci_z_pod_przekatnej:
        print()
        print("Nie zostal spelniony warunek zbieznosci metody Jacobiego dla wybranej macierzy!!!")
        zamknijProgram()
    macierz_do_B = np.loadtxt(f"przyklady/{wybor_uzytkownika}.txt", usecols=range(n, n+1), dtype=float)
    return [macierz_do_A, macierz_do_B, n]
