# doctest

---
### Agenda
- What are docstrings
- What is docstring testing

---
### Python docstrings
documentation string is string literal in the class, module, function or method definition
- written as a first statement
- accessible from the doc attribute for any of the Python object 
- accessible with the built-in help() function 

Two forms of writing a Docstring
- one-line Docstrings
- multi-line Docstrings

---
### One-line Docstrings
The one-line Docstrings are the Docstrings which fits all in one line. 

```
def square(a):
    '''Returns argument a is squared.'''
    return a*a

print (square.__doc__)

help(square)
```

outputs:
```
Returns argument a is squared.

Help on function square in module __main__:
square(a)
    Returns argument a is squared.
```

---
### Summary One-line Docstrings 
Takeaways
- the line begins with a capital letter, i.e., R in our case and end with a period(".")
- the closing quotes are on the same line as the opening quotes. This looks better for one-liners
- there's no blank line either before or after the Docstring. It is good practice

The above line in quotes is more of command than a description which ends with a period sign at last.

---
### Multi-line Docstrings
The general format for writing a Multi-line Docstring is as follows
```
def some_function(argument1):
    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """

    return argument1

print(some_function.__doc__)
```
outputs:
```
Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Docstrings


---
### Python Built-in Docstrings
All the built-in function, classes, methods have the actual human description attached to it. 

You can access it in one of two ways.
- doc attribute
- the help function

---
### Python Built-in Docstrings (2)
For example
```
import time
print(time.__doc__)
```
outputs:

```
This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (including century, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.
```


---
### Python Built-in Docstrings (2)
Similarly:
```
help(print)
```
outputs:
```
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

---
### Doctest
This module searches for pieces of text that look like interactive Python sessions
- executes to verify that they work 

There are several common ways to use doctest
- to check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented
- to perform regression testing by verifying that interactive examples from a test file or a test object work as expected
- to write tutorial documentation for a package, liberally illustrated with input-output examples

---
### Doctest (2)

an example
```
"""
This is the "example" module.
The example module supplies one function, sum().  For example,
>>> sum(10, 100)
110
"""

def sum(a, b):
    """Return the sum of a and b 
    >>> sum(10,100)
    110
    >>> sum("a",1)
    Traceback (most recent call last):
        ...
    TypeError: cannot concatenate 'str' and 'int' objects
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

```


---
### Run Doctest
Run doctests using the command line
```
python3 filename.py (-v)
or
python -m doctest -v filename.py
```

No output means success!

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Testing with doctest

---
### Using example files
Another application of doctest is testing interactive examples in a text file
```
import doctest
doctest.testfile("example.txt")
```

The file contains docstring:
```
The ``mysum`` module
======================

Using ``mysum``
-------------------

This is an example text file in reStructuredText format.  First import
``sum`` from the ``mysum`` module:

    >>> from mysum import sum

Now use it:

    >>> sum(6,10)
    16
```

---
### Running doctest with example file
To run
```
python3 filename.py (-v)
or
python -m doctest -v filename.py
or 
python -m doctest -v example.txt
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
Using example files


---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Write your first doctest tests