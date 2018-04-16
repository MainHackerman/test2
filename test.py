import os

fruit = ['jablko', 'hruska', 'banan']

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


def ClearEnv():
    os.system('rm test')
    os.system('rm test_values')

def Test0(test_val):
    CreateDataSet(test_val)
    list = GetResults()
    if test_val[0] in list[-2] and '5' in list[-2]:
        print('PASS - Can buy.')
    else:
        print('FAIL - Cannot buy.')
    ClearEnv()

def Test1(test_val):
    CreateDataSet(test_val)
    if GetResults()[-2] == 'Nákup se ruší.':
        print('PASS - Can cancel shopping.')
    else:
        print('FAIL - Cannot cancel shopping.')
    ClearEnv()


def Test2(test_val):
    CreateDataSet(test_val)
    list = GetResults()
    if test_val[0] in list[-2] and '5' in list[-2]:
        print('PASS - Can change the budget.')
    else:
        print('FAIL - Cannot change the budget.')
    ClearEnv()

def Test3(test_val):
    for item in fruit:
        test_val[-1] = item
        CreateDataSet(test_val)
        list = GetResults()
        if item == 'banan':
            if test_val[0] in list[-2] and '2' in list[-2]:
                print('PASS - Can remove', item, 'from shopping list.')
            else:
                print('FAIL - Cant remove', item, 'from shopping list.')
        else:
            if test_val[0] in list[-2] and '4' in list[-2]:
                print('PASS - Can remove', item, 'from shopping list.')
            else:
                print('FAIL - Cant remove', item, 'from shopping list.')
        ClearEnv()

def Test4(test_val):
    for item in fruit:
        test_val[3] = item
        test_val[-2] = item
        CreateDataSet(test_val)
        list = GetResults()
        if 'Tato položka není v seznamu.' not in list:
            print('FAIL - Can remove item', item, 'from shopping list twice.')
        else:
            print('PASS - Cannot remove', item, 'from shopping list twice.')
        ClearEnv()

test0_val = ['Pepa', 5]
test1_val = ['Pepa', 2, 'KONEC']
test2_val = ['Pepa', 2, 'BUDGET', 5]
test3_val = ['Pepa', 4, 'NAKUP', 'ovoce']
test4_val = ['Pepa', 1, 'NAKUP', 'ovoce', 'NAKUP', 'ovoce', 'KONEC']

Test1(test1_val)
Test2(test2_val)
Test3(test3_val)
Test4(test4_val)
