# 1 Jan 1900 was a Monday.
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?


# 1 Jan 1900 was a Monday.
# 31 Dec 1900 was a Monday.
# 1 Jan 1901 was a Tuesday.

days = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def get_days_in_month(mm: int, yyyy: int) -> int:
	if v := days[mm]:
		return v
	if yyyy % 100 == 0 and yyyy % 400 == 0:
		return 29
	elif yyyy % 4 == 0:
		return 29
	else:
		return 28


def main():
	day = 2
	count = 0
	for y in range(1901, 2001):
		for m in range(12):
			day = (day + get_days_in_month(m, y)) % 7
			if day == 0:
				count += 1
	return count
