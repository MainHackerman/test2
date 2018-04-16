import os


def CreateDataSet(list):
    os.system('touch test_values')
    os.system('rm test_values')
    os.system('touch test_values')
    try:
        file = open('test_values')
        file.close()
    except:
        print('Cannot create file for test values - exiting test.')
        quit()

    for item in list:
        os.system("echo " + str(item) + " >> test_values")

def GetResults():
    os.system('python3 project.py < test_values > test')
    file = open('test')
    string = file.read()
    file.close()
    return string.split('\n')

def Test1(test_val):
    CreateDataSet(test_val)
    if GetResults()[-2] == 'Nákup se ruší.':
        print('PASS')
    else:
        print('FAIL')
    os.system('rm test')
    os.system('rm test_values')

def Test2(test_val):
    CreateDataSet(test_val)
    list = GetResults()
    if test_val[0] in list[-2] and '4' in list[-2]:
        print('PASS')
    else:
        print('FAIL')
    os.system('rm test')
    os.system('rm test_values')

def Test3(test_val):
    CreateDataSet(test_val)
    print(GetResults())

test1_val = ['Pepa', 2, 'KONEC']
test2_val = ['Pepa', 2, 'BUDGET', 5]
test3_val = ['Pepa', 2, 'NAKUP', 'jablko', 'NAKUP', 'jablko', 'KONEC']

Test1(test1_val)
Test2(test2_val)
Test3(test3_val)