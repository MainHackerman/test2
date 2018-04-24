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
    if test_val[0] in list[-2]:
        os.system('rlPass "Name in output"')
    else:
        os.system('rlFail "Name not in output"')
    if '5' in list[-2]:
        os.system('rlPass "Price ok"')
    else:
        os.system('rlFail "Wrong price calculation"')
    ClearEnv()

def Test1(test_val):
    CreateDataSet(test_val)
    if GetResults()[-2] == 'Nákup se ruší.':
        os.system('rlPass "Can cancel shopping"')
    else:
        os.system('rlFail "Cant cancel shopping"')
    ClearEnv()

def Test2(test_val):
    CreateDataSet(test_val)
    list = GetResults()
    if test_val[0] in list[-2]:
        os.system('rlPass "Can change the budget"')
    else:
        os.system('rlFail "Cant change the budget"')
    if '5' in list[-2]:
        os.system('rlPass "Price ok"')
    else:
        os.system('rlFail "Wrong price calculation"')
    ClearEnv()

def Test3(test_val):
    for item in fruit:
        test_val[-1] = item
        CreateDataSet(test_val)
        list = GetResults()
        if item == 'banan':
            if test_val[0] in list[-2] and '2' in list[-2]:
                os.system('rlPass "Can remove' + str(item) + 'from shopping list"')
                #print('PASS - Can remove', item, 'from shopping list.')
            else:
                os.system('rlFail "Cant remove' + str(item) + 'from shopping list"')
                #print('FAIL - Cant remove', item, 'from shopping list.')
        else:
            if test_val[0] in list[-2] and '4' in list[-2]:
                os.system('rlPass "Can remove' + str(item) + 'from shopping list"')
                #print('PASS - Can remove', item, 'from shopping list.')
            else:
                os.system('rlFail "Cant remove' + str(item) + 'from shopping list"')
                #print('FAIL - Cant remove', item, 'from shopping list.')
        ClearEnv()

def Test4(test_val):
    for item in fruit:
        test_val[3] = item
        test_val[-2] = item
        CreateDataSet(test_val)
        list = GetResults()
        if 'Tato položka není v seznamu.' not in list:
            os.system('rlFail "Can remove' + str(item) + 'from shopping list twice"')
            #print('FAIL - Can remove item', item, 'from shopping list twice.')
        else:
            os.system('rlPass "Cant remove' + str(item) + 'from shopping list twice"')
            #print('PASS - Cannot remove', item, 'from shopping list twice.')
        ClearEnv()

def Test5(test_val):
    CreateDataSet(test_val)
    list = GetResults()
    if list[-2] == 'Nákup se ruší':
        os.system('rlPass "Shopping ends when everything is removed form the list"')
    else:
        os.system('rlFail "Shopping does not end when everything is removed form the list"')
    ClearEnv()

test0_val = ['Pepa', 5]
test1_val = ['Pepa', 2, 'KONEC']
test2_val = ['Pepa', 2, 'BUDGET', 5]
test3_val = ['Pepa', 4, 'NAKUP', 'ovoce']
test4_val = ['Pepa', 1, 'NAKUP', 'ovoce', 'NAKUP', 'ovoce', 'KONEC']
test5_val = ['Pepa', 0, 'NAKUP', 'banan', 'NAKUP', 'jablko', 'NAKUP', 'hruska']

os.system('rlJournalStart')
Test0(test0_val)
Test1(test1_val)
Test2(test2_val)
Test3(test3_val)
Test4(test4_val)
Test5(test5_val)
os.system('rlJournalEnd')