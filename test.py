import os


def CreateDataSet(list):
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


def Test1(test_val):
    CreateDataSet(test_val)
    os.system('python3 project.py < test_values > test')

    file = open('test')
    string = file.read()
    file.close()
    list = string.split('\n')
    if list[-2] == 'Nákup se ruší.':
        print('PASS')
    else:
        print('FAIL')
    os.system('rm test')

def Test2(test_val):
    CreateDataSet(test_val)
    os.system('python3 project.py < test_values > test')
    file = open('test')
    string = file.read()
    file.close()
    list = string.split('\n')
    if 'Pepa' in list[-2] and '4' in list[-2]:
        print('PASS')
    else:
        print('FAIL')
    os.system('rm test')


test1_val = ['Pepa', 2, 'KONEC']
test2_val = ['Pepa', 2, 'BUDGET', 5]

Test1(test1_val)
Test2(test2_val)
