# The prime factors of 13195 are 5,7,13 and 29.
# What is the largest prime factor of the number 600851475143


def main(n: int = 600851475143):
	mx = n
	m = int(n**0.5 + 1)
	for i in range(2, m):
		if n % i == 0:
			mx = i
			while n % i == 0:
				n = n // i
	return mx
