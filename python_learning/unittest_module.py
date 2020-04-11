# documentation website: https://docs.python.org/3/library/unittest.html

# short description of what unittest does
'''
it supports:
- test automation
- sharing of setup and shutdown code for tests
- aggregation of tests into collections
- independence of the tests from the reporting framework

important concepts:
- test fixture
- test case
- test suite
- test runner 

'''

# using corey schafer's tutorial
def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if y == 0:
		raise ValueError('Cannot divide by zero!')
	return x / y

print(add(10, 5))

# but you have no clear idea to see what failed and what succeeded

# for a test.py file, naming convention is "test_.....py"
# when naming tests, they MUST start with "test_"

import unittest

# first make a class
# inherit from unittest.TestCase
class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(add(10, 5), 15)
		self.assertEqual(add(-1, 1), 0)
		self.assertEqual(add(-1, -1), -2)

	def test_subtract(self):
		self.assertEqual(subtract(10, 5), 5)
		self.assertEqual(subtract(-1, 1), -2)
		self.assertEqual(subtract(-1, -1), 0)

	def test_multiply(self):
		self.assertEqual(multiply(10, 5), 50)
		self.assertEqual(multiply(-1, 1), -1)
		self.assertEqual(multiply(-1, -1), 1)

	def test_divide(self):
		self.assertEqual(divide(10, 5), 2)
		self.assertEqual(divide(-1, 1), -1)
		self.assertEqual(divide(-1, -1), 1)
		self.assertEqual(divide(3, 4), 0.75) # tests if using floor or normal division!

# use of context manager when testing exceptions
		with self.assertRaises(ValueError):
			divide(10, 0)

if __name__ == '__main__':
	unittest.main()

# if many tests
# use setup and teardown methods
# helps keep the code dry

def setUp(self): # runs code before every single test (defined function)
	pass

def tearDown(self): # runs code after every single test (defined function, basically)
	pass

# need to review OOP stuff

# now need to find method to count number of tables
# assertEqual 
# then add another test for table names

BREAK TIME brb 




