# more doctest

---
### Handling unpredictable output
There are other cases where the exact output may not be predictable
- but should still be testable!

examples
- local date and time values and object ids change on every test run
- default precision used in the representation of floating point values depend on compiler options
- object string representations may not be deterministic

---
### Example unpredictable output
```
class MyClass(object):
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    >>> unpredictable(MyClass())
    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]
    """
    return [obj]
```

These id values change each time a program runs, because it is loaded into a different part of memory.

---
### Example unpredictable output (2)
When the tests include values that are likely to change in unpredictable ways
and where the actual value is not important to the test results
- use the ELLIPSIS option to ignore portions of the verification value

```
class MyClass(object):
    pass

def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return [obj]
```

The comment after the call to unpredictable() (#doctest: +ELLIPSIS) tells doctest to turn on the ELLIPSIS option for that test

---
<!-- .slide: class="lab" -->
## Demo time!
Unpredictable output


---
### Tracebacks
Tracebacks are a special case of changing data
- paths in a traceback depend on the location where a module is installed on the filesystem on a given system
- it would be impossible to write portable tests if they were treated the same as other output
```
def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/no/such/path/doctest_tracebacks.py", line 14, in this_raises
        raise RuntimeError('here is the error')
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
```

doctest makes a special effort to recognize tracebacks, and ignore the parts that might change from system to system

---
### Tracebacks

In fact, the entire body of the traceback is ignored and can be omitted.

```
def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
```

When doctest sees a traceback header line 
- it skips ahead to find the exception type and message, ignoring the intervening lines entirely

---
### Working Around Whitespace
In real world applications, output usually includes whitespace such as blank lines, tabs, and extra spacing to make it more readable
- blank lines cause issues with doctest because they are used to delimit tests

example: double_space() takes a list of input lines, and prints them double-spaced with blank lines between

```
def double_space(lines):
    """Prints a list of lines double-spaced.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    
    Line two.
    
    """
    for l in lines:
        print l
        print
    return
```
outputs:
```
***Test Failed*** 1 failures.
```

---
### Working Around Whitespace (2)

The test fails, because it interprets the blank line after Line one as the end of the sample output

To match the blank lines, replace them in the sample input with the string <BLANKLINE>

```
def double_space(lines):
    """Prints a list of lines double-spaced.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    """
    for l in lines:
        print l
        print
    return
```

doctest replaces actual blank lines with the same literal before performing the comparison, so now the actual and expected values match and the test passes


---
### Working Around Whitespace (3)
Another pitfall of using text comparisons for tests is that embedded whitespace can also cause tricky problems with tests

This example has a single extra space after the 6
```
def my_function(a, b):
    """
    >>> my_function(2, 3)
    6 
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
```

Extra spaces could ocur via copy-and-paste errors, but they can go unnoticed in the source file and be invisible in the test failure report as well

---
### Working Around Whitespace (3)

Using one of the diff-based reporting options (REPORT_NDIFF) shows the difference between the actual and expected values with more detail
- the extra space becomes visible

```
def my_function(a, b):
    """
    >>> my_function(2, 3) #doctest: +REPORT_NDIFF
    6 
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b
```

Unified (REPORT_UDIFF) and context (REPORT_CDIFF) diffs are also available, for output where those formats are more readable

---
### Working Around Whitespace (4)

There are cases where it is beneficial to add extra whitespace in the sample output for the test, and have doctest ignore it
- data structures can be easier to read when spread across several lines, even if their representation would fit on a single line

```
def my_function(a, b):
    """Returns a * b.

    >>> my_function(['A', 'B', 'C'], 3) #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B', 'C',
     'A', 'B', 'C',
     'A', 'B', 'C']

    This does not match because of the extra space after the [ in the list
    
    >>> my_function(['A', 'B', 'C'], 2) #doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B', 'C',
      'A', 'B', 'C' ]
    """
    return a * b
```
    
When NORMALIZE_WHITESPACE is turned on, any whitespace in the actual and expected values is considered a match. 
- you cannot add whitespace to the expected value where none exists in the output 
- the length of the whitespace sequence and actual whitespace characters do not need to match

The first test example gets this rule correct, and passes, even though there are extra spaces and newlines
The second has extra whitespace after [ and before ], so it fails

---
### Test locations 
All of the tests in the examples so far have been written in the docstrings of the functions they are testing
- you can use textfiles (saw that earlier..)
-  doctest looks for tests in other places, too

```
#!/usr/bin/env python
# encoding: utf-8

"""Tests can appear in any docstring within the module.

Module-level tests cross class and function boundaries.

>>> A('a') == B('b')
False
"""

class A(object):
    """Simple class.

    >>> A('instance_name').name
    'instance_name'
    """
    def __init__(self, name):
        self.name = name
    def method(self):
        """Returns an unusual value.

        >>> A('name').method()
        'eman'
        """
        return ''.join(reversed(list(self.name)))

class B(A):
    """Another simple class.
        
    >>> B('different_name').name
    'different_name'
    """
```

Every docstring can contain tests at the module, class and function level.

---
### Test locations (2)

In cases where you have tests that you want to include with your source code, but do not want to have appear in the help for your module
- you need to put them somewhere other than the docstrings
- doctest also looks for a module-level variable called __test__ and uses it to locate other tests
- __test__ should be a dictionary mapping test set names (as strings) to strings, modules, classes, or functions

```
__test__ = {
    'numbers':"""
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",

    'strings':"""
>>> my_function('a', 3)
'aaa'

>>> my_function(3, 'a')
'aaa'
""" 
}

def my_function(a, b):
    """Returns a * b
    """
    return a * b
```

If the value associated with a key is a string, it is treated as a docstring and scanned for tests
If the value is a class or function, doctest searchs them recursivesly for docstrings, which are then scanned for tests

---
<!-- .slide: class="lab" -->
## Demo time!
Test Locations


---
### Test Context
The execution context created by doctest as it runs tests contains a copy of the module-level globals for the module containing your code
- isolates the tests from each other somewhat, so they are less likely to interfere with one another
- each test source (function, class, module) has its own set of global values

TestGlobals has two methods, one() and two() 
- the tests in the docstring for one() set a global variable, and the test for two() looks for it (expecting not to find it)

```
class TestGlobals(object):

    def one(self):
        """
        >>> var = 'value'
        >>> 'var' in globals()
        True
        """

    def two(self):
        """
        >>> 'var' in globals()
        False
        """
```

---
### Test Context (2)
That does not mean the tests cannot interfere with each other, if they change the contents of mutable variables defined in the module

```
_module_data = {}

class TestGlobals(object):

    def one(self):
        """
        >>> TestGlobals().one()
        >>> 'var' in _module_data
        True
        """
        _module_data['var'] = 'value'

    def two(self):
        """
        >>> 'var' in _module_data
        False
        """
```    
The module varabile _module_data is changed by the tests for one(), causing the test for two() to fail

---
### Test Context (3)
If you need to set global values for the tests
- to parameterize them for an environment for example
- pass values to testmod() and testfile() and have the context set up using data you control

```
if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'john':"YES"})
```

---
<!-- .slide: class="lab" -->
## Demo time!
Test Contexts


---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Write your first unittest tests