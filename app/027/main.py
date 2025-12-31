# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive
# integer values 0 <= n <= 39. However,
# when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
# primes for the consecutive values 0 <= n <= 79. The product of the
# coefficients, -79 and 1601, is -126479.
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000
# where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4$
# Find the product of the coefficients a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0

primes = set()


def is_prime(n: int):
	if abs(n) < 2:
		return False
	if n in primes:
		return True
	mx = int(n**0.5)
	for i in range(2, mx + 1):
		if n % i == 0:
			return False
	primes.add(n)
	return True


def main():
	# a^2 - 4b < 0 => b > a^2 / 4
	mx = 0
	selected = (0, 0)
	for a in range(-1000, 1001):
		mn = int(a * a / 4)
		for b in range(mn, 1000):
			n = 0
			while is_prime(n * n + a * n + b):
				n += 1
			if n > mx:
				mx = n
				selected = a, b
	return selected[0] * selected[1]
