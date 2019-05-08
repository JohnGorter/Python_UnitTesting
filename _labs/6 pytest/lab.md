
# Lab working with PyTest

## Exercise 1. Setup

### Step 1. Write a calculator
Write or find a calculator that can add, subtract, divide and multiply. 

## Step 2.  Install PyTest and test the calculator
Install PyTest and create at least 4 tests that validate the workings of the calculator. 

## Exercise 2. Markers

### Step 1. Use markers
Write more tests over multiple files and qualify each test
using a marker given the test category (add, subtract, multiply and divide).

### Step 2. Test markers
Use PyTest to test all subtract tests but not the other tests..

### Extra exersize
Experiment with the following features
- fixtures
- parameterizing tests
- running tests in parallel



Create a new virtual environment using python -m virtualenv or python -m venv. 
More info about that here:
https://docs.python.org/3/library/venv.html

# Step 2. Practice activating and deactivating your virtual environment a few times
$ source venv/bin/activate
$ deactivate

On Windows:
C:\Users\okken\sandbox>venv\scripts\activate.bat
C:\Users\okken\sandbox>deactivate

# Step 3. Install pytest in your new virtual environment
Even if you thought you already had pytest installed, you’ll need to install it into
the virtual environment you just created

# Step 4. Create a few test files
Practice running pytest against these files.

# Step 5. Change the assert statements. 
Don’t just use assert something == something_else; try things like:
- assert 1 in [2, 3, 4]
- assert a < b
- assert ’fizz’ not in ’fizzbuzz’