import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("C:\\Users\\User\\Desktop\\Simple_calculater\\tests\\test_hypothesis.py"))))

import hypothesis
from hypothesis import given, strategies as st, assume
from main import add, subtract, division, multiplication, power, square_root

@given(st.integers(),st.integers())

def test_add_hypothesis(a,b):
    result = add(a,b)
    assert isinstance(result,int)
    assert result == a+b

@given(st.integers(),st.integers())
def test_add_hypothesis(a,b):
    result = subtract(a,b)
    assert isinstance(result,int)
    assert result == a-b

@given(st.integers(),st.integers())
def test_multiplication(a,b):
    result = multiplication(a,b)
    assume(a!=0)
    assert isinstance(result,int)
    assert result == a*b

@given(st.integers(),st.integers().filter(lambda x: x!=0))
def test_division_hypothesis(a,b):
    result = division(a,b)
    assume(a!=0)
    assert isinstance(result,(int,float))
    assert result == a/b

@given(st.integers(),st.floats().filter(lambda x: x!=0))
def test_division_hypothesis_Nenorm(a,b):
    result = division(a,b)
    assume(a!=0)
    assert isinstance(result,(int,float))
    assert result == a/b

@given(st.integers(), st.integers)
def test_power(a,b):
    result = power(a,b)
    assert isinstance(result,int)
    assert result == a**b