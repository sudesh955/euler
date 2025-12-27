# n! means n * (n - 1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the
# digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
# Find the sum of the digits in the number 100!.


def mutliply(digits: list[int], num: int):
	carry = 0
	for i, it in enumerate(digits):
		s = carry + it * num
		digits[i] = s % 10
		carry = s // 10
	while carry != 0:
		digits.append(carry % 10)
		carry = carry // 10


def main(n: int = 100):
	x = [1]
	for i in range(2, n + 1):
		mutliply(x, i)
	s = 0
	for it in x:
		s += it
	return s
