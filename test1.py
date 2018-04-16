file = open('test1')
string = file.read()
list = string.split('\n')
if list[-2] == 'Nákup se ruší.':
    print('PASS')
else:
    print('FAIL')