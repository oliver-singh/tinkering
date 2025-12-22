from app.utils import add


def test_positive_add():
    assert add(2, 3) == 5

def test_negative_add():
    assert add(-1, -1) == -2

def test_zero_add():
    assert add(0, 5) == 5
