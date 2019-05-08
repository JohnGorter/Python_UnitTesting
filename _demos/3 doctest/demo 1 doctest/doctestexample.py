"""
This is the "example" module.
The example module supplies one function, sum().  For example,
"""

def sum(a, b):
    """Return the sum of a and b 
    >>> sum(10,10)
    20

    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()