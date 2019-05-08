# unittest mock

---
### Test Doubles

> In automated unit testing, it may be necessary to use objects or procedures that look and behave like their release-intended counterparts, but are actually simplified versions that reduce the complexity and facilitate testing. 

A test double is a generic (meta) term used for these objects or procedures

---
### Test Doubles (2)
Different types of test doubles
- Test stub 
  - providing the tested code with "indirect input"
- Mock object 
  - verifying "indirect output" of the tested code, by defining the expectations before the tested code is executed
- Test spy 
  - verifying "indirect output" of the tested code, by asserting the expectations afterwards, without having defined the expectations before the tested code is executed
- Fake object 
  - a simpler implementation, e.g. using an in-memory database in the tests instead of doing real database access
- Dummy object 
  - when a parameter is needed for the tested method but without actually needing to use the parameter

--
### Mocking
Mocking is simply the act of replacing the part of the application you are testing with a dummy version of that part called a mock.

Instead of calling the actual implementation, you would call the mock, and then make assertions about what you expect to happen.

---
### benefits of mocking
Benefits of mocking
- Increased speed 
    - Tests that run quickly are extremely beneficial
- Avoiding undesired side effects during testing 
- If you are testing a function which makes calls to an external API, you may not want to make an actual API call every time you run your tests. You’d have to change your code every time that API changes, or there may be some rate limits, but mocking helps you avoid that.

---
### Using test doubles
unittest.mock

> unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.


---
### Using test doubles (2)
unittest.mock
- provides a core Mock class
- removes the need to create a host of stubs throughout your test suite
- after performing action, assertions about which methods/attributes and arguments where used can be made
- return values can be specified and needed attributes can be set

Additionally, mock provides 
- a patch() decorator that handles patching module and class level attributes within the scope of a test
  along with sentinel for creating unique objects

---
### Using test doubles (3)
unittest.mock classes and decorators
- Mock/ MagicMock 
  - create all attributes and methods as you access them and store details of how they have been used
  - with Mock you can mock magic methods but you have to define them
  - while MagicMock has "default implementations of most of the magic methods."
  - more on this later..
- patch()

If you don't need to test any magic methods, Mock is adequate and doesn't bring a lot of extraneous things into your tests
If you need to test a lot of magic methods MagicMock will save you some time


---
### Using test doubles (4)
An example of Mock/MagicMock
```
>>> from unittest.mock import MagicMock
>>> thing = ProductionClass()
>>> thing.method = MagicMock(return_value=3)
>>> thing.method(3, 4, 5, key='value')
3
>>> thing.method.assert_called_with(3, 4, 5, key='value')
```

---
### Using test doubles (4)
side_effect parameter allows you to perform side effects, 
including raising an exception when a mock is called

```
>>> mock = Mock(side_effect=KeyError('foo'))
>>> mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'
```

---
### Using test doubles (4)
more examples

```
>>> values = {'a': 1, 'b': 2, 'c': 3}
>>> def side_effect(arg):
...     return values[arg]
...
>>> mock.side_effect = side_effect
>>> mock('a'), mock('b'), mock('c')
(1, 2, 3)
>>> mock.side_effect = [5, 4, 3, 2, 1]
>>> mock(), mock(), mock()
(5, 4, 3)
```

---
### Patch Decorator
The patch() decorator / context manager makes it easy to mock classes or objects in a module under test.

```
>>> from unittest.mock import patch
>>> @patch('module.ClassName2')
... @patch('module.ClassName1')
... def test(MockClass1, MockClass2):
...     module.ClassName1()
...     module.ClassName2()
...     assert MockClass1 is module.ClassName1
...     assert MockClass2 is module.ClassName2
...     assert MockClass1.called
...     assert MockClass2.called
...
>>> test()
```




