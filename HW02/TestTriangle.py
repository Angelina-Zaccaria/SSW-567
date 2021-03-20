# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from math import sqrt

from triangle_classification import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_invalidInputA(self):
        self.assertEqual(classify_triangle("a",4,5),"InvalidInput")
    def test_invalidInputB(self):
        self.assertEqual(classify_triangle(3,"b",5),"InvalidInput")
    def test_invalidInputC(self):
        self.assertEqual(classify_triangle(3,4,"c"),"InvalidInput")
    def test_invalidInputD(self):
        self.assertEqual(classify_triangle(199,210,150),"InvalidInput")
    def test_InvalidInputNeg(self):
        self.assertEqual(classify_triangle(-1,7,9),"InvalidInput")
    def test_InvalidInputZero(self):
        self.assertEqual(classify_triangle(0,2,3),"InvalidInput")

    def test_equilateral(self):
        self.assertEqual(classify_triangle(1,1,1),"Equilateral")

    def test_isoscelesA(self):
        self.assertEqual(classify_triangle(1,3,3),"Isosceles")
    def test_isoscelesB(self):
        self.assertEqual(classify_triangle(3,1,3),"Isosceles")
    def test_isoscelesC(self):
        self.assertEqual(classify_triangle(3,3,1),"Isosceles")

    def test_notATriangleA(self):
        self.assertEqual(classify_triangle(7,3,3),"NotATriangle")
    def test_notATriangleB(self):
        self.assertEqual(classify_triangle(3,7,3),"NotATriangle")
    def test_notATriangleC(self):
        self.assertEqual(classify_triangle(3,3,7),"NotATriangle")

    def test_rightA(self):    
        self.assertEqual(classify_triangle(3,4,5),'Right')
    def test_rightB(self):     
        self.assertEqual(classify_triangle(5,3,4),'Right')
    def test_rightC(self):     
        self.assertEqual(classify_triangle(5,12,13),'Right')

    def test_rightSqrtA(self):    
        self.assertEqual(classify_triangle(2*sqrt(2),2,2),"Right")
    def test_rightSqrtB(self):     
        self.assertEqual(classify_triangle(5,5*sqrt(3),10),'Right')
    def test_rightSqrtC(self):             
        self.assertEqual(classify_triangle(4,4,4*sqrt(2)),"Right")

    def test_scaleneA(self):
        self.assertEqual(classify_triangle(2,3,4),"Scalene")
    def test_scaleneB(self):
        self.assertEqual(classify_triangle(7,5,3),"Scalene")
    def test_scaleneC(self):
        self.assertEqual(classify_triangle(8.2,3.2,10),"Scalene")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

