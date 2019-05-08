# nose2 

---
### Nose/2
A Python unit test framework

> nose2’s purpose is to extend unittest to make testing nicer and easier to understand

---

<!-- ---
### Nose2 Installation and Execution
The recommended way to install nose2 is with pip
```
pip install nose2
```
Running tests
```
nose2
```

This will find and run tests in all packages in the current working directory, and any sub-directories of the current working directory whose names start with ‘test’.

To find tests, nose2 looks for modules whose names start with ‘test’. In those modules, nose2 will load tests from all unittest.TestCase subclasses, as well as functions whose names start with ‘test’.

The nose2 script supports a number of command-line options, as well as extensive configuration via config files. For more information see Using nose2 and Configuring nose2. -->

---
### nose2
nose2 is 
- successor to nose
- unittest with plugins

> extend unittest to make testing nicer and easier to understand

---
### nose2 
nose2 is based on unittest
- use nose2 to add value on top of unittest

Example, written in typical unittest style:

```
import unittest

class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")
```

You can then run this test like so:
```
$ nose2 -v
```


---
### Added value of nose2
nose2 
- supports more testing configuration 
- provides more tools than unittest on its own

For example:
```
from nose2.tools import params

@params("Sir Bedevere", "Miss Islington", "Duck")
def test_is_knight(value):
    assert value.startswith('Sir')
```
and then run this like so:
```
$ nose2 -v --pretty-assert
```

---
### Added value of nose2 (2)

output:
```
test_fancy.test_is_knight:1
'Sir Bedevere' ... ok
test_fancy.test_is_knight:2
'Miss Islington' ... FAIL
test_fancy.test_is_knight:3
'Duck' ... FAIL

======================================================================
FAIL: test_fancy.test_is_knight:2
'Miss Islington'
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/ebs/home/sirosen/tmp/test_fancy.py", line 6, in test_is_knight
    assert value.startswith('Sir')
AssertionError

>>> assert value.startswith('Sir')

values:
    value = 'Miss Islington'
    value.startswith = <built-in method startswith of str object at 0x7f3c3172f430>
======================================================================
FAIL: test_fancy.test_is_knight:3
'Duck'
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/mnt/ebs/home/sirosen/tmp/test_fancy.py", line 6, in test_is_knight
    assert value.startswith('Sir')
AssertionError

>>> assert value.startswith('Sir')

values:
    value = 'Duck'
    value.startswith = <built-in method startswith of str object at 0x7f3c3172d490>
----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=2)
```

---
### Getting started with nose2
The recommended way to install nose2 is with pip
```
pip3 install nose2
```

---
### Running tests
To run tests in a project, use the nose2 script:
```
nose2
```

This will find and run tests in 
- all packages in the current working directory
-  any sub-directories of the current working directory whose names start with ‘test’


---
### Naming Tests
nose2 will look in each directory under the starting directory
unless the configuration modifies the included paths. 

Directories nose2 will look in:
- Directory that contains an __init__.py file (a Python package)
- Directory name that contains “test” after being lowercased.
- Directory name that is either lib or src

---
### Naming Tests (2)

Each of the following test files will be run:
- test.py
- test_views.py
- test_models.py
- testThingy.py

These files will not be run:
- not_a_test.py
- myapp_test.py
- some_test_file.py

---
### Naming Tests (3)

Within test modules, nose2 will load tests from unittest.TestCase subclasses
and from test functions (functions whose names begin with “test”).

---
### Running Tests
In the simplest case, go to the directory that includes your project source and run nose2:
```
nose2
```

This will discover tests in packages and test directories under that directory, load them, and run them

---
### Specifying Tests to Run
Pass test names to nose2 on the command line to run individual test modules, classes, or tests.

For example, to run the first test generated from the parameterized test test_params_func
```
pkg1.test.test_things.test_params_func:1
```

Plugins may provide other means of test selection.

---
### setup.py test
nose2 supports distribute/setuptools’ python setup.py test standard for running tests. 
To use nose2 to run your package’s tests, add the following to your setup.py:

```
setup(...
      test_suite='nose2.collector.collector',
      ...
      )
```

---
### Beware
Two warnings about running tests this way:

- because the setuptools test command is limited, nose2 returns a “test suite” that actually takes over the test running process completely, bypassing the test result and test runner that call it
    - this may be incompatible with some packages.

- because the command line arguments to the test command may not match up properly with nose2’s arguments, the   nose2 instance started by the collector does not accept any command line arguments. 
    - This means that it always runs all tests, and that you cannot configure plugins on the command line when running tests this way. 

As a workaround, nose2 will read configuration from setup.cfg 

### Recap

Nose2 vs Unittest
Advantages:
- Supercedes unittest
    Nose wraps around unittest, adding some more feature and functionality to it, such as SkipTest or auto-discovery.

- Minimal boilerplate
    Nose tries to keep boilerplate code to a minimum. As such, it's very easy to read and write initial tests.

- Numerous plugins available
There's a large number of plugins available which make unit testing easier. Things like coverage reporting, test selection and xUnit-compatible test output can be added through plugins.
