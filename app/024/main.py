# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.


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


def main(n: int = 28123):
	primes = [2, 3, 5, 7]
	abundant: list[int] = []
	for i in range(2, n):
		if sum_of_factors(i, primes) > i:
			abundant.append(i)
	lookup = set(abundant)
	s = 0
	for i in range(1, n + 1):
		for a in abundant:
			if (i - a) in lookup:
				break
		else:
			s += i
	return s
