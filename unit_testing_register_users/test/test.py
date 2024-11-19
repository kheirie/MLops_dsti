# run in terminal pytest -s test.py  to capture inputs
import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

import re

from registerusers import *

def test_validate_username():
    assert validate_username("validusername") is True
    assert validate_username("") is False
    assert validate_username("invalid username") is False

def test_validate_password():
    assert validate_password("P@ssw0rd123") is True
    assert validate_password("short") is False
    assert validate_password("Password123") is False  
    assert validate_password("12345678") is False  

def test_validate_email():
    assert validate_email("user@example.com") is True
    assert validate_email("userexample.com") is False 
    assert validate_email("user@.com") is False 
    assert validate_email("@example.com") is False  