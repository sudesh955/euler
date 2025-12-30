# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220
# Evaluate the sum of all the amicable numbers under 10000


def sum_of_factors(num: int, primes: list[int]):
	s = 1
	x = num
	mx = int(num**0.5) + 1
	for p in primes:
		if p > mx:
			break
		if x == 1:
			break
		if x % p != 0:
			continue
		m, n = 1, 1
		while x % p == 0:
			x = x // p
			n = n * p
			m += n
		s *= m
	if x != 1:
		s *= x + 1
		if x not in primes:
			primes.append(x)
	return s - num


def main(n: int = 10000):
	primes: list[int] = [2, 3, 5]
	d = [0 for _ in range(n)]
	for a in range(2, n):
		d[a] = sum_of_factors(a, primes)
	s = 0
	mx_safe_b = primes[-1] ** 2
	for a in range(2, n):
		b = d[a]
		if a == b:
			continue
		if b < n and d[b] == a:
			s += a
			continue
		assert b <= mx_safe_b
		if sum_of_factors(b, primes) == a:
			s += a
	return s
