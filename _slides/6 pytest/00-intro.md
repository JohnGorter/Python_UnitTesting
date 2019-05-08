# PyTest

---
### Agenda

---
### PyTest references

Mozilla and Dropbox

---
### Introduction

Pytest is a python based testing framework, which is used to write and execute test codes. 

---
### Advantages of Pytest
The advantages are as follows
- Pytest can run multiple tests in parallel, which reduces the execution time of the test suite
- Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
- Pytest allows us to skip a subset of the tests during execution.
- Pytest allows us to run a subset of the entire test suite.
- Pytest is free and open source.
- Because of its simple syntax, pytest is very easy to start with.

---
### Installation

To start the installation, execute the following command 
```
pip3 install pytest 
```

Confirm the installation using the following command to display the help section of pytest.
```
pytest -h
pytest --version
```

---
### Running tests
Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py in the current directory and subdirectories

Pytest automatically identifies those files as test files. We can make pytest run other filenames by explicitly mentioning them

---
### A basic test
Here an example of a basic test
```
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11
```
Run the test using the following command 
```
pytest
```

---
### A basic example 

The above command will generate the following output 
```
test_square.py .F
============================================== FAILURES 
==============================================
______________________________________________ testsquare 
_____________________________________________
   def testsquare():
   num=7
>  assert 7*7 == 40
E  assert (7 * 7) == 40
test_square.py:9: AssertionError
================================= 1 failed, 1 passed in 0.06 seconds 
=================================
```

---
### A basic example 
See the first line of the result. It displays the file name and the results. F represents a test failure and dot(.) represents a test success.

Below that, we can see the details of the failed tests. It will show at which statement the test has failed. In our example, 7*7 is compared for equality against 49, which is wrong. In the end, we can see test execution summary, 1 failed and 1 passed.

The function tescompare is not executed because pytest will not consider it as a test since its name is not of the format test*.

---
### A basic example 
Lets be more verbose
```
pytest -v
```
-v increases the verbosity.
```
test_square.py::test_sqrt PASSED
test_square.py::testsquare FAILED
============================================== FAILURES 
==============================================
_____________________________________________ testsquare 
_____________________________________________
   def testsquare():
   num = 7
>  assert 7*7 == 40
E  assert (7 * 7) == 40
test_square.py:9: AssertionError
================================= 1 failed, 1 passed in 0.04 seconds 
=================================
```

Now the result is more explanatory about the test that failed and the test that passed.

---
### Single test file and multiple test files

Adding more files in the same directory are automatically picked up
when you use

```
pytest 
```

---
### Test Suites
In a real scenario, we will have multiple test files and each file will have a number of tests. Tests will cover various modules and functionalities. 

Suppose, we want to run only a specific set of tests; how do we go about it?

---
### Test Suites (2)
Pytest provides two ways to run the subset of the test suite.

- select tests to run based on substring matching of test names
- select tests groups to run based on the markers applied

---
### Test Suites (3)
To execute the tests containing a string in its name we can use the following syntax

```
pytest -k <substring> -v
```

-k 'substring' represents the substring to search for in the test names.

Example
```
pytest -k great -v
```
This will execute all the test names having the word ‘great’ in its name 

Note − The name of the test function should still start with ‘test’

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
running specific tests
pytest -k "john_more"

---
### Markers

Pytest allows us to use markers on test functions
Markers are used to set various features/attributes to test functions
Pytest provides many inbuilt markers 
- xfail
- skip 
- parametrize

Apart from that, users can create their own marker names
Markers are applied on the tests using the syntax given below 
```
@pytest.mark.<markername>
```

---
### Markers (2)
To use markers, import pytest module in the test file
We can define our own marker names to the tests and run the tests having those marker names

To run the marked tests, we can use the following syntax −
```
pytest -m <markername> -v
```
-m 'markername' represents the marker name of the tests to be executed.

---
### Markers (3)

Example 3 markers – great, square, others
```
import pytest
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200

# other file
import pytest
import math

@pytest.mark.square
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
   num = 7
   assert 7*7 == 40

@pytest.mark.others
   def test_equality():
   assert 10 == 11
```

Now to run the tests marked as others, run 
```
pytest -m others -v
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
markers


---
### Fixtures
Fixtures are functions, which will run before each test function to which it is applied

Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data

---
### Fixtures (2)

A function is marked as a fixture by 
```
@pytest.fixture
```

A test function can use a fixture by mentioning the fixture name as an input parameter.

Example
```
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
```

---
### Fixtures (2)
Pytest, while the test is getting executed, will see the fixture name as input parameter.

It  executes the fixture function and the returned value is stored to the input parameter, 
which can be used by the test

Execute the test 
```
pytest -k divisible -v
```

---
### Fixtures (2)
The above command will generate the following result
```
test_div_by_3_6.py::test_divisible_by_3 PASSED
test_div_by_3_6.py::test_divisible_by_6 FAILED
============================================== FAILURES
==============================================
________________________________________ test_divisible_by_6
_________________________________________
input_value = 39
   def test_divisible_by_6(input_value):
>  assert input_value % 6 == 0
E  assert (39 % 6) == 0
test_div_by_3_6.py:12: AssertionError
========================== 1 failed, 1 passed, 6 deselected in 0.07 seconds
==========================
```

---
### Fixtures (3)

However,  there are limitations:
- a fixture function defined inside atest file has a scope within the test file only
   - you cannot use that fixture in another test file
 
To make a fixture available to multiple test files
- define the fixture function in a file called conftest.py

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
fixtures

---
### Conftest.py
We can define the fixture functions in conftest.py to make them accessible across multiple test files

conftest.py:
```
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input
```

You can now remove the fixture functions from the test_ file
```
import pytest

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
```

---
### Conftest.py
And use them in other files too:
```
import pytest

def test_divisible_by_13(input_value):
   assert input_value % 13 == 0
```

Now, we have multiple files making use of the fixture defined in conftest.py

---
### Conftest.py 

Tests will look for fixture in the same file.

As the fixture is not found in the file, it will check for fixture in conftest.py file

On finding it, the fixture method is invoked and the result is returned to the input argument of the test


---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Conftest.py

---
### Parameterizing tests

Parameterizing of a test is done to run the test against multiple sets of inputs

using the following marker
```
@pytest.mark.parametrize
```

Example
```
import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output
```

Here the test multiplies an input with 11 and compares the result with the expected output. The test has 4 sets of inputs, each has 2 values – one is the number to be multiplied with 11 and the other is the expected result

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
parameterized tests

---
### Skip and Xfail tests

Consider
- a test is not relevant for some time due to some reasons
- a new feature is being implemented and we already added a test for that feature

In these situations, we have the option to xfail the test or skip the tests

---
### Skip and Xfail tests (2)

Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests
 
Details of these tests will not be printed even if the test fails 
 
We can xfail tests using the following marker
```
@pytest.mark.xfail
```

---
### Skip and Xfail tests (3)

Skipping a test means that the test will not be executed. 

We can skip tests using the following marker
```
@pytest.mark.skip
```

Later, when the test becomes relevant we can remove the markers

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Skip and fail


---
### Stop Test Suite after N Test Failures

In a real scenario, once a new version of the code is ready to deploy, it is first deployed into pre-prod/ staging environment. 

Then a test suite runs on it.

The code is qualified for deploying to production only if the test suite passes. If there is test failure, whether it is one or many, the code is not production ready.

---
### Stop Test Suite after N Test Failures

What if we want to stop the execution of test suite soon after n number of test fails?

This can be done in pytest using maxfail

Example
```
pytest --maxfail = <num>
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
max fail

---
### Parallel execution

By default, pytest runs tests in sequential order

In a real scenario, a test suite will have a number of test files and each file will have a bunch of tests
- leads to a large execution time

We can run tests in parallel



---
### Parallel execution (2)

Install the pytest-xdist plugin

```
pip3 install pytest-xdist
```
Now, run tests by using the syntax 
```
pytest -n 'num'
```

-n num runs the tests by using multiple workers, here it is 3

We will not be having much time difference when there is only a few tests to run. However, it matters when the test suite is large

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
parallel execution


---
### Test Execution Results in XML Format

The details of the test execution can be stored in an xml file form dashboard projection.

Execute the tests and generate the xml by running
```
pytest test_multiplication.py -v --junitxml="result.xml"
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
generating xml


---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Exploring PyTest



