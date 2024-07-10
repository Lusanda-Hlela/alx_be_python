# Writing Unit Tests for a Simple Calculator Class

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  def setUp(self):
    '''Set up the SimpleCalculator instance before each test.'''
    self.calc = SimpleCalculator()
  
  def test_addition(self):
    '''Test the addition method'''
    self.assertEqual(self.calc.add(2, 3), 5)
    
    self.assertEqual(self.calc.add(-1, 1), 0)
    
    self.assertEqual(self.calc.add(5, 5), 10)
    # Add more assertions to thoroughly test the add method.
  
  def test_subtraction(self):
    '''Test the subtraction method'''
    self.assertEqual(self.calc.subtract(5, 3), 2)
    
    self.assertEqual(self.calc.subtract(-1, 1), -2)
    
    self.assertEqual(self.calc.subtract(5, 5), 0)
  
  def test_multiplication(self):
    '''Test the multiplication method'''
    self.assertEqual(self.calc.multiply(2, 3), 6)
    
    self.assertEqual(self.calc.multiply(-1, 1), -1)
    
    self.assertEqual(self.calc.multiply(5, 5), 25)
  
  def test_division(self):
    '''Test the division method'''
    self.assertEqual(self.calc.divide(10, 2), 5)
    
    self.assertEqual(self.calc.divide(-10, 2), -5)
    
    self.assertEqual(self.calc.divide(5, 0), None)
    
    self.assertEqual(self.calc.divide(5, 5), 1)
    # Add more assertions to thoroughly test the subtract method.

# Remember to write additional test methods for subtract. multiply, and divide.

if __name__ == "__main__":
  unittest.main()