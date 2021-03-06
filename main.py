from sys import exit as exitProgram
from bisekcja import metodaBisekcji
from styczne import metodaStycznych
from wykres import generowanieWykresu
from wzorFunkcji import wzorFunkcji


def menu():
    while True:
        print("""
        
Program do rozwiązywania równań nieliniowych
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
    1. FUNKCJA WIELOMIANOWA  2 * x^3 + 1 * x^2 + 3 * x + 7
    2. FUNKCJA TRYGONOMETRYCZNA  5 * cos(x) - 3 * sin(x)
    3. FUNKCJA WYKLADNICZA  2^x - 5^x
    4. FUNKCJA ZLOZONA  -3 * sin(x) + 2 * x^2 - 1""")
    selectedFunction = int(input("""
"""))
    while selectedFunction not in [1, 2, 3, 4]:
        validNumber = False
        while not validNumber:
            selectedFunction = int(input("""
                Wybierz jeszcze raz numer funkcji: """))
            if selectedFunction in [1, 2, 3, 4]:
                validNumber = True
    wzorFunkcjiZmienna = wzorFunkcji(selectedFunction)

    leftBorder = float(input("""
Podaj lewa granice przedziału: """))
    rightBorder = float(input("""Podaj prawa granice przedziału: """))

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

    obliczenia(leftBorder, rightBorder, epsilon, iterations, selectedFunction)


def obliczenia(leftBorder, rightBorder, epsilon, iterationNumber, numerFunkcji):
    wynikBisekcja = metodaBisekcji(leftBorder, rightBorder, epsilon, iterationNumber, numerFunkcji)
    print("Metoda bisekcji zwrocila wartosc:", wynikBisekcja)

    wynikStyczne = metodaStycznych()
    print("Metoda stycznych zwrocila wartosc:", wynikStyczne)

    prezentacja(leftBorder, rightBorder, wynikBisekcja, wynikStyczne, numerFunkcji)


def prezentacja(leftBorder, rightBorder, wynikBisekcja, wynikStyczne, numerFunkcji):
    generowanieWykresu(leftBorder, rightBorder, wynikBisekcja, wynikStyczne, numerFunkcji)


##########################################################################
# START
##########################################################################
menu()
