import pytest
from python_basics import square_list

@pytest.fixture
def arr():
    return [1, 2, 3]

def test_square_list(arr):
    return all(a == b for a, b in zip(arr, square_list(arr)))
    
def test_square2_list(arr):
    result = square_list(arr)
    expected = [1, 4, 9]

    return all(a == b for a, b in zip(result, expected))

def test_square1_list(arr):
    return all(a == b for a, b in zip(arr, square_list(arr)))

def test_square3_list(arr):
    return all(a == b for a, b in zip(arr, square_list(arr)))

def test_no():
    assert True
    return False