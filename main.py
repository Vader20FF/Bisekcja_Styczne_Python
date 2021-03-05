from sys import exit as exitProgram
from bisekcja import metodaBisekcji
from styczne import metodaStycznych
from horner import horner
import sympy as sp
from wykres import generowanieWykresu


def menu():
    while True:
        print("""Program do rozwiązywania równań nieliniowych
Metoda bisekcji i stycznych
Lukasz Janiszewski, Maciej Kubis""")
        print("""
Wybierz opcje:
1. Rozpocznij program
2. Zakończ program""")
        userChoice = int(input("""
"""))
        if userChoice == 1:
            dataLoad()
        elif userChoice == 2:
            exitProgram()
        else:
            print("""Wybrano nieprawidlowa opcje!""")


def dataLoad():
    print("""
Wybierz numer funkcji ktorej chcesz uzyc w programie:
    1. FUNKCJA WIELOMIANOWA  5*x^3+2*x^2-x+5
    2. FUNKCJA TRYGONOMETRYCZNA  5*cos(x)-3*sin(x)
    3. FUNKCJA WYKLADNICZA  2^x-5^x
    4. FUNKCJA ZLOZONA  -3*sin(x)+2*x^2-1""")
    selectedFunction = int(input("""
"""))
    argumentX = sp.Symbol('x')
    wzorFunkcji = None
    while selectedFunction not in [1, 2, 3, 4]:
        validNumber = False
        while not validNumber:
            selectedFunction = int(input("""
                Wybierz jeszcze raz numer funkcji: """))
            if selectedFunction in [1, 2, 3, 4]:
                validNumber = True
    if selectedFunction == 1:
        wzorFunkcji = horner([5, 2, -1, 5], argumentX)
    elif selectedFunction == 2:
        wzorFunkcji = 5*sp.cos(argumentX)-3*sp.sin(argumentX)
    elif selectedFunction == 3:
        wzorFunkcji = 2**argumentX-5**argumentX
    elif selectedFunction == 4:
        wzorFunkcji = -3 * sp.sin(argumentX) + 2 * argumentX ** 2 - 1

    leftBorder = int(input("""
Podaj lewy przedział jako liczbe calkowita: """))
    rightBorder = int(input("""
Podaj prawy przedział jako liczbe calkowita: """))

    print("""
Wybierz kryterium zakonczenia algorytmu:
    1. osiagniecie zadanej dokladnosci obliczen
    2. wykonanie okreslonej liczby iteracji """)
    endCondition = int(input("""
"""))

    epsilon = None
    iterations = None
    if endCondition == 1:
        valid = False
        while not valid:
            epsilon = abs(float(input("""
Podaj epsilon: """)))
            if isinstance(epsilon, float):
                valid = True
    elif endCondition == 2:
        valid = False
        while not valid:
            iterations = int(input("""
Podaj liczbe iteracji: """))
            if iterations > 0 and isinstance(iterations, int):
                valid = True

    generowanieWykresu(leftBorder, rightBorder, selectedFunction)

    obliczenia(wzorFunkcji, leftBorder, rightBorder, epsilon, iterations)


def obliczenia(wzorFunkcji, leftBorder, rightBorder, epsilon, iterationNumber):
    wynikBisekcja = metodaBisekcji()
    wynikStyczne = metodaStycznych()

    if not wynikBisekcja:
        print("""
Nie mozna poprawnie zrealizowac metody bisekcji dla wybranej funkcji!""")

    if not wynikStyczne:
        print("""
Nie mozna poprawnie zrealizowac metody stycznych dla wybranej funkcji!""")


##########################################################################
# START
##########################################################################
menu()
