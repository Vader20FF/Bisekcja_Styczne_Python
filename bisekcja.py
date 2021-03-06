from wartoscFunkcji import wartoscFunkcji


def metodaBisekcji(leftBorder, rightBorder, epsilon, iterations, numerFunkcji):
    xl = leftBorder
    xu = rightBorder
    xm = 0
    print(leftBorder, rightBorder, epsilon, iterations, numerFunkcji)
    # Jesli wartosc iloczynu f(xl) * f(xu) jest mniejsze od 0, istnieje przynajmniej jeden pierwiastek
    print("Podstawowe zalozenie:", wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xu, numerFunkcji))
    if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xu, numerFunkcji) < 0:
        # Dzialanie na epsilonie
        if iterations is None and epsilon is not None:
            print("Wykonuje metoda epsilon")
            xm = (xl + xu) / 2
            if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xm, numerFunkcji) > 0:
                xl = xm
                xm = (xl + xu) / 2
                if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xm, numerFunkcji) < 0:
                    xu = xm
                    while abs(xu - xl / xu) * 100 > epsilon:
                        xm = (xl + xu) / 2
                        if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xm, numerFunkcji) < 0:
                            xu = xm
        elif epsilon is None and iterations is not None:
            print("Wykonuje metoda iteracji")
            for iterationNumber in range(iterations):
                xm = (xl + xu) / 2
                if wartoscFunkcji(xm, numerFunkcji) == 0:
                    return xm
                if wartoscFunkcji(xl, numerFunkcji) * wartoscFunkcji(xm, numerFunkcji) < 0:
                    xu = xm
                else:
                    xl = xm
            print(f"Znaleziono rozwiazanie po {iterations} iteracjach.")
            return xm
        else:
            print("Nie podano ani epsilona ani liczby iteracji!")
    else:
        print("""
Nie spelniono podstawowego zalozenia metody bisekcji!""")







