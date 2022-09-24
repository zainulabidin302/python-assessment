import pytest
from python_basics import square_list

@pytest.fixture
def arr():
    return [1, 2, 3]

def test_square_list(arr):
    return all(a == b for a, b in zip(arr, square_list(arr)))
    

