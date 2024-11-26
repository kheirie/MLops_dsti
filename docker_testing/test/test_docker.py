import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from mul import *

def test_answer():
    assert func(3) == 6
    assert func(2) == 4