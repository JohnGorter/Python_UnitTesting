### testing the order and the method calls

from unittest.mock import MagicMock, call

mock = MagicMock()
mock.john()
mock.method()
# mock.john()
mock.attribute.method(10, x=53)

print(mock.mock_calls)
mock.assert_has_calls([call.method(), call.john(), call.attribute.method(10, x=53)], False)