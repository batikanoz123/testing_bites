from lib.high_value import *

def test_first_highest():
    high_value = HighValue(2,1)
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_second_highest():
    high_value = HighValue(1,2)
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_values_equal():
    high_value = HighValue(2,2)
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_increase_first_by():
    high_value = HighValue(1,2)
    high_value.add(2, "first")
    result = high_value.get_highest()
    assert result == "First value is higher"
    
def test_increase_second_by():
    high_value = HighValue(2,1)
    high_value.add(2, "second")
    result = high_value.get_highest()
    assert result == "Second value is higher"