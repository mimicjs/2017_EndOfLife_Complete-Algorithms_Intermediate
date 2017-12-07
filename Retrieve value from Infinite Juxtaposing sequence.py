'''
Coder: Jacky Shew
Description: Return value at an index of an infinite sequence created by 
			 juxtaposing the increasing larger sequences of incremented integers
			 e.g. 11212312341234512345612345671234567812345678912345678910
Objective: Uses Divide-and-Conquer
Input: First Line: Total no. of inputs. Following Lines: Index to retrieve value from.
'''

def find_element(find_x, seq, counter, previous_find_x):
	digits_iterated = 1
	while_counter = 1
	while find_x > digits_iterated:
		find_x -= digits_iterated
		digits_iterated += len(str(while_counter+1))
		while_counter += 1
	if previous_find_x < find_x:
		for i in range(counter, while_counter+1):
			seq += str(i)
		counter = while_counter+1
		previous_find_x = find_x
	print(seq[find_x-1])
	return seq,counter,previous_find_x

test_cases = int(input())
seq = ''
counter = 1
previous_find_x = 0
for i in range(test_cases):
	seq, counter, previous_find_x = find_element(int(input()), seq, counter, previous_find_x)