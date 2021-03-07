import matplotlib.pyplot as plt
import numpy as np
from wartoscFunkcji import wartoscFunkcji
from wzorFunkcji import wzorFunkcji


def generowanieWykresu(lewaGranica, prawaGranica, wynikBisekcja, wynikStyczne, numerFunkcji):
    x = np.linspace(lewaGranica, prawaGranica, 1000)  # generowanie argumentów wykresu funkcji
    plt.plot(x, wartoscFunkcji(x, numerFunkcji), label='wykres funkcji f(x)')
    plt.plot(wynikBisekcja, wartoscFunkcji(wynikBisekcja, numerFunkcji), 'x')
    plt.plot(wynikStyczne, wartoscFunkcji(wynikStyczne, numerFunkcji), '+')
    plt.legend(['wykres funkcji f(x)', f'Miejsce zerowe metody Bisekcji: {round(wynikBisekcja, 6)}',
                f'Miejsce zerowe metody Stycznych: {round(wynikStyczne, 6)}'],
               loc='best')
    plt.title('f(x)=' + str(wzorFunkcji(numerFunkcji)))
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
