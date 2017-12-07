'''
Coder: Jacky Shew
Description: Heapsort. Output sorted subset of integers

Input: First Line: Total no. of Integers in list. Second Line: Subset size.
	   Following Lines: Integers in list.

Input example:
3
2
7
1
2
'''

def swap(i, j):
	seq[i], seq[j] = seq[j], seq[i]
	
def heap(finish, i):
	l = 2 * i + 1
	r = 2 * (i + 1)
	n = i
	if l < finish and seq[i] < seq[l]:
		n = l
	if r < finish and seq[n] < seq[r]:
		n = r
	if n != i:
		swap(i, n)
		heap(finish, n)

def heapsort(finish):
	start = finish // 2 - 1
	for i in range(start, -1, -1):
		heap(finish, i)
	for i in range(finish-1, 0, -1):
		swap(i, 0)
		heap(i, 0)

finish = int(input())
selective_output = int(input())
seq = []
for i in range(finish):
	seq.append(int(input()))
heapsort(finish)
for i in range(selective_output):
	print(seq[i])