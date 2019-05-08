# PyTest Mocking

---
### Mocking in pytest
use a plugin

Thin-wrapper around the mock package for easier use with py.test
https://pypi.org/project/pytest-mock/


---
### pytest-mock plugin

This plugin installs a mocker fixture which is a thin-wrapper around the patching API 
provided by the mock package, but with the benefit of not having to worry about undoing 
patches at the end of a test

example:
```
import os
class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)

def test_unix_fs(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')
```

---
### pytest-mock plugin (2)

Another example:
```
import pytest

def sum(a, b):
    return a + b

def test_sum1(mocker):
    mocker.patch(__name__ + ".sum", return_value=9)
    assert sum(2, 3) == 9

def test_sum2(mocker):
    def crazy_sum(a, b):
        return b + b
    mocker.patch(__name__ + ".sum", side_effect=crazy_sum)
    assert sum(2, 3) == 6
```
Result:
```
============= test session starts ==============
platform cygwin -- Python 3.6.4, pytest-3.10.1, py-1.7.0, pluggy-0.8.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/xyz/temp, inifile:
plugins: mock-1.10.0, cov-2.6.0
collected 2 items

patch_test.py::test_sum1 PASSED          [ 50%]
patch_test.py::test_sum2 PASSED          [100%]

=========== 2 passed in 0.02 seconds ===========
```

---
### Mocker fixture API
The mocker fixture has the same API as mock.patch
```
def test_foo(mocker):
    # all valid calls
    mocker.patch('os.remove')
    mocker.patch.object(os, 'listdir', autospec=True)
    mocked_isfile = mocker.patch('os.path.isfile')
```

---
### Mocker fixture API (2)

The supported methods from the fixture are 
- mocker.patch
- mocker.patch.object
- mocker.patch.multiple
- mocker.patch.dict
- mocker.stopall
- mocker.resetall(): calls reset_mock() in all mocked objects up to this point.

---
### Mocker fixture objects
These objects from the mock module are accessible directly from mocker for convenience:
- Mock
- MagicMock
- PropertyMock
- ANY
- DEFAULT (Version 1.4)
- call (Version 1.1)
- sentinel (Version 1.2)
- mock_open
- Spy

---
### Spy 
The spy acts exactly like the original method in all cases
except it allows use of mock features with it, like retrieving call count

It also works for class and static methods

example:
```
def test_spy(mocker):
    class Foo(object):
        def bar(self):
            return 42

foo = Foo()
mocker.spy(foo, 'bar')
assert foo.bar() == 42
assert foo.bar.call_count == 1
```

---
### Stub
The stub is a mock object that accepts any arguments and is useful to test callbacks

example:
```
def test_stub(mocker):
    def foo(on_something):
        on_something('foo', 'bar')

    stub = mocker.stub(name='on_something_stub')

    foo(stub)
    stub.assert_called_once_with('foo', 'bar')
```

---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Exploring PyTest-Mock