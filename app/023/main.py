# The Fibonacci sequence is defined by the recurrence relation:
# f(n) = f(n-1) + f(n-2) where f(1) = 1 and f(2) = 1
# What is the index of the first term in the Fibonacci sequence to contain
# digits?


def add(x: list[int], y: list[int], z: list[int]):
	xn, yn, zn = len(x), len(y), len(z)
	n = max(len(x), len(y))
	carry = 0
	for i in range(n):
		s = carry
		if i < xn:
			s += x[i]
		if i < yn:
			s += y[i]
		if i < zn:
			z[i] = s % 10
		else:
			z.append(s % 10)
		carry = s // 10
	if carry > 0:
		assert carry < 10
		z.append(carry)


def main(n: int = 1000):
	a = [1]
	b = [1]
	c = [2]
	i = 2
	while len(b) < n:
		add(a, b, c)
		a, b, c = b, c, a
		i += 1
	return i
