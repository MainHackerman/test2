file = open('test2')
string = file.read()
list = string.split('\n')
if 'Pepa' in list[-2] and '4' in list[-2]:
    print('PASS')
else:
    print('FAIL')