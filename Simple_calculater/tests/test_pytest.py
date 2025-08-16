import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("C:\\Users\\User\\Desktop\\Simple_calculater\\tests\\test_pytest.py"))))


import pytest
import math
from main import add,subtract,multiplication,division,area,power,sin,cos,tan,log,percent,factorial,add3, square_root



@pytest.mark.parametrize("a,b,expected",[
    (2,2,4),
    (7,-3,4),
    (-2,5,3),
    
])
def test_add_parameterized(a,b,expected):
    assert add(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[
    (10,5,5),
    (10,-5,15),
    (-10,5,-15),
    (-10,-5,-5),
])
def test_subtract(a,b,expected):
    assert subtract(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[
    (2,2,4),
    (2,-2,-4),
    (-2,-2,4),
    (2,0,0),
])

def test_multiplication(a,b,expected):
    assert multiplication(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[ 
    (10,5,2),
    (10,-5,-2),
    (-10,-5,2),
    
])
def test_division(a,b,expected):
    assert division(a,b)==expected
    try:
        division(10,0)
    except ValueError as e:
        assert str(e)=="Cannot divibe by zero"

@pytest.mark.parametrize("a,expected",[
    (4,2),
    (16,4),
    (2,1.41421),

])
def test_square_root(a, expected):
    result = square_root(a)
    assert result==pytest.approx(expected, rel=1e-4)



def test_square_root_negative():
    with pytest.raises(ValueError) as exc_info:
        square_root(-4)

    assert str(exc_info.value)=="Не может быть меньше нуля"


@pytest.mark.parametrize("x,expected", [
    (0,1),(1,1),(5,120),
])
def test_factorial(x,expected):
    result = factorial(x)
    assert result == expected

def test_factorial_negative():
    with pytest.raises(ValueError) as exc_info:
        factorial(-4)

    assert str(exc_info.value) == "Не может быть отрицательным"

@pytest.mark.parametrize("angle ,expected", [
    (math.pi/ 2,1.0),
    (-math.pi/2,-1.0),
    (0,0.0),
])
def test_sin(angle,expected):
    result = sin(angle)
    assert result == pytest.approx(expected,rel= 1.0e-4)

@pytest.mark.parametrize("angle , expected", [
    (0,1.0),
    (math.pi/2,0.0),
    (math.pi/4,pytest.approx(0.7071, rel=1e-4)),
])

def test_cos(angle, expected):
    result = cos(angle)
    assert result == pytest.approx(expected,rel=1e-4)

@pytest.mark.parametrize('angle, expected',[
    (math.pi/4, pytest.approx(1.0,rel=1e-4)),(math.pi/4,pytest.approx(-1.0,rel=1e-4)),
])
def test_tan(angle,expected):
    result=tan(angle)
    assert result == pytest.approx(expected, rel=1e-4)