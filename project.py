jmeno = input()
budget = int(input())

banan = 2
jablko = 1
hruska = 1

cena = banan + jablko + hruska

while cena > budget:
    print('Prekrocil jsi budget, jak pokracovat?')
    print('Zadej KONEC pro skonceni, BUDGET pro zmenu budgetu, NAKUP pro smazani polozky z nakupniho listu')
    vyber = input()
    if vyber == 'KONEC':
        quit()
    elif vyber == 'BUDGET':
        budget = int(input('Zadej novou castku'))
    elif vyber == 'NAKUP':
        print('Jakou položku chceš odebrat?')
        vyber = input()
        if vyber == 'banan':
            cena = cena - banan
        elif vyber == 'jablko':
            cena = cena - jablko
        elif vyber == 'hruska':
            cena = cena - hruska
