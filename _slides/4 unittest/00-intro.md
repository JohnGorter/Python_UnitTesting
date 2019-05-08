
# unittest

---
### Unittest 
- built into the Python standard library since version 2.1. 
  - often used in commercial applications and open-source projects

- unittest contains
  - a testing framework
  - a test runner

- unittest requires that
  - you put your tests into classes as methods
  - you use special assertion methods in the unittest.TestCase class instead of the built-in assert statement

---
### Unittest (2)
Originally inspired by JUnit that has a similar flavor as major unit testing frameworks in other languages

Unittest
- supports test automation 
- sharing of setup and shutdown code for tests
- aggregation of tests into collections
- independence of the tests from the reporting framework.
- is object-oriented

---
### Unittest (3)

unittest classes in the framework

<image src="./images/PythonUnitTest1.gif"></image>

---
### Writing tests
Remeber the ingredients of unit testing were:
- Arrange
- Act
- Assert

Where the last 'Assert' part often is provided through an API.
Python has that API too...

Assert validates the results

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Asserting through the REPL

---
### Writing the tests (2)
Making a test case instead of testing on the REPL
- make file called test_sum.py

```py
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Your first unit test

---
### Writing the tests (3)
Steps to use unittest
- import unittest from the standard library
- create a class that inherits from the TestCase class
- write test methods 
  - use assertions like self.assertEqual() 
- call unittest.main()

if you’re writing test cases for Python 2 and 3
- in Python 2.7 and below, unittest is called unittest2
- if you simply import from unittest, you will get different versions with different features between Python 2 and 3

<!-- ---
### Writing the tests (4)

<image style="height:80vh" src="./images/PythonUnitTest2.gif"></image> -->

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Hello unittest

---

### Assertion methods
lists the most commonly used methods 

|Method|Checks that	|New in|
|---|---|---|
|assertEqual(a, b)|	a == b|	 |
|assertNotEqual(a, b)|	a != b|	 |
|assertTrue(x)|	bool(x) is True|	| 
|assertFalse(x)|	bool(x) is False|	 |
|assertIs(a, b)|	a is b|	3.1|
|assertIsNot(a, b)|	a is not b|	3.1|
|assertIsNone(x)|	x is None|	3.1|

---
### Assertion methods (2)

|Method|Checks that	|New in|
|---|---|---|
|assertIsNotNone(x)|	x is not None|	3.1|
|assertIn(a, b)|	a in b|	3.1|
|assertNotIn(a, b)|	a not in b|	3.1|
|assertIsInstance(a, b)|	isinstance(a, b)|	3.2|
|assertNotIsInstance(a, b)|	not isinstance(a, b)|	3.2|

---
### Assertion methods (3)

Check the production of exceptions, warnings, and log messages using the following methods:

|Method|	Checks that|	New in|
|---|---|---|
|assertRaises(exc, fun, *args, **kwds)|	fun(*args, **kwds) raises exc|	 
|assertRaisesRegex(exc, r, fun, *args, **kwds)|	fun(*args, **kwds) raises exc and the message matches regex r|	3.1|
|assertWarns(warn, fun, *args, **kwds)|	fun(*args, **kwds) raises warn|	3.2|
|assertWarnsRegex(warn, r, fun, *args, **kwds)|	fun(*args, **kwds) raises warn and the message matches regex| r	3.2|
|assertLogs(logger, level)|	The with block logs on logger with minimum level|	3.4|

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Hello assertWarn

---
### Running tests
Test are run using test runners
- a special application designed for running tests
  - checks output
  - gives tools for debugging and diagnosing tests

---

### Running tests (2)
Run tests from the command line
```
python3 demo_unittest.py
```
or use -v
```
python3 demo_unittest.py -v
```

Your script has to call the main() entry point

---
### Running tests (3)
The main entrypoint can be 
```
if __name__ == "__main__":
  unittest.main()
```
or
```
results = unittest.TextTestRunner().Run()
```

---
###  Running tests (4)
Run test from command-line interface
The unittest module can be used from the command line directly to run tests

using modules
```
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```
using files
```
python -m unittest tests/test_something.py
```

---
###  Running tests (4) 
Running tests using test discovery

- Unittest supports simple test discovery 
- in order to be compatible with test discovery
  - all test files must be modules or packages
  - importable from the top-level directory of the project
    - their filenames must be valid identifiers

- implemented in TestLoader.discover()
  - can also be used from the command line
```
cd project_directory
python -m unittest discover
```

---
### Discover sub-commands

|switch|Meaning|
|---|---|
|-v, --verbose|Verbose output|
|-s, --start-directory directory|
Directory to start discovery (. default)|
|-p, --pattern pattern|Pattern to match test files (test*.py default)|
|-t, --top-level-directory directory|Top level directory of project (defaults to start directory)|

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Running tests through discover


---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Write your first unittest tests