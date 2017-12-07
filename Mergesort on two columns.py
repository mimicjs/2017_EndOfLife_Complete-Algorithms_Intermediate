'''
Coder: Jacky Shew
Description: Sort two columns of integers with Mergesort O(n log n)

Input syntax: First line: Total no. of Rows. Following lines: 2 Integers separated by a space.

Input example:
3
7 2
2 7
2 4
'''

def merge_sort(seq):
	if len(seq) < 2:
		return seq
	m = int(len(seq) / 2)
	return merge(merge_sort(seq[:m]), merge_sort(seq[m:]))

def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if int(left[i][0]) == int(right[j][0]):
			if int(left[i][1]) < int(right[j][1]):
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		elif int(left[i][0]) < int(right[j][0]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def get_seq():
	for i in range(int(input())):
		seq.append(input().split())

seq = []
get_seq()
seq = merge_sort(seq)
for i in seq:
	print(i[0]+' '+i[1])