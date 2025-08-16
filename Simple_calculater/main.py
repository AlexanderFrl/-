#Создаю набор колькулиционных функций
import math

def add(a,b):
    return  a + b

def subtract(a,b):
    return  a - b

def multiplication(a,b):
    return a * b

def division (a, b):
    if b == 0: #На ноль делить нельзя
        raise ValueError("Cannot divibe by zero")
    return  a / b

def area(a,b):
    if a < 0 or b < 0:
        raise ValueError("S не может быть отрицательной")
    return a * b
    
 
def add3(a,b,c):
    return a + b + c
    
def power(a,b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError("Не может быть меньше нуля")
    return a ** 0.5  

def factorial(n):
    if n < 0:
        raise ValueError("Не может быть отрицательным")
    return math.factorial(n)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.cos(math.radians(x))

def log(a,base=math.e):
    if a <=0:
        raise ValueError("Logarithm не может быть отрицателен или равен нулю")
    return math.log(a,base)

def percent(value,percent):
    return value * (percent/100)