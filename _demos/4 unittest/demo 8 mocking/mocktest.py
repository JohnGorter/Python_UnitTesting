from unittest.mock import Mock, MagicMock

class ProductionClass:
    def closer(self, something):
        something.close()

real = ProductionClass()
mock = Mock()
real.closer(mock)
mock.close.assert_called_with()  # make assertions on the called methods

mock = MagicMock(name='foo')
print(mock)
print(mock.method)
print(mock.john)

mock.john()
mock.john.assert_called()