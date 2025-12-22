# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that
# the 6th prime is 13.
# What is the 10001st prime number?


def is_prime(n: int, primes: list[int]):
	sqrt = int(n**0.5 + 1)
	for p in primes:
		if p > sqrt:
			return True
		if n % p == 0:
			return False
	return True


def main(n: int = 10001):
	i = 5
	count = 3
	primes = [2, 3, 5]
	while count != n:
		i += 1
		if is_prime(i, primes):
			primes.append(i)
			count += 1
	return primes[-1]
