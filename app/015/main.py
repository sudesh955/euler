# Starting in the top left corner of a 2x2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

from functools import cache


def main(n: int = 20):
	@cache
	def move(x: int, y: int) -> int:
		if x == n and y == n:
			return 1
		m = 0
		if x != n:
			m += move(x + 1, y)
		if y != n:
			m += move(x, y + 1)
		return m

	return move(0, 0)
