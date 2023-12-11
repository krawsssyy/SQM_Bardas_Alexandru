import unittest
from ModularMath import *
class UnitTest2(unittest.TestCase):
	def test_exp_inv(self):
		m = ModularMath(11)
		self.assertEqual(m.get_m(), 11)
		self.assertEqual(m.exp(11, 2), 0)
		self.assertEqual(m.exp(10, 2), 1)
		self.assertEqual(m.exp(9, 3), 3)
		self.assertEqual(m.inv(2), 6)
		self.assertEqual(m.inv(9), 5)
		self.assertEqual(m.inv(14), 4)
		m = ModularMath(10)
		with self.assertRaises(ValueError):
			m.inv(2)
		self.assertEqual(m.get_m(), 10)
		self.assertEqual(m.inv(3), 7)

if __name__ == "__main__":
	unittest.main()