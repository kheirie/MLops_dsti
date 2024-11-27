import sys
import os
# Always run from unit_testing_best_practice/test
sys.path += ['../src'] 
src_path = os.path.abspath(os.path.join("docker_testing", "src"))

if src_path not in sys.path:
    sys.path.append(src_path)

from mul import *

def test_answer():
    assert func(3) == 6
    assert func(2) == 4
    assert func(4) == 8