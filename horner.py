def horner(listaWspolczynnikow, argumentX):
    wynik = 0
    for item in reversed(listaWspolczynnikow):
        wynik = wynik * argumentX + item
    return wynik