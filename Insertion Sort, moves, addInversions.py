'''
Coder: Jacky Shew
Description: Insertion Sort, outputs sorted list, additional inversions

Input: First line: Total no. of Integers. Following lines: Integers
Outputs: Sorted list of integers, no. of Moves, additional inversions

Input example:
3
7
1
2
'''

def begin():
	number = int(input())
	seq = []
	moves = 0
	inversions = int(((number-1)*number)/2)
	for i in range(number):
		next = int(input())
		seq.append(next)
		element = seq[i]
		j = i
		while (j > 0 and seq[j-1] > element):
			seq[j] = seq[j-1]
			j = j - 1
			moves += 1
		seq[j] = element
	inversions -= moves
	return seq,moves,inversions

sorted_sequence,moves,inversions = begin()
print(*sorted_sequence, sep='\n')
print("moves:", moves, sep='')
print("additionalinversions:", inversions, sep='')