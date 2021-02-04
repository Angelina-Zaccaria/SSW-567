import unittest
from math import isclose, sqrt

def classify_triangle(a, b, c):
    try:
        if (a + b <= c) or (b + c <= a) or (a + c <= b):
            return "not a triangle"

        if a == b == c:
            return "equilateral" #equilateral cannot be a right triangle
        elif a == b or b == c or a == c:
            output = "isosceles"
        else:
            output = "scalene"

        if isclose(a**2 + b**2, c**2, abs_tol=1e-8) or isclose(b**2 + c**2, a**2, abs_tol=1e-8) or isclose(a**2 + c**2, b**2, abs_tol=1e-8):
            output += " and right triangle"
        return output
    except:
        return "invalid input type"

def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ') = ',classify_triangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    
    def test_invalidInput(self):
        self.assertEqual(classify_triangle("a",4,5),"invalid input type")
        self.assertEqual(classify_triangle(3,"b",5),"invalid input type")
        self.assertEqual(classify_triangle(3,4,"c"),"invalid input type")

    def test_notATriangle(self):
        self.assertEqual(classify_triangle(3,3,7),"not a triangle")
        self.assertEqual(classify_triangle(3,7,3),"not a triangle")
        self.assertEqual(classify_triangle(7,3,3),"not a triangle")
        self.assertEqual(classify_triangle(0,2,3),"not a triangle")
        self.assertEqual(classify_triangle(-1,7,9),"not a triangle")

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3,3,3),"equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3,3,1),"isosceles")
        self.assertEqual(classify_triangle(3,1,3),"isosceles")
        self.assertEqual(classify_triangle(1,3,3),"isosceles")
    
    def test_isoscelesRight(self):
        self.assertEqual(classify_triangle(4,4,4*sqrt(2)),"isosceles and right triangle")
        self.assertEqual(classify_triangle(2,2*sqrt(2),2),"isosceles and right triangle")
        self.assertEqual(classify_triangle(3.3*sqrt(2),3.3,3.3),"isosceles and right triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(2,3,4),"scalene")
        self.assertEqual(classify_triangle(7,5,3),"scalene")
        self.assertEqual(classify_triangle(8.2,3.2,10),"scalene")

    def test_scaleneRight(self):    
        self.assertEqual(classify_triangle(3,4,5),'scalene and right triangle')
        self.assertEqual(classify_triangle(5,12,13),'scalene and right triangle')
        self.assertEqual(classify_triangle(5,5*sqrt(3),10),'scalene and right triangle')

if __name__ == '__main__':
    runClassifyTriangle(1,"a",3)
    runClassifyTriangle(7,3,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(2,2,1)
    runClassifyTriangle(2,3,4)
    runClassifyTriangle(5,12,13)
    
    unittest.main(exit=True) 