import numpy as np


def obliczanie(x2, N, B, M, x1, liczba_iteracji, epsilon):
    if liczba_iteracji is None and epsilon is not None:
        liczba_iteracji = 0
        while True:
            pass
    elif epsilon is None and liczba_iteracji is not None:
        for numer_iteracji in range(liczba_iteracji):
            x2 = np.matmul(N, B)
            x2 = np.add(x2, np.matmul(M, x1))
    else:
        print("Nie podano ani epsilona ani liczby iteracji!")
