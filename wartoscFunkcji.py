from horner import horner
import numpy as np


def wartoscFunkcji(x, wzorFunkcji):
    if wzorFunkcji == 1:
        return horner([2, 1, 3, 7], x)
    elif wzorFunkcji == 2:
        return 5 * np.cos(x) - 3 * np.sin(x)
    elif wzorFunkcji == 3:
        return 2**x-5**x
    elif wzorFunkcji == 4:
        return -3 * np.sin(x) + 2 * x ** 2 - 1
    else:
        print("""
Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wartoscFunkcji" """)
        return None

