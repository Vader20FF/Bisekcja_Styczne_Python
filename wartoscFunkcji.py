from horner import horner
import numpy as np


def wartoscFunkcji(x, numerFunkcji):
    if numerFunkcji == 1:
        return horner([2, 1, 3, 7], x)
    elif numerFunkcji == 2:
        return np.sin(x)-5*np.cos(x)
    elif numerFunkcji == 3:
        return 2**(x-1)-4
    elif numerFunkcji == 4:
        return 3*np.sin(2**x)+2**x
    else:
        print("""
Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wartoscFunkcji" """)
        return None

