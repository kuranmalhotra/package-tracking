
from app.tracking_app import (
    function,
)

def test_function():
    x = "hey"
    result = function(x)
    assert result == "hey"