# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?


def gcd(a: int, b: int):
	r = a % b
	while r != 0:
		a, b = b, r
		r = a % b
	return b


def main(n: int = 20):
	lcm = 1
	for i in range(2, n + 1):
		lcm = (lcm * i) // gcd(lcm, i)
	return lcm
