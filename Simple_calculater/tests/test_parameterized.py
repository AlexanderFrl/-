import unittest
from parameterized import parameterized
from main import add, area, subtract, multiplication, division,power,square_root, factorial,sin,cos,tan,log,percent



class TestMathFunction(unittest.TestCase):

    @parameterized.expand([
        ("add",add,2,3,5),
        ("add",add,3,-3,0),
        ("add",add,0,-17,-17)
       
        
    ])
    def test_operation(self,name,func,a,b,expected):
        self.assertEqual(func(a,b),expected) 



    @parameterized.expand([
        ("area",area,2,3,6),
        ("area,area_negative_a",area,7,-7,ValueError),
        ("area_negative_b", area,1,-2,ValueError)
                
    ])  
    def test_area(self,name,func,a,b,expected):
        if isinstance(expected, type) and  issubclass(expected, Exception):
            with self.assertRaises(expected):
                func(a,b)
        else:
            self.assertEqual(func(a,b),expected)
        
        
    @parameterized.expand([
        ("subtract",subtract,8,8,0),
        ("subtract",subtract,12,-8,20),
        ("subtract",subtract,-8,8,-16)
        
        ])
    def test_subtract(self,name,func,a,b,expected):
        self.assertEqual(func(a,b),expected)
        
    @parameterized.expand([
        ("multiplication",multiplication,2,2,4),
        ("multiplication",multiplication,-2,2,-4),
        ("multiplication",multiplication,-2,-2,4)
     ])
    def test_multiplication(self,name,func,a,b,expected):
        self.assertEqual(func(a,b),expected)
        
        
    @parameterized.expand([
        ("division",division,5,1,5),
        ("division",division,5,-1,-5),
        ("division",division,-5,-1,5)
        ])
        
    def test_division(self,name,func,a,b,expected):
        if isinstance(expected, type) and issubclass(expected, Exception):
            with self.assertRaises(expected):
                func(a,b)
        else:
            self.assertEqual(func(a,b),expected)
            
    @parameterized.expand([
        ("add",add,2,3,5),
        ("subtract",subtract,5,2,3),
        ("multiplication", multiplication,2,2,4),
        ("division",division,3,1,3),
        ("area",area,2,2,4),
        ("power",power,2,2,4),
    ])
    def test_all(self,name,func,a,b,expected):
        result = func(a,b)
        self.assertEqual(result,expected,f"Ошибка при вычисление:{result} != {expected}")
        if isinstance(expected, type) and issubclass(expected, Exception):
            with self.assertRaises(expected):
                
                func(a,b)
        else:
            self.assertEqual(func(a,b),expected)   

    @parameterized.expand([
        ("square_root",square_root,4,2.0),
        ("square_root",square_root,9,3.0),
        ("square_root",square_root,2,1.4142),
    ])
    def test_square_root(self,name,func,a,expected):
       self.assertAlmostEqual(func(a),expected,delta=0.0001)

    def test_square_root2(self):
        self.assertAlmostEqual(square_root(2),1.4142,delta=0.0001)

    @parameterized.expand([
        ("add",add,(2,3),5),
        ("subtract",subtract,(6,3),3),
        ("area",area,(2,2),4),
        ("square_root",square_root,(4,),2.0,None),
        ("division", division,(5,2),2.5),
        ("multiplication",multiplication,(5,5),25),
    ])
    def test_mult(self,name,func,args,expected,delta=0.0001):
        result = func(*args)
        if isinstance(expected, type) and issubclass(expected,Exception):
            with self.assertRaises(ValueError):
                func(args)
        else:
            self.assertAlmostEqual(result,expected,delta=delta)

    @parameterized.expand([
        ("sin", sin, (3,), 0.052),
        ("cos",cos,(3,),0.9986),
        ("tan",tan,(3,),0.9986),
        ("log",log,(4,),1.386),
        ("factorial",factorial,(5,),120),
        ("percent", percent,(5,10),0.5),
    ])
    def test_trigonometria(self,name,func,args,expected,delta=0.001):
        result = func(*args)
        if isinstance(expected, type) and issubclass(expected,Exception):
            with self.assertRaises(ValueError):
                func(args)
        else:
            self.assertAlmostEqual(result,expected,delta=delta)

if'__name__'=='__main__':
    unittest.main()
#решить задачу 