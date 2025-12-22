# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 * 99. Find the largest palindrome made from the product
# of two 3-digit numbers.


def is_palindrome(original: int):
	y = 0
	x = original
	while x != 0:
		y = y * 10 + x % 10
		x = x // 10
	return original == y


def main(n: int = 3):
	mx = 0
	lb, up = 10 ** (n - 1) - 1, 10**n - 1
	for i in range(up, lb, -1):
		for j in range(up, i - 1, -1):
			x = i * j
			if x < mx:
				break
			if is_palindrome(x):
				mx = x
	return mx
