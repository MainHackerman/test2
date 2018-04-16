jmeno = input()
budget = int(input())

banan = 3
bananB = True
jablko = 1
jablkoB = True
hruska = 1
hruskaB = True

cena = banan + jablko + hruska

while cena > budget:
    print('Prekrocil jsi budget, jak pokracovat?')
    print('Zadej KONEC pro skonceni, BUDGET pro zmenu budgetu, NAKUP pro smazani polozky z nakupniho listu')
    vyber = input()
    if vyber == 'KONEC':
        break
    elif vyber == 'BUDGET':
        budget = int(input('Zadej novou castku'))
    elif vyber == 'NAKUP':
        print('Jakou položku chceš odebrat?')
        vyber = input()
        if vyber == 'banan' and bananB == True:
            cena = cena - banan
            bananB = False
        elif vyber == 'jablko' and jablkoB == True:
            cena = cena - jablko
            jablkoB = False
        elif vyber == 'hruska' and hruskaB == True:
            cena = cena - hruska
            hruskaB = False
        else:
            print('Tato položka není v seznamu.')

if vyber == 'KONEC' or cena <= 0:
    print('Nákup se ruší.')
else:
    print('Na nákup půjde', jmeno, 'a zaplatí',cena)