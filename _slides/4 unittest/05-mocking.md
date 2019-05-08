# more mocking

---
### Mock Patching Methods
Common uses for Mock objects include

- Patching methods
- Recording method calls on objects

You might want to replace a method on an object to check that it is called with the correct arguments by another part of the system:
```
>>> real = SomeClass()
>>> real.method = MagicMock(name='method')
>>> real.method(3, 4, 5, key='value')
<MagicMock name='method()' id='...'>
```

Once our mock has been used (real.method in this example) it has methods and attributes that allow you to make assertions about how it has been used.

---
### Mock Assertions
Once the mock has been called its called attribute is set to True

To check that it was called with the correct arguments, use
- assert_called_with() 
- assert_called_once_with() 

Example:
```
>>> class ProductionClass:
...     def method(self):
...         self.something(1, 2, 3)
...     def something(self, a, b, c):
...         pass
...
>>> real = ProductionClass()
>>> real.something = MagicMock()
>>> real.method()
>>> real.something.assert_called_once_with(1, 2, 3)
```

---
### Mock for Method Calls on an Object
Another common use case is to pass an object into a method (or some part of the system under test) and then check that it is used in the correct way

The simple ProductionClass below has a closer method
If it is called with an object then it calls close on it
```
class ProductionClass:
    def closer(self, something):
        something.clos

real = ProductionClass()
mock = Mock()
real.closer(mock)
mock.close.assert_called_with()
```

We don’t have to do any work to provide the ‘close’ method on our mock. Accessing close creates it. 

---
### Mocking Classes

When you patch a class, then that class is replaced with a mock

Instances are created by calling the class

In the example below we have a function some_function that instantiates Foo and calls a method on it. The call to patch() replaces the class Foo with a mock. The Foo instance is the result of calling the mock, so it is configured by modifying the mock return_value.

```
def some_function():
    instance = module.Foo()
    return instance.method()

with patch('module.Foo') as mock:
    instance = mock.return_value
    instance.method.return_value = 'the result'
    result = some_function()
    assert result == 'the result'
```

---
### Naming your mocks
It can be useful to give your mocks a name. 
- name is shown in the repr of the mock 
- can be helpful when the mock appears in test failure messages

The name is also propagated to attributes or methods of the mock:
```
mock = MagicMock(name='foo')
mock
<MagicMock name='foo' id='...'>
mock.method
<MagicMock name='foo.method' id='...'>
```

---
### Tracking calls
Often you want to track more than a single call to a method.
The mock_calls attribute records all calls to child attributes of the mock 
- also to their children

```
mock = MagicMock()
mock.method()
<MagicMock name='mock.method()' id='...'>
mock.attribute.method(10, x=53)
<MagicMock name='mock.attribute.method()' id='...'>
mock.mock_calls
[call.method(), call.attribute.method(10, x=53)]
```

---
### Tracking calls (2)

If you make an assertion about mock_calls and any unexpected methods have been called
then the assertion will fail!

You use the call object to construct lists for comparing with mock_calls:

```
expected = [call.method(), call.attribute.method(10, x=53)]
mock.mock_calls == expected
True
```

---
<!-- .slide: data-background="url('images/demo.jpg')" data-background-size="cover" --> 
<!-- .slide: class="lab" -->
## Demo time!
mocking and asserting method calls

---
### Tracking calls (3)
However, parameters to calls that return mocks are not recorded
which means it is not possible to track nested calls where the parameters
used to create ancestors are important:

```
m = Mock()
m.factory(important=True).deliver()
<Mock name='mock.factory().deliver()' id='...'>
m.mock_calls[-1] == call.factory(important=False).deliver()
True
```

---
### Setting Return Values and Attributes
Setting the return values on a mock object is trivially easy:

```
mock = Mock()
mock.return_value = 3
mock()
3
```

Of course you can do the same for methods on the mock:
```
mock = Mock()
mock.method.return_value = 3
mock.method()
3
```

---
### Setting Return Values and Attributes (2)
The return value can also be set in the constructor:
```
mock = Mock(return_value=3)
mock()
3
```

If you need an attribute setting on your mock, just do it:

```
mock = Mock()
mock.x = 3
mock.x
3
```


---
### Setting Return Values and Attributes (3)

Sometimes you want to mock up a more complex situation 
- for example mock.connection.cursor().execute("SELECT 1")

If we wanted this call to return a list, then we have to configure the result of the nested call

We can use call to construct the set of calls in a “chained call” 
```
mock = Mock()
cursor = mock.connection.cursor.return_value
cursor.execute.return_value = ['foo']
mock.connection.cursor().execute("SELECT 1")
['foo']
expected = call.connection.cursor().execute("SELECT 1").call_list()
mock.mock_calls
[call.connection.cursor(), call.connection.cursor().execute('SELECT 1')]
mock.mock_calls == expected
True
```

It is the call to .call_list() that turns our call object into a list of calls representing the chained calls

---
### Raising exceptions with mocks
A useful attribute is side_effect
```
mock = Mock(side_effect=Exception('Boom!'))
mock()
Traceback (most recent call last):
  ...
Exception: Boom!
```

---
### Side effect functions and iterables
side_effect can also be set to a function or an iterable
- where your mock is going to be called several times,
- you want each call to return a different value

```
mock = MagicMock(side_effect=[4, 5, 6])
mock()
4
mock()
5
mock()
6
```


---
### Side effect functions and iterables (2)
For more advanced use cases, side_effect can be a function
The function will be called with the same arguments as the mock

Whatever the function returns is what the call returns:
```
vals = {(1, 2): 1, (2, 3): 2}
def side_effect(*args):
    return vals[args]

mock = MagicMock(side_effect=side_effect)
mock(1, 2)
1
mock(2, 3)
2
```

---
### Specs
Mock allows you to provide an object as a specification for the mock, 
using the spec keyword argument

Accessing methods / attributes on the mock that don’t exist on your specification object 
will immediately raise an attribute error

```
mock = Mock(spec=SomeClass)
mock.old_method()
Traceback (most recent call last):
   ...
AttributeError: object has no attribute 'old_method'
```

---
### Specs

Using a specification also enables a smarter matching of calls made to the mock, 
regardless of whether some parameters were passed as positional or named arguments

```
def f(a, b, c): pass

mock = Mock(spec=f)
mock(1, 2, 3)
<Mock name='mock()' id='140161580456576'>
mock.assert_called_with(a=1, b=2, c=3)
```

---
### Patch Decorators
A common need in tests is to patch a class attribute or a module attribute
- for example patching a builtin 
- patching a class in a module to test that it is instantiated

 Modules and classes are effectively global
 - patching on them has to be undone after the test or the patch will persist into other tests!
 
mock provides three convenient decorators 
- patch()
- patch.object()
- patch.dict()

---
### Patch Decorators (2)
- Patch takes a single string to specify the attribute to patch
    - it also optionally takes a value that you want the attribute (or class or whatever) to be replaced with
- ‘patch.object’ takes an object and the name of the attribute to patch plus optionally the value to patch it with

patch.object:
```
original = SomeClass.attribute
@patch.object(SomeClass, 'attribute', sentinel.attribute)
def test():
    assert SomeClass.attribute == sentinel.attribute

test()
assert SomeClass.attribute == original

```

---
### Patch Decorators (3)
If you are patching a module (including builtins) then use patch() instead of patch.object():
```
mock = MagicMock(return_value=sentinel.file_handle)
with patch('builtins.open', mock):
    handle = open('filename', 'r')

mock.assert_called_with('filename', 'r')
assert handle == sentinel.file_handle, "incorrect file handle returned"
```

---
### Patch Decorators (4)
A nice pattern is to actually decorate test methods themselves:
```
class MyTest(unittest.TestCase):
    @patch.object(SomeClass, 'attribute', sentinel.attribute)
    def test_something(self):
        self.assertEqual(SomeClass.attribute, sentinel.attribute)

original = SomeClass.attribute
MyTest('test_something').test_something()
assert SomeClass.attribute == original
```

---
### Patch with a mock
If you want to patch with a Mock, 
you can use patch() or patch.object()
 
The mock will be created for you and passed into the test function / method
```
class MyTest(unittest.TestCase):
    @patch.object(SomeClass, 'static_method')
    def test_something(self, mock_method):
        SomeClass.static_method()
        mock_method.assert_called_with()

MyTest('test_something').test_something()
```

---
### Patch with a mock (2)
You can stack up multiple patch decorators using this pattern:
```
class MyTest(unittest.TestCase):
    @patch('package.module.ClassName1')
    @patch('package.module.ClassName2')
    def test_something(self, MockClass2, MockClass1):
        self.assertIs(package.module.ClassName1, MockClass1)
        self.assertIs(package.module.ClassName2, MockClass2)

MyTest('test_something').test_something()
```

---
### Patch dict
There is also patch.dict() for setting values in a dictionary 
just during a scope and restoring the dictionary to its original state when the test ends:
```
foo = {'key': 'value'}
original = foo.copy()
with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
    assert foo == {'newkey': 'newvalue'}

assert foo == original
```

---
### Patch with context managers
patch, patch.object and patch.dict can all be used as context managers

Where you use patch() to create a mock for you,
you can get a reference to the mock using the “as” form of the with statement:

```
class ProductionClass:
    def method(self):
        pass

with patch.object(ProductionClass, 'method') as mock_method:
    mock_method.return_value = None
    real = ProductionClass()
    real.method(1, 2, 3)

mock_method.assert_called_with(1, 2, 3)
```

---
### Patch decorators on class
As an alternative patch, patch.object and patch.dict can be used as class decorators. 
When used in this way it is the same as applying the decorator individually to every method
whose name starts with “test”.

---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
More mocking dependencies
