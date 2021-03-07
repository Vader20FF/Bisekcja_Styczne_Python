from wartoscFunkcji import wartoscFunkcji
from wzorFunkcji import wzorFunkcji
import sympy as sp


def metodaBisekcji(lewaGranica, prawaGranica, epsilon, liczbaIteracji, numerFunkcji):
    xl = lewaGranica
    xu = prawaGranica
    xm = 0
    # Jesli wartosc iloczynu f(xl) * f(xu) jest mniejsza od 0, istnieje przynajmniej jeden pierwiastek
    if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xu, numerFunkcji) < 0:
        # Dzialanie na epsilonie
        if liczbaIteracji is None and epsilon is not None:
            liczbaIteracji = 0
            x = sp.Symbol('x')
            pochodna = sp.diff(wzorFunkcji(numerFunkcji))
            while True:
                xm = (xl + xu) / 2
                wartoscPochodnej = pochodna.subs(x, xm)
                if abs(wartoscFunkcji(xm, numerFunkcji)) <= epsilon and (abs(wartoscPochodnej) > epsilon):
                    print()
                    print(f"Metoda Bisekcji (epsilon): Znaleziono rozwiazanie po {liczbaIteracji} iteracjach.")
                    print(f"Metoda Bisekcji (epsilon): Osiagnieto dokladnosc na poziomie {epsilon}.")
                    return xm
                elif wartoscFunkcji(xm, numerFunkcji) * wartoscFunkcji(xl, numerFunkcji) < 0:
                    xu = xm
                else:
                    xl = xm
                liczbaIteracji += 1
        # Dzialanie na liczbie iteracji
        elif epsilon is None and liczbaIteracji is not None:
            for iterationNumber in range(liczbaIteracji):
                xm = (xl + xu) / 2
                if wartoscFunkcji(xm, numerFunkcji) == 0:
                    return xm
                if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xm, numerFunkcji) < 0:
                    xu = xm
                else:
                    xl = xm
            temp_epsilon = abs(wartoscFunkcji(xm, numerFunkcji))
            print(f"Metoda Bisekcji (liczba iteracji): Znaleziono rozwiazanie po {liczbaIteracji} iteracjach.")
            print(f"Metoda Bisekcji (liczba iteracji): Osiagnieto dokladnosc na poziomie {temp_epsilon}.")
            return xm
        else:
            print("Nie podano ani epsilona ani liczby iteracji!")
    else:
        print("""
Nie spelniono podstawowego zalozenia metody bisekcji!""")







