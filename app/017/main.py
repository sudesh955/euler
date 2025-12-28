# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all
# the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance with
# British usage.

from typing import Optional


numbers = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
	100: "hundred",
	1000: "thousand",
}


def words(x: int, parts: Optional[list[str]] = None) -> list[str]:
	if parts is None:
		parts = []
	if x < 1:
		raise ValueError(x)
	if x <= 20:
		parts.append(numbers[x])
	elif x < 100:
		r = x % 10
		y = x - r
		if r == 0:
			parts.append(numbers[x])
		else:
			parts.append(numbers[y])
			parts.append(numbers[r])
	elif x <= 999:
		r = x % 100
		if r == 0:
			parts.append(numbers[x // 100])
			parts.append(numbers[100])
		else:
			parts.append(numbers[x // 100])
			parts.append(numbers[100])
			parts.append("and")
			words(x % 100, parts)
	elif x == 1000:
		parts.append(numbers[1])
		parts.append(numbers[1000])
	else:
		raise ValueError(x)
	return parts


def main(n: int = 1000):
	s = 0
	for i in range(1, n + 1):
		for w in words(i):
			s += len(w)
	return s
