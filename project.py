# rozklad na prvocinitele
cislo = int(input('Zadej cislo: '))
zbytek = cislo
delitel = 2

# prvocisla
dva = 0
tri = 0
pet = 0
sedm = 0
jedenact = 0
trinact = 0
sedmnact = 0
dvacettri = 0

# algoritmus
while zbytek > 1:
    while cislo % delitel != 0:
        delitel = delitel + 1
    if delitel == 2:
        dva = dva + 1
    if delitel == 3:
        tri = tri + 1
    if delitel == 5:
        pet = pet + 1
    if delitel == 7:
        sedm = sedm + 1
    if delitel == 11:
        jedenact = jedenact + 1
    if delitel == 13:
        trinact = trinact + 1
    if delitel == 17:
        sedmnact = sedmnact + 1
    if delitel == 23:
        dvacettri = dvacettri + 1
    print(delitel)
    zbytek = zbytek/delitel

print(dva, tri, pet, sedm, jedenact, trinact, sedmnact, dvacettri)
