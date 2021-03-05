from horner import horner
import numpy as np


def wartoscFunkcji(argumentX, wzorFunkcji):
    """Zwracanie wartości wybranej funkcji dla argumentu x

            Parametry
            ----------
            arg_x : float
                wartosc argumentu x
            wybor  : String
                wybór funkcji A, B, C lub D
            Dane wyjsciowe
            -------
            wart_fun : float
                wartość funkcji dla argumentu x
    """
    if wzorFunkcji == 1:    # A dla funkcji wielomianowej
        wart_fun = horner([5, 2, -1, 5], argumentX)  # obliczenie wartosci schematem hornera
    elif wzorFunkcji == 2:  # B dla funkcji trygonometrycznej
        wart_fun = 5 * np.cos(argumentX) - 3 * np.sin(argumentX)
    elif wzorFunkcji == 3:  # C dla funkcji wykładniczej
        wart_fun = 2**argumentX-5**argumentX
    elif wzorFunkcji == 4:  # D dla funkcji złożonej
        wart_fun = -3*np.sin(argumentX)+2*argumentX**2-1
    else:
        print("""
Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wartoscFunkcji" """)
