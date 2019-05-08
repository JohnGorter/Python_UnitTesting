# more unittest

---
### Agenda
- Setup and Teardown aka Test fixtures
- Test Suites

---
### Setup and Teardown
The basic building blocks of unit testing are test cases
- single scenarios that must be set up and checked for correctness
- test cases are represented by unittest.TestCase instances


> The testing code of a TestCase instance should be entirely self contained, such that it can be run either in isolation or in arbitrary combination with any number of other test cases

---
### Setup and Teardown (2)

The simplest TestCase subclass will simply implement a test method (i.e. a method whose name starts with test) in order to perform specific testing code:
```
import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

```

---
### Setup and Teardown (3)
Tests can be numerous, and their set-up can be repetitive. 
- we can factor out set-up code by implementing a method called setUp()
- testing framework will call this automatically call for every single test we run

```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
```

> The order is determined by sorting the test method names

---
### Setup and Teardown (4)

If the setUp() method raises an exception while the test is running, 
the framework will consider the test to have suffered an error, and the test method will not be executed

---
### Setup and Teardown (5)
Similarly, there is a tearDown() method that tidies up after the test method has been run:
```
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
```

If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.

> This is called a test fixture

---
### Setup and Teardown (6)

There is also setUp and tearDown for 
- classes
    - setUpClass and tearDownClass
- modules
    - setupModule and tearDownModule

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
setUp and tearDown

---
### Organizing test code
It is recommended that you use TestCase implementations to group tests together according to the features they test. 

- test suite represented by TestSuite class

All tests are run automatically but you can build a testsuite manually:
```
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```

---
### Test Suites
Usually, a few test cases are enough for your testing needs of a single class
- what if you have a dozen or more tests cases on hand?
- what if you want only a subset of test routines to run from the same test case
- what if you want to refactor your test routines for easier cataloging and distribution?

Test Suite -> a set of grouped tests to execute

---
### Test Suites (2)
Placing the test code in a separate module

Advantages
- the test module can be run standalone from the command line
- the test code can more easily be separated from shipped code
- there is less temptation to change test code to fit the code it tests without a good reason
- test code should be modified much less frequently than the code it tests
- tested code can be refactored more easily
- tests for modules written in C must be in separate modules anyway, so why not be consistent?
- if the testing strategy changes, there is no need to change the source code

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
testsuits

---
### Skipping tests

Unittest supports 

- skipping individual test methods 
- skipping classes of tests
- marking a test as an “expected failure,” 
    - a test that is broken and will fail, but shouldn’t be counted as a failure on a TestResult

---
### Skipping tests (2)
You can skip a test (conditionally) using the skipTest base call
```
class MyTestCase(unittest.TestCase):
    def test_me(self, arg):
        self.skipTest("not doing anything anymore")

    def test_onMac(self):
        if sys.platform.startswith("win"):
            self.skipTest("requires Non Windows OS")
        print("testing")        
```

---
### Skipping tests (3)
You can also use decorators
```
class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3), "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
```

---
### Skipping tests (3)

Output in verbose mode:
```
test_format (__main__.MyTestCase) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase) ... skipped 'demonstrating skipping'
test_windows_support (__main__.MyTestCase) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK (skipped=3)
```

---
### Skipping tests (4)

Classes can be skipped just like methods
```
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```

TestCase.setUp() can also skip the test. This is useful when a resource that needs to be set up is not available.

---
### Skipping Tests (5)
Expected failures use the expectedFailure() decorator.
```
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```
        
---
### Skipping Tests (6)

It’s easy to roll your own skipping decorators by making a decorator that calls skip() on the test when it wants it to be skipped. This decorator skips the test unless the passed object has a certain attribute:

def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Skipping tests

---
### Distinguishing test iterations using subtests
When there are very small differences among your tests, for instance some parameters, 
unittest allows you to distinguish them inside the body of a test method using the subTest() context manager

For example, the following test:
```
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

---
### Outputs
will produce the following output:

```
======================================================================
FAIL: test_even (__main__.NumbersTest) (i=1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest) (i=3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest) (i=5)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0
```

Without using a subtest, execution would stop after the first failure, and the error would be less easy to diagnose because the value of i wouldn’t be displayed:

---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Advancing your unit tests