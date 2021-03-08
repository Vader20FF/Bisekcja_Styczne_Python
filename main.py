from sys import exit as exitProgram
from bisekcja import metodaBisekcji
from styczne import metodaStycznych
from wykres import generowanieWykresu


def menu():
    while True:
        print("""
        
-------------------------------------------------------------------------        
Program do rozwiązywania równań nieliniowych
Metoda bisekcji i stycznych
Lukasz Janiszewski, Maciej Kubis""")
        print("""
Wybierz opcje:
1. Rozpocznij program
2. Zakończ program""")
        wyborUzytkownika = int(input("""
Wybór: """))
        if wyborUzytkownika == 1:
            wczytywanieDanych()
        elif wyborUzytkownika == 2:
            exitProgram()
        else:
            print("""Wybrano nieprawidlowa opcje!""")


def wczytywanieDanych():
    print("""
Wybierz numer funkcji ktorej chcesz uzyc w programie:
    1. FUNKCJA WIELOMIANOWA  2 * x^3 + 1 * x^2 + 3 * x + 7
    2. FUNKCJA TRYGONOMETRYCZNA  sin(x) - 5 * cos(x)
    3. FUNKCJA WYKLADNICZA  2^(x-1) - 4
    4. FUNKCJA ZLOZONA  cos(2 * x^2 + 4)""")
    numerFunkcji = int(input("""
Wybór: """))
    while numerFunkcji not in [1, 2, 3, 4]:
        poprawnaLiczba = False
        while not poprawnaLiczba:
            numerFunkcji = int(input("""
                Wybierz jeszcze raz numer funkcji: """))
            if numerFunkcji in [1, 2, 3, 4]:
                poprawnaLiczba = True

    lewaGranica = float(input("""
Podaj lewa granice przedziału: """))
    prawaGranica = float(input("""Podaj prawa granice przedziału: """))

    print("""
Wybierz kryterium zakonczenia algorytmu:
    1. osiagniecie zadanej dokladnosci obliczen
    2. wykonanie okreslonej liczby iteracji """)
    warunekKonca = int(input("""
Wybór: """))

    epsilon = None
    liczbaIteracji = None
    if warunekKonca == 1:
        valid = False
        while not valid:
            epsilon = abs(float(input("""
Podaj epsilon: """)))
            if isinstance(epsilon, float):
                valid = True
    elif warunekKonca == 2:
        valid = False
        while not valid:
            liczbaIteracji = int(input("""
Podaj liczbe iteracji: """))
            if liczbaIteracji > 0 and isinstance(liczbaIteracji, int):
                valid = True

    obliczenia(lewaGranica, prawaGranica, epsilon, liczbaIteracji, numerFunkcji)


def obliczenia(lewaGranica, prawaGranica, epsilon, liczbaIteracji, numerFunkcji):
    wynikBisekcja = metodaBisekcji(lewaGranica, prawaGranica, epsilon, liczbaIteracji, numerFunkcji)
    wynikStyczne = metodaStycznych(lewaGranica, prawaGranica, epsilon, liczbaIteracji, numerFunkcji)

    if wynikBisekcja is None and wynikStyczne is None:
        print("""
Miejsca zerowe wybranej funkcji nie moga byc wyznaczone powyzszymi metodami!""")
    else:
        if wynikBisekcja is None:
            print("""
Miejsca zerowe wybranej funkcji nie moga byc wyznaczone metoda bisekcji!""")
            print("Metoda Stycznych zwrocila wartosc:", wynikStyczne)
        elif wynikStyczne is None:
            print("""
Miejsca zerowe wybranej funkcji nie moga byc wyznaczone metoda stycznych!""")
            print("Metoda Bisekcji zwrocila wartosc:", wynikBisekcja)
        else:
            print("Metoda Bisekcji zwrocila wartosc:", wynikBisekcja)
            print("Metoda Stycznych zwrocila wartosc:", wynikStyczne)
        prezentacja(lewaGranica, prawaGranica, wynikBisekcja, wynikStyczne, numerFunkcji)


def prezentacja(lewaGranica, prawaGranica, wynikBisekcja, wynikStyczne, numerFunkcji):
    generowanieWykresu(lewaGranica, prawaGranica, wynikBisekcja, wynikStyczne, numerFunkcji)


##########################################################################
# START
##########################################################################
menu()
