class ModularMath:
	def __init__(self, modul):
		self._m = modul

	def add(self, a, b):
		return (a + b) % self._m

	def sub(self, a, b):
		return (a - b) % self._m

	def mul(self, a, b):
		return (a * b) % self._m

	def div(self, a,b):
		return (a // b) % self._m

	def exp(self, a, b):
		return (a ** b) % self._m

	def inv(self, a):
		return pow(a, -1, self._m)

	def get_m(self):
		return self._m
