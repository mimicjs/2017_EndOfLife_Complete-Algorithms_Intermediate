'''
Coder: Jacky Shew
Description: Evaluates expressions with only '*' and '+' such that
			 it obtains the largest possible result.

Objective: Use Dynamic Programming

Input: Starts off with number of evaluations
	   Remember to include spaces

Input example: 
3
5 + 5 * 10 * 139 + 393
4 + 2 * 140
29 * 92 * 10 + 49 * 1094
'''

def find_min_max(minimum_mat, maximum_mat, p, q, operators):
	min_value = 2**(63-1)
	max_value = -(2**63)
	for r in range(p, q):
		a = maximum_mat[p][r]
		b = minimum_mat[p][r]
		x = maximum_mat[r+1][q]
		y = minimum_mat[r+1][q]
		if operators[r] == '+':
			l = a+x
			m = a+y
			n = b+x 
			o = b+y
		else:
			l = a*x
			m = a*y 
			n = b*x 
			o = b*y
		min_value = min(min_value, l, m, n, o)
		max_value = max(max_value, l, m, n, o)
	return min_value, max_value

#Program starts here
for j in range(int(input())): #Takes input
	equation = input().split() #Takes the expression
	operands = equation[::2]
	operators = equation[1::2]
	minimum_mat = []
	maximum_mat = []
	for i in range(len(operands)):
		minimum_mat.append([])
		maximum_mat.append([])
		for j in range(len(operands)):
			if i != j:
				minimum_mat[i].append(0)
				maximum_mat[i].append(0)
			else: 
				minimum_mat[i].append(int(operands[i]))
				maximum_mat[i].append(int(operands[i]))
	for i in range(1, len(operands)):
		for j in range(len(operands) - i):
			k = i + j
			minimum_mat[j][k], maximum_mat[j][k] = find_min_max(minimum_mat, maximum_mat, j, k, operators) #Function is called on this line
	print(maximum_mat[0][len(operands)-1])
