import unittest
from ModularMath import *
class UnitTest0(unittest.TestCase):
	def test_add_sub(self):
		m = ModularMath(10)
		self.assertEqual(m.get_m(), 10)
		self.assertEqual(m.add(1, 3), 4)
		self.assertEqual(m.add(7, 7), 4)
		self.assertEqual(m.add(10, 100), 0)
		self.assertEqual(m.add(-3, -2), 5)
		self.assertEqual(m.sub(15, 19), 6)
		self.assertEqual(m.sub(10, 10), 0)
		self.assertEqual(m.sub(19, 7), 2)
		m = ModularMath(19)
		self.assertEqual(m.get_m(), 19)
		self.assertEqual(m.add(19, 38), 0)
		self.assertEqual(m.sub(19, 38), 0)

if __name__ == "__main__":
	unittest.main()