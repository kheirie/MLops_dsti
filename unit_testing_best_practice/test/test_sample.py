import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 

from sample import *

def test_answer():
    assert func(3) == 5