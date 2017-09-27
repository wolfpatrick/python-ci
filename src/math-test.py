import unittest
from math import Math

class MathTest(unittest.TestCase):
	def test_addition(self):
	# Make test fail
		self.assertEqual(Math.addition(3, 1), 7)