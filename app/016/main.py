# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000


def multiply_by_2(num: list[int]):
	carry = 0
	for i, it in enumerate(num):
		s = it * 2 + carry
		num[i] = s % 10
		carry = s // 10
	assert carry < 10
	if carry != 0:
		num.append(carry)


def main(n: int = 1000):
	num = [1]
	for _ in range(n):
		multiply_by_2(num)
	s = 0
	for x in num:
		s += x
	return s
