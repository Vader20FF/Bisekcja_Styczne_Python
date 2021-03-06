import pylab as pb
import numpy as np
from wartoscFunkcji import wartoscFunkcji
from wzorFunkcji import wzorFunkcji


def generowanieWykresu(leftBorder, rightBorder, functionNumber):
    x = np.linspace(leftBorder, rightBorder, 1000)  # generowanie argumentów wykresu funkcji
    pb.plot(x, wartoscFunkcji(x, functionNumber), label='wykres funkcji f(x)')
    # funkcja pokazujaca wykres (nie ma potrzeby jej używać, ale jak już jest niech zostanie :P)
    # pb.legend(['wykres funkcji f(x)', 'miejsce zerowe z metody bisekcji: {}'.format(rozwiazanie_bisekcja),
    #            'miejsce zerowe z metody Newtona: {}'.format(rozwiazanie_newton)],
    #           loc='upper left')  # tworzy legendę wykresu

    pb.title('f(x)=' + str(wzorFunkcji(functionNumber)))  # tworzy tytuł wykresu
    pb.grid(True)  # tworzy siatke na wykresie
    pb.xlabel("x")  # opis osi x
    pb.ylabel("y")  # opis osi y
    pb.show()  # pokazuje wykres