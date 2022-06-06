import statistics 
import math 

class Calculator():
	"""Calculator"""
	
	def add(self, *args):
		return sum(args)

	def sub(self, x, y):
		return x - y

	def multi(self, x, y):
		return x * y

	def division(self, x, y):
		if y == 0:
			return None
		return x / y

	def is_even(self, x):
		if x % 2 == 0:
			return True 
		return False 

	def divisors(self, x):
		divisors = []
		for i in range(1,x + 1):
			if x % i == 0:
				divisors.append(i)
		return divisors

	def cosine(self, x):
		return math.cos(x)

	def average(self, nums):
		return statistics.mean(nums)

	def is_prime(self, num):
		return False if num < 2 or [False for x in range(2, int(math.sqrt(num))+1) if num % x == 0] else True

if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(3,3))
	print(calc.sub(3,3))
	print(calc.multi(3, 3))
	print(calc.cosine(0))
	print(calc.cosine(270))
	print(calc.average([3, 3, 4, 10]))
	print ("Prime")
	print(calc.is_prime(5))
	print(calc.is_prime(7))
	print(calc.is_prime(10))