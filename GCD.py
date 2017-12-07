'''
Coder: Jacky Shew
Description: Calculates the GCD Greatest Common Denominator (with gcd library import)

Input: List of integers until input 0.
'''

from fractions import gcd
import sys

while True:
	numbers_gcd = input()
	if len(numbers_gcd) == 1 and numbers_gcd == 0 or len(numbers_gcd) == 1 and numbers_gcd == '0' :
		sys.exit()
	list_gcd = (' '.join(numbers_gcd.split())).split()
	x = int(list_gcd[0])
	for i in list_gcd[1::]:
		x = gcd(x, int(i))
	print('The gcd of the integers is ', abs(x),'.',sep='')