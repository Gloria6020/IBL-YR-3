


"""
    The function tests the validity of IPv4 addresses using the validate function from the numb3rs
    module.
    """
from numb3rs import validate
    
def test_valid_ipv4_addresses():
    assert validate('192.168.0.1') == True
    assert validate('10.0.0.1') == True
    assert validate('172.16.0.1') == True
    assert validate('255.255.255.255') == True

def test_invalid_ipv4_addresses():
    assert validate('192.168.0') == False
    assert validate('192.168.0.256') == False
    assert validate('192.168.0.1.2') == False
    assert validate('192.168.-1.1') == False
    assert validate('192.168.0.01')== False