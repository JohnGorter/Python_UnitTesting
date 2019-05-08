
# Step 1. Create a virtual environment

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