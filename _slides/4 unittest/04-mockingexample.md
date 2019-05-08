# mocking example walkthrough

---
### Basic Usage
Imagine a simple class:
```
class Calculator:
    def sum(self, a, b):
        return a + b
```
This class implements one method, sum that takes two arguments, the numbers to be added, a and b. It returns a + b;

A simple test case for this could be as follows:
```
from unittest import TestCase
from main import Calculator
class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)
```

---
### Run the test
You can run this test case using the command:
```
python -m unittest
```
You should see output that looks approximately like this:
```
.
_____________________________________________________________

Ran 1 test in 0.003s

OK
```

Pretty fast, right?

---
### Adding complexity
Now, imagine the code looked like this:
```
import time

class Calculator:
    def sum(self, a, b):
        time.sleep(10) # long running process
        return a + b
```

Since this is a simple example, we are using time.sleep() to simulate a long running process. 

---
### Adding complexity (2)

The previous test case now produces the following output:
```
.
_____________________________________________________________

Ran 1 test in 10.003s

OK
```

That process has just considerably slowed down our tests.

---
### Refactor the test 

Better, we use a mock sum function with well defined behavior
```
from unittest import TestCase
from unittest.mock import patch

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)
```

We are importing the patch decorator from unittest.mock 
It replaces the actual sum function with a mock function 
In this case, our mock function always returns 9

---
### Running test case

we get this output:
```
.
_____________________________________________________________

Ran 1 test in 0.001s

OK
```

---
### A More Advanced Example
In this example, we’ll be using the requests library to make API calls. You can get it via pip install.
```
pip install requests
```
Our code under test in main.py looks as follows:
```
import requests

class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)
```

This code defines a class Blog with a posts method. 
Invoking posts on the Blog object will trigger an API call to jsonplaceholder, a JSON generator API service

---
### A More Advanced Example (2)
In our test, we want to mock out the unpredictable API call and only test that a Blog object’s posts method returns posts
We will need to patch all Blog objects’ posts methods 

```
from unittest import TestCase
from unittest.mock import patch, Mock

class TestBlog(TestCase):
    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)
```

---
### A More Advanced Example (3)

This produces the following output:
```
.
_____________________________________________________________

Ran 1 test in 0.001s

OK
```

Note that testing the mocked value instead of an actual blog object allows us to make extra assertions about how the mock was used

---
### More Mocking 

A mock allows us to test 
- how many times it was called
- the arguments it was called with 
- whether the mock was called at all

We’ll see additional examples in the next section.

---
### More Mocking (2)
Other Assertions We Can Make on Mocks
Using the previous example, these are useful assertions on the Mock blog object


```
# Additional assertions
assert MockBlog is main.Blog # The mock is equivalent to the original

assert MockBlog.called # The mock wasP called

blog.posts.assert_called_with() # We called the posts method with no arguments

blog.posts.assert_called_once_with() # We called the posts method once with no arguments

# blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts with no arguments

blog.reset_mock() # Reset the mock object

blog.posts.assert_not_called() # After resetting, posts has not been called.
```

---
### More Mocking (3)

Mock objects can also be reset to a pristine state 
- the mock object has not been called yet
- especially useful when you want to make multiple calls to your mock and want each one to run on a fresh instance of the mock

---
### Side Effects
Things that you want to happen when your mock function is called

Common examples are 
- calling another function 
- raising exceptions

---
### Side Effects (2) 
Let us revisit our sum function. What if, instead of hard coding a return value, we wanted to run a custom sum function instead? 

Our custom function will mock out the undesired long running time.sleep call and only remain with the actual summing functionality we want to test. 

We can simply define a side_effect in our test

```
from unittest import TestCase
from unittest.mock import patch

def mock_sum(a, b):
    # mock sum function without the long running time.sleep
    return a + b

class TestCalculator(TestCase):
    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 5)
        self.assertEqual(sum(7,3), 10)
```

---
### Side Effects (3)
Running the tests should pass
```
.
_____________________________________________________________

Ran 1 test in 0.001s

OK
```



---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Mocking dependencies