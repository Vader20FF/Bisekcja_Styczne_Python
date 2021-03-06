from wartoscFunkcji import wartoscFunkcji
from wzorFunkcji import wzorFunkcji
import sympy as sp


def metodaBisekcji(leftBorder, rightBorder, epsilon, iterations, numerFunkcji):
    xl = leftBorder
    xu = rightBorder
    xm = 0
    print(leftBorder, rightBorder, epsilon, iterations, numerFunkcji)
    # Jesli wartosc iloczynu f(xl) * f(xu) jest mniejsze od 0, istnieje przynajmniej jeden pierwiastek
    if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xu, numerFunkcji) < 0:
        # Dzialanie na epsilonie
        if iterations is None and epsilon is not None:
            x = sp.Symbol('x')
            df = sp.diff(wzorFunkcji(numerFunkcji))  # obliczenie pochodnej funkcji
            liczbaIteracji = 0
            while True:
                xm = (xl + xu) / 2
                dfxn = df.subs(x, xm)       # obliczenie wartosci pochodnej dla argumentu
                if abs(wartoscFunkcji(xm, numerFunkcji)) <= epsilon and (abs(dfxn) > epsilon):
                    # jeżeli znaleźliśmy miejsce zerowe mniejsze bądź równe przybliżeniu zera
                    # oraz funkcja w tym miejscu nie dąży do stałej wartości
                    print(f"Metoda Bisekcji (epsilon): Znaleziono rozwiazanie po {liczbaIteracji} iteracjach.")
                    print(f"Metoda Bisekcji (epsilon): Osiagnieto dokladnosc na poziomie {epsilon}.")
                    return xm
                elif wartoscFunkcji(xm, numerFunkcji) * wartoscFunkcji(xl, numerFunkcji) < 0:
                    xu = xm
                else:
                    xl = xm
                liczbaIteracji += 1

        elif epsilon is None and iterations is not None:
            for iterationNumber in range(iterations):
                xm = (xl + xu) / 2
                if wartoscFunkcji(xm, numerFunkcji) == 0:
                    return xm
                if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xm, numerFunkcji) < 0:
                    xu = xm
                else:
                    xl = xm
            temp_epsilon = abs(wartoscFunkcji(xm, numerFunkcji))
            print(f"Metoda Bisekcji (liczba iteracji): Znaleziono rozwiazanie po {iterations} iteracjach.")
            print(f"Metoda Bisekcji (liczba iteracji): Osiagnieto dokladnosc na poziomie {temp_epsilon}.")
            return xm
        else:
            print("Nie podano ani epsilona ani liczby iteracji!")
    else:
        print("""
Nie spelniono podstawowego zalozenia metody bisekcji!""")







