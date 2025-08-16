#>Unittest проверка правильной работоспособности с 3 тестами на каждую функцию
import unittest
from main import add, subtract, multiplication, division, add3, area, power, square_root, factorial,sin,cos,tan,log,percent


#Авто на Сложение
class TestMathFunction(unittest.TestCase):
    def test_add_norm(self):
        self.assertEqual(add(2,8), 10)
        self.assertEqual(add(9 , 21), 30)
    def test_add_zero(self):
        self.assertEqual(add(0,9), 9)
        self.assertEqual(add(21, 0), 21)
    def test_add_negative(self):
        self.assertEqual(add(-7,84), 77)
        self.assertEqual(add(24, -11), 13)


 # Авто на вычитание  



    def test_subtract_norm(self):
        self.assertEqual(subtract(25, 9), 16)
        self.assertEqual(subtract(39, -61),100)
        self.assertEqual(subtract(-25, 13), -38)
        
    def test_subtract_zero(self):
        self.assertEqual(subtract(0,5),-5)
        self.assertEqual(subtract(0,-5), 5)
        self.assertEqual(subtract(13,0), 13)
        
    def test_subtract_negative(self):
        self.assertEqual(subtract(0,33), -33)
        self.assertEqual(subtract(39,-61),100)
        self.assertEqual(subtract(-25, 13), -38)
 # Авто на умножение      


    def test_multiplication_norm(self):
        self.assertEqual(multiplication(5,5),25)
        self.assertEqual(multiplication(1,17),17)
        
    def test_multiplication_zero(self):
        self.assertEqual(multiplication(1,0),0)
        self.assertEqual(multiplication(0,1),0)
        
    def test_multiplication_negative(self):
        self.assertEqual(multiplication(-4,1),-4)
        self.assertEqual(multiplication(-1,-1),1)
        self.assertEqual(multiplication(1,1),1)# тест на ошибку(пройден и исправлен)
        
#  Авто на деление      
	


    def	test_division_norm(self):
        self.assertEqual(division(10,2), 5.0)#
        with self.assertRaises(ValueError):##Применяем правило
            division(10,0)
   
        
        
    def test_division_negative(self):
        self.assertEqual(division(-25, 5), -5.0)
        with self.assertRaises(ValueError):
            division(-25,0)
        self.assertEqual(division(-33,3),-11.0)
        with self.assertRaises(ValueError):
            division(-33,0)
        self.assertEqual(division(98536, 2),49268.0)
        with self.assertRaises(ValueError):
           division(98536,0)
            

    def test_add3_norm(self):
        self.assertEqual(add3(1,2,3),6)
        self.assertEqual(add3(-3,5,-2), 0)

#Авто на степень
    def test_power_norm(self):
        self.assertEqual(power(1,2),1)
        self.assertEqual(power(2,2),4)
        self.assertEqual(power(2,3),8)

    def test_power_zero(self):
        self.assertEqual(power(0,4),0)
        self.assertEqual(power(3,0),1)
        self.assertEqual(power(0,0),1)

    def test_power_negative(self):
        self.assertEqual(power(-2,2),4)
        self.assertEqual(power(2,-2), 0.25)

    def test_square_root(self):
        self.assertAlmostEqual(square_root(2),1.4142,delta=0.0001)
        self.assertAlmostEqual(square_root(5), 2.230, delta=0.01)

    def test_factorial(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(3),6)

    def test_sin(self):
        self.assertAlmostEqual(sin(3),0.05, delta=0.01)
        self.assertAlmostEqual(sin(-3),-0.05, delta=0.01)

    def test_cos(self):
        self.assertAlmostEqual(cos(3),0.99,delta=0.01)
        self.assertAlmostEqual(cos(-3), 0.998, delta=0.001)

    def test_tan(self):
        self.assertAlmostEqual(tan(3),0.9986,delta=0.001)
        self.assertAlmostEqual(tan(-3),0.9986, delta=0.001)

    def test_log(self):
        self.assertAlmostEqual(log(4),1.386, delta=0.001)

    def test_percent(self):
        self.assertAlmostEqual(percent(5,10),0.5)
        self.assertEqual(percent(-5,10),-0.5)









# Проиграть все тесты       
if'__name__'=='__main__':
    unittest.main()
		