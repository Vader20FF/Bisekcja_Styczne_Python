import pylab as pb
import numpy as np
from wartoscFunkcji import wartoscFunkcji


def generowanieWykresu(leftBorder, rightBorder, functionNumber):
    x = np.linspace(leftBorder, rightBorder, 1000)  # generowanie argumentów wykresu funkcji
    pb.plot(x, wartoscFunkcji(x, functionNumber), label='wykres funkcji f(x)')