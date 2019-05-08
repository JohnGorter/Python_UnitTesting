class MyClass(object):
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    >>> unpredictable(MyClass())
    [<class.MyClass object at 0x10055a2d0>]

    >>> unpredictable(MyClass()) 
    [<class.MyClass object at 0x...>]

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<class.MyClass object at 0x...>]
    """
    return [obj]

