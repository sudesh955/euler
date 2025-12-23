# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 if n is even
# n -> 3n + 1 if n is odd
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at $13$ and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# Note: Once the chain starts the terms are allowed to go above one million.


def coltaz_with_cache(x: int, cache: dict[int, int] = {1: 1}):
	items: list[int] = []
	while x not in cache:
		items.append(x)
		if x % 2 == 0:
			x = x // 2
		else:
			x = 3 * x + 1
	y = cache[x]
	for it in reversed(items):
		y += 1
		if it < 1_000_000:
			cache[it] = y
	return y


def coltaz(x: int):
	y = 1
	while x != 1:
		if x % 2 == 0:
			x = x // 2
		else:
			x = 3 * x + 1
		y += 1
	return y


def main(n: int = 1_000_000):
	mx, start = 0, 0
	cache: dict[int, int] = {1: 1}
	for i in range((n - 2) // 2, n):  # coltaz(2n) > coltaz(n)
		# value = coltaz(i)
		value = coltaz_with_cache(i, cache)
		if value > mx:
			mx = value
			start = i
	return start
