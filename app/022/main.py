# Using `names.txt` a text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical
# value for each name, multiply this value by its alphabetical position in the
# list to obtain a name score. For example, when the list is sorted into
# alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938 name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
# What is the total of all the name scores in the file

score = {ch: i for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}


def get_score(name: str):
	s = 0
	for ch in name:
		s += score.get(ch, 0)
	return s


def main():
	with open("app/022/names.txt") as f:
		text = f.read()
	names = text.strip().split(",")
	names = [it[1:-1].upper() for it in names]
	names.sort()
	s = 0
	for i, it in enumerate(names, 1):
		s += i * get_score(it)
	return s
