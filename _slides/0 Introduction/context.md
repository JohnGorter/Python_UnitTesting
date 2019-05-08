# Testing

---
### Why test?
Software Quality Assurance

- Is writing unit tests enough?

---
### Sorts of test
- Black box testing
  - unit testing
  - integration testing
  - System testing
- White Box testing
  - API testing
  - Mutation testing
  - Core coverage
- Performance testing
  - Load testing
  - Stress testing
...


---
### Sorts of test (3)
- Unit test
  - test that checks a small bit of code, in isolation of the rest of the system. 
- Integration test
  - test that checks a larger bit of the code, maybe several classes, or a subsystem 
  - it’s a label used for some test larger than a unit test, but smaller than a system test
- System test (end-to-end)
  - test that checks all of the system under test in an environment as close to the end-user environment as possible
- Functional test
  - test that checks a single bit of functionality of a system
- Subcutaneous test 
  - test that doesn’t run against the final end-user interface, but against an interface just below the surface]


---
### Unit testing
- enable completely modular code development
- to test an entire system as a whole, many different parts could fail 
-  may be difficult to locate the responsible code

- unit testing tests a subset of your larger system
- much easier to detect bugs in a small amount of code

- unit tests are not an afterthought! 
- intended to be an integral part of the development process


---
### Test Concepts

test fixture
  - represents the preparation needed to perform on tests and cleanup actions
  - for example, creating temporary databases, directories, or starting a server process

test case
  - the individual unit of testing
  - checks for a specific response to a particular set of inputs
  - unittest provides a base class, TestCase, to create new test cases

---
### Test Concepts (2)

test suite
  - a collection of test cases, test suites, or both
  - used to aggregate tests that should be executed together

test runner
  - a component which orchestrates the execution of tests 
  - provides the outcome to the user 
  - indicates the results of executing the tests

---
### Test Frameworks
Frameworks contain test api, test runners and test reporters

Populair test frameworks
- doctest
  - Python example testrunner Python standard library
- unittest
  - test runner in Python standard library
- nose or nose2
- pytest