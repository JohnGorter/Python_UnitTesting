from unittest.mock import patch

class SomeClass:
    attribute = 10

class sentinel:
    attribute = 100

original = SomeClass.attribute
@patch.object(SomeClass, 'attribute', sentinel.attribute)
def test():
    assert SomeClass.attribute == sentinel.attribute

test()
assert SomeClass.attribute == original