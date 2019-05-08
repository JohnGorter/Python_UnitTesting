"""
This is the "example" module.
The example module supplies one function, sum().  For example,
>>> sum(10, 100)
110
"""

def sum(a, b):
    """Return the sum of a and b 
    >>> print(john)
    YES

    >>> sum(10,100)
    110
    >>> sum(1,1)
    2
    >>> sum("a",1)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'john':"YES"})