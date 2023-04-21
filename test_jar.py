import pytest
from jar import Jar

def test_init():
    # Test initialization with default capacity
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0
    
    # Test initialization with custom capacity
    j = Jar(8)
    assert j.capacity == 8
    assert j.size == 0
    
    # Test initialization with invalid capacity
    with pytest.raises(ValueError):
        j = Jar(-1)
    with pytest.raises(ValueError):
        j = Jar("not an int")
    
def test_str():
    # Test empty jar
    j = Jar()
    assert str(j) == ""
    
    # Test jar with cookies
    j.deposit(3)
    assert str(j) == "🍪🍪🍪"
    
def test_deposit():
    # Test valid deposit
    j = Jar(4)
    j.deposit(2)
    assert j.size == 2
    
    # Test deposit exceeding capacity
    with pytest.raises(ValueError):
        j.deposit(4)
    assert j.size == 2
    
    # Test invalid deposit
    with pytest.raises(ValueError):
        j.deposit(-1)
    assert j.size == 2
    
def test_withdraw():
    # Test valid withdrawal
    j = Jar()
    j.deposit(3)
    j.withdraw(2)
    assert j.size == 1
    
    # Test withdrawal exceeding jar size
    with pytest.raises(ValueError):
        j.withdraw(2)
    assert j.size == 1
    
    # Test invalid withdrawal
    with pytest.raises(ValueError):
        j.withdraw(-1)
    assert j.size == 1
