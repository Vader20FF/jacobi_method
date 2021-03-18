from pobieranie_wartosci import pobieranie_wartosci
# from przypisywanie_wartosci import przypisywanie_wartosci
# from obliczanie import obliczanie
from sys import exit as zamknijProgram
import numpy as np

A, B, N, M, L, D, U, x1, x2 = [[]], [], [], [[]], [], [], [], [], []
n = 0


def rozwiniecie():
    global n
    global A, B, L, D, U

    # ustaiwenie wartosci macierzy A i B jako odpowiednio wartosci wspolczynnikow po lewo i po prawo od znaku rownosci
    # z pobranych rownan
    A, B = pobieranie_wartosci(n)

    # ustawianie wartosci macierzy D jako wartosci przekatnej macierzy A
    D = np.zeros((n, n))
    row, col = np.diag_indices_from(D)
    D[row, col] = np.diagonal(A)

    # ustawianie wartosci macierzy L jako wartosci z pod przekatnej macierzy A
    # jako drugi parametr funkcji ustawiamy ktora przekotna chcemy zaczac zerowanie macierzy
    L = np.triu(A, 1)

    # ustawianie wartosci macierzy U jako wartosci z pod przekatnej macierzy A
    # jako drugi parametr funkcji ustawiamy ktora przekotna chcemy zaczac zerowanie macierzy
    U = np.tril(A, -1)



def wstep():
    global n
    print("------------------------------------------------------------------")
    print("Program do rozwiazywania ukladow rownan liniowych metoda Jacobiego")
    print("Lukasz Janiszewski, Maciej Kubis")
    print("------------------------------------------------------------------")
    print()
    print("""
Wybierz opcje:
1. Rozpocznij program
2. Zakończ program""")
    wyborUzytkownika = 0
    while wyborUzytkownika != 1 or wyborUzytkownika != 2:
        wyborUzytkownika = int(input("""
        Wybór: """))
        if wyborUzytkownika == 1:
            while n < 1:
                n = int(input("""
Podaj liczbe rownan w ukladzie: """))
                if n < 1:
                    print("Podaj liczbe rownan w ukladzie wieksza lub rowna 1!")
            rozwiniecie()
        elif wyborUzytkownika == 2:
            zamknijProgram()
        else:
            print("""Wybrano nieprawidlowa opcje!""")



wstep()
