import pylab as pb
import numpy as np
from wartoscFunkcji import wartoscFunkcji
from wzorFunkcji import wzorFunkcji


def generowanieWykresu(leftBorder, rightBorder, wynikBisekcja, wynikStyczne, numerFunckji):
    x = np.linspace(leftBorder, rightBorder, 1000)  # generowanie argumentów wykresu funkcji
    pb.plot(x, wartoscFunkcji(x, numerFunckji), label='wykres funkcji f(x)')
    pb.legend(['wykres funkcji f(x)', 'miejsce zerowe z metody bisekcji: {}'.format(wynikBisekcja),
               'miejsce zerowe z metody stycznych: {}'.format(wynikStyczne)],
              loc='upper left')  # tworzy legendę wykresu
    pb.title('f(x)=' + str(wzorFunkcji(numerFunckji)))  # tworzy tytuł wykresu
    pb.grid(True)  # tworzy siatke na wykresie
    pb.xlabel("x")  # opis osi x
    pb.ylabel("y")  # opis osi y
    pb.show()  # pokazuje wykres