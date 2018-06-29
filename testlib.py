import os

def CreateDataSet(list):
    test_file = open('test_values','w')
    for item in list:
        test_file.write(item)
    test_file.close()

def GetResults():
    os.system('python3 project.py < test_values > test')
    file = open('test')
    string = file.read()
    file.close()
    return string.split('\n')

def ClearEnv():
    os.system('rm test')
    os.system('rm test_values')

