# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def main(n: int = 1000):
	n3 = (n - 1) // 3  # multiples of 3
	n5 = (n - 1) // 5  # multiples of 5
	n15 = (n - 1) // 15  # multiples of 15
	sum_n3 = 3 * n3 * (n3 + 1) // 2
	sum_n5 = 5 * n5 * (n5 + 1) // 2
	sum_n15 = 15 * n15 * (n15 + 1) // 2
	return sum_n3 + sum_n5 - sum_n15
