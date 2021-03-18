import numpy as np


def obliczanie(N, B, M, x1, liczba_iteracji, epsilon):
    if liczba_iteracji is None and epsilon is not None:
        x2 = np.matmul(N, B)
        x2 = np.add(x2, np.matmul(M, x1))
        while epsilon < any(np.abs(np.subtract(x1, x2))):
            x1 = x2
            x2 = np.matmul(N, B)
            x2 = np.add(x2, np.matmul(M, x1))
        return f"Znalezione rozwiazania ukladu przy zadanej dokladnosci: {epsilon} \n {x1}"
    elif epsilon is None and liczba_iteracji is not None:
        for numer_iteracji in range(liczba_iteracji):
            x2 = np.matmul(N, B)
            x2 = np.add(x2, np.matmul(M, x1))
            x1 = x2
        return f"Znalezione rozwiazania ukladu przy zadanej liczbie iteracji: {liczba_iteracji} \n {x1}"
    else:
        print("Nie podano ani epsilona ani liczby iteracji!")
