# Lab 4: Creating a Calculator class


## Exercise 1: Testing a calculator

### Step 1: Writing the code for a calculator
Create a new python file and write a class that acts as a calculator. The methods it should support are 
- add, - subtract, - multiply, -divide.

### Step 2: Write unittest class
Write a testclass that tests the earlier written Calculator class. Run and validate the written tests.


### Extra exercise
Add an option to calculate tupels, lists and sets, the effect should be that each member is calculated with the corresponding member
of the second argument. For example adding (1,2,3) and (3,4,1) results in (4,6,4)

Add testcases to test this functionality as well.

## Exercise 2: More testing on a calculator

### Step 1. Change the calculator
Make some changes to the calculator so that the totals are 
remembered upon each calculation. For now, store the subtotal in a global variable (}normally you would use some sort of persistence).

The calculator should work in a way that each calculation effects on the subtotal, for example:
0
calc.add(1)
1
calc.add(3)
4
calc.subtract(3)
1

etc..

### Step 2. Change the unittests
Change the earlier written unittests so they test the new 
way of working using the subtotals. Notice that the testmethods now potentionally could have an effect on each other because of the shared state.

### Step 3. Add setUp and tearDown
Add setUp and tearDown methods that setup and cleanup after each test has executed. Make sure that each test works on a clean setup. 

### Step 4. Add skipTest to unittests
Use the skipTest to skip all the divide tests when run on a Windows operating system. Validate the tests

### Extra exercise
Try to find a way to make your own decorator that skips all tests when the testmethod does not have an assert 

## Exercise 3: Integrating doctest and unittest

### Step 1: Adding docstrings
Add docstrings to your calculator so they are a helpful aid for others when they want to use your calculator. 

### Step 2: Adding REPL tests
Add tests in your docstrings to test your functions. Make sure to test them using the techniques demonstrated during the course. 

### Step 3: Integrate doctest and unittest
Integrate your doctest and unittest so when the testrunner runs, the doctest run as well. Test your setup

## Exercise 4: Mocking

### Step 1. Adding persistence


