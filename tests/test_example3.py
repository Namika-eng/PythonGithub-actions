import pytest

# A fixture that provides test data
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


# Function to test
def sum_numbers(numbers):
    return sum(numbers)


# Test case using the fixture
def test_sum_numbers(sample_data):
    result = sum_numbers(sample_data)
    assert result == 15
    