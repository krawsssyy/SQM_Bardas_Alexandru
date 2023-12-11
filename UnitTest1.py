import unittest
from ModularMath import *
class UnitTest1(unittest.TestCase):
	def test_mul_div(self):
		m = ModularMath(11)
		self.assertEqual(m.get_m(), 11)
		self.assertEqual(m.mul(11, 2), 0)
		self.assertEqual(m.mul(3, 4), 1)
		self.assertEqual(m.mul(4, 5), 9)
		self.assertEqual(m.div(15, 5), 3)
		self.assertEqual(m.div(16, 5), 3)
		self.assertEqual(m.div(36, 3), 1)
		m = ModularMath(15)
		self.assertEqual(m.get_m(), 15)
		self.assertEqual(m.mul(15, 3), 0)
		self.assertEqual(m.mul(19, 2), 8)
		self.assertEqual(m.mul(7, 2), 14)
		self.assertEqual(m.div(150, 10), 0)
		self.assertEqual(m.div(10, 3), 3)
		self.assertEqual(m.div(100, 3), 3)

if __name__ == "__main__":
	unittest.main()