from pobieranie_wartosci import pobieranie_wartosci
from obliczanie import obliczanie
from sys import exit as zamknijProgram
import numpy as np


def zakonczenie(wartosc_konczaca):
    print()
    print(wartosc_konczaca)
    print()
    print()


def rozwiniecie():

    # ustawianie wartosci macierzy A i B jako odpowiednio wartosci wspolczynnikow po lewo i po prawo od znaku rownosci
    # z pobranych rownan
    temp_list = pobieranie_wartosci()
    if not temp_list:
        wstep()
    else:
        A, B, n = temp_list

    print()
    print("Aktualnie rozwiazywany jest uklad o wspolczynnikach:")
    print(A)
    print("i wartosciach po prawej stronie rownosci:")
    temp_B = B.reshape(1, n)
    print(np.rot90(temp_B, k=3))
    print()

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

    # tworzymy macierz N
    N = np.zeros((n, n))
    row, col = np.diag_indices_from(N)
    N[row, col] = (np.diagonal(D))**(-1)

    # tworzymy macierz M
    M = np.matmul(-N, (np.add(L, U)))

    liczba_iteracji = None
    epsilon = None
    print("""Wybierz kryterium zakonczenia algorytmu:
    1. osiagniecie zadanej dokladnosci obliczen
    2. wykonanie okreslonej liczby iteracji """)
    warunekKonca = int(input("""
    Wybór: """))

    if warunekKonca == 1:
        valid = False
        while not valid:
            epsilon = abs(float(input("""
    Podaj epsilon: """)))
            if isinstance(epsilon, float):
                valid = True
    elif warunekKonca == 2:
        valid = False
        while not valid:
            liczba_iteracji = int(input("""
    Podaj liczbe iteracji: """))
            if liczba_iteracji > 0 and isinstance(liczba_iteracji, int):
                valid = True

    x1 = np.zeros(n)
    wartosc_konczaca = obliczanie(N, B, M, x1, liczba_iteracji, epsilon)

    zakonczenie(wartosc_konczaca)


def wstep():
    while(True):
        print("------------------------------------------------------------------")
        print("Program do rozwiazywania ukladow rownan liniowych metoda Jacobiego")
        print("Lukasz Janiszewski, Maciej Kubis")
        print("------------------------------------------------------------------")
        print()
        print("""Wybierz opcje:
1. Rozpocznij program
2. Zakończ program""")
        wyborUzytkownika = int(input("""
    Wybór: """))
        if wyborUzytkownika == 1:
            rozwiniecie()
        elif wyborUzytkownika == 2:
            zamknijProgram()
        else:
            print("""Wybrano nieprawidlowa opcje!""")


wstep()
