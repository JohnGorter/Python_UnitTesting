# doctest - unittest

---
### Doctest vs Unittest

Both are valuable
- doctest for cases where the test is giving an example of usage that is actually useful as documentation
  - most use doctest in reverse: not to test code is correct based on doctest, but to check that doc is correct based on the code
- unittest for actually testing the code, the goal is to thoroughly test every case, rather than illustrate what is does by example

---
### Doctest and Unittest 

Unittest Suite
- if you use both unittest and doctest for testing the same code in different situations
  - unittest integration in doctest useful for running the tests together
  - two classes, DocTestSuite and DocFileSuite create test suites compatible with the test-runner API of unittest
  - tests from each source collapse into a single outcome

```
import doctest
import unittest

import doctest_simple

suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(doctest_simple))
suite.addTest(doctest.DocFileSuite('doctest_in_help.rst'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```


---
<!-- .slide: data-background="url('images/lab2.jpg')" data-background-size="cover"  --> 
<!-- .slide: class="lab" -->
## Lab time!
Integrate doctest and unittest


