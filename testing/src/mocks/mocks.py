from unittest.mock import Mock

def test_mock():
    mock = Mock()
    mock.x = 3
    mock.y = 4
    mock.distance.return_value = 5
    assert mock.x * mock.x + mock.y * mock.y == mock.distance() * mock.distance()
    assert mock.distance.call_count == 2
    mock.distance.assert_called_with()
    
