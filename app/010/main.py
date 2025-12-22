# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def main(n: int = 2_000_000):
	i = 0
	is_prime = [True for i in range(n)]
	is_prime[0] = False
	is_prime[1] = False
	for i in range(int(n**0.5)):
		if not is_prime[i]:
			continue
		for j in range(i * i, n, i):
			is_prime[j] = False
	s = 0
	for i in range(n):
		if is_prime[i]:
			s += i
	return s
