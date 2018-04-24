# test2

## Components

### project.py
 - file with student's solution of the task - the one that's being tested

### test.py
 - test script
 - can be upgraded to support students using float for prices
 - maj ingliš very gut
 
 ## Test functions
 
 ### CreateDataSet(list)
 - creates file with test values (one pre row) from **list**
 - The touch, rm, touch cycle is there for situation in which the *test_values* file is not present, so the *rm* command does not produce any error.
 
 ### GetResults()
 - takes test values and pass them into project script
 - optput of the project script is then saved into file name *test*
 - the test file is then read, each row gets separated and it's returned as a list (one item of a list - one row of output)
 - this is differnt from same named function from test script from first student project
 
 ### ClearEnv()
 - deletes *test* file and *test_values* file
 
 ### Test0()
  - Tests basic funkcionality - passes in budget value that is enaught to pay the price
  
 ### Test1()
  - Passes low budget and then select to exit the program
  
 ### Test2()
  - Passes low budget then raises the budget 
  
 ### Test3()
  - Passes low budget then tries to remove one item from fruit list. This is done for all item in fruit list repeating whole proces of creation dataset and results.
 
 ### Test4()
  -  Passes low budget then tries to remove one item from fruit list twice. This is done for all item in fruit list repeating whole proces of creation dataset and results.
 
 ### Test5():
  - Removes all items from shopping list, checks if correct message is printed.