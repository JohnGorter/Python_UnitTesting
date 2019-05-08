def testfunc():
    assert 1 == 1

def test_john():
    print("john 1")
    assert 2 == 2

def test_john_more():
    print("jo")
    assert 1 == 1 


# pytest -k "john" -v