from wartoscFunkcji import wartoscFunkcji
from wzorFunkcji import wzorFunkcji
import sympy as sp


def metodaStycznych(lewaGranica, prawaGranica, epsilon, liczbaIteracji, numerFunkcji):
    # sprawdzenie warunku, że funkcja ma różne znaki na końcach przedziału
    if wartoscFunkcji(lewaGranica, numerFunkcji) * wartoscFunkcji(prawaGranica, numerFunkcji) < 0:
        x = sp.Symbol('x')
        pochodna = sp.diff(wzorFunkcji(numerFunkcji))
        if abs(pochodna.subs(x, lewaGranica)) < abs(pochodna.subs(x, prawaGranica)):
            xi = prawaGranica
        elif abs(pochodna.subs(x, lewaGranica)) > abs(pochodna.subs(x, prawaGranica)):
            xi = lewaGranica
        else:
            xi = (lewaGranica + prawaGranica) / 2
        # Dzialanie na epsilonie
        if liczbaIteracji is None and epsilon is not None:
            liczbaIteracji = 0
            while True:
                wartosc = wartoscFunkcji(xi, numerFunkcji)
                wartoscPochodnej = pochodna.subs(x, xi)
                if (abs(wartosc) < epsilon) and (abs(wartoscPochodnej) > epsilon):
                    print()
                    print(f"Metoda Stycznych (epsilon): Znaleziono rozwiazanie po {liczbaIteracji} iteracjach.")
                    print(f"Metoda Stycznych (epsilon): Osiagnieto dokladnosc na poziomie {epsilon}.")
                    return xi
                xi = xi - float(wartosc / wartoscPochodnej)
                liczbaIteracji += 1
        # Dzialanie na liczbie iteracji
        elif epsilon is None and liczbaIteracji is not None:
            for n in range(liczbaIteracji):
                wartosc = wartoscFunkcji(xi, numerFunkcji)
                wartoscPochodnej = pochodna.subs(x, xi)
                xi = xi - float(wartosc / wartoscPochodnej)
            temp_epsilon = abs(wartoscFunkcji(xi, numerFunkcji))
            print(f"Metoda Stycznych (liczba iteracji): Znaleziono rozwiazanie po {liczbaIteracji} iteracjach.")
            print(f"Metoda Stycznych (liczba iteracji): Osiagnieto dokladnosc na poziomie {temp_epsilon}.")
            return xi
        else:
            print("Nie podano ani epsilona ani liczby iteracji!")
    else:
        print("""
Nie spelniono podstawowego zalozenia metody stycznych!""")
