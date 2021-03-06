from horner import horner
import sympy as sp


def wzorFunkcji(numerFunkcji):
    x = sp.Symbol('x')
    if numerFunkcji == 1:
        return horner([2, 1, 3, 7], x)
    elif numerFunkcji == 2:
        return 5*sp.cos(x)-3*sp.sin(x)
    elif numerFunkcji == 3:
        return 2**x-5**x
    elif numerFunkcji == 4:
        return -3*sp.sin(x)+2*x**2-1
    else:
        print("""
Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wzorFunkcji" """)
        return None
