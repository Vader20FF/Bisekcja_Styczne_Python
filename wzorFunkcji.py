from horner import horner
import sympy as sp


def wzorFunkcji(numerFunkcji):
    x = sp.Symbol('x')
    if numerFunkcji == 1:
        return horner([2, 1, 3, 7], x)
    elif numerFunkcji == 2:
        return sp.sin(x)-5*sp.cos(x)
    elif numerFunkcji == 3:
        return 2**(x-1)-4
    elif numerFunkcji == 4:
        return 3*sp.sin(2**x)+2**x
    else:
        print("""
Przekazano nieprawidlowa wartosc numeru wzoru funkcji do metody "wzorFunkcji" """)
        return None
