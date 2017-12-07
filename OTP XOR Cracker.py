'''
Coded by: Jacky Shew

Line 46 and 52 need reviewing
However I won't be continuing as this program has already served its purpose
'''

import binascii #Program needs this

#################################################
#	       The XOR/OTP Cipher should only       # 
#      consist of 13 Hexadecimals each line     #
#################################################

#Insert your One Time Pad inbetween Brackets ([])

pad = [
"F852126DB3BB782B7CC6D652259616DA5EA19ED85A61E97FC383",\
"E4480D28BFBA686563DAC0053FC542C55EED819D587BE96AD483",\
"EF525F71B3A03D6079C7CE0521DE0D9248E982C91967E46EDD92",\
"ED511A6DFCB4692B78C6DA4076D9109259E4CDDE5866EB63C483",\
"E6520C7CFCBA7B2B63C0DC0535DF16CB1BE89E9D5C7EFC7FC983",\
"FF551A28AABC787C37C1CA0533CE16C05AEE9FD9507DED79C983",\
"E3580D6DFCA1756E65CD994424D342DC54A19ECD5077E979C383"
]

#For each line, put speech marks or apostrophes to convert into string
#Separate each line with a comma (,) 
#OPTIONAL: Separate each line with a backslash (/) and press Enter

#Last column is not a letter
#Last column probably is Full Stops, Question Marks, etc...

#XOR Cipher cannot be cracked if length()

####################################################
#        PUT THE PROGRAM IN AN EMPTY FOLDER        #
#           MAY CREATE A LOT OF TEXTFILES          #
####################################################

#You may now Start the Program

column_move = 0 #Initialising Variable for Column
letter_count = 0 #Initialising Variable for Alphabetical Letter
first_column = True
while column_move!= 26: #
						# Needs to be 27 so it'll also go over the last column
						#
	first,second = 0+column_move*2,1+column_move*2 #Chained for easier change
	column_hex = pad[0][first]+pad[0][second] #Column Hex looping
	text_file = open(str(column_move+1)+". "+column_hex+"'s Output File.txt", "w") #Saves File with Corresponding Hex
	while letter_count !=26: #
							 # Needs to be a higher count due to additional punctuation marks and full stop
							 #
		cap_letter_hex = [41,42,43,44,45,46,47,48,49,'4A','4B','4C','4D','4E','4F',\
						  50,51,52,53,54,55,56,57,58,59,'5A'] #Hex Code for Capital Letters in Alphabetical Order
		lower_letter_hex = [20,61,62,63,64,65,66,67,68,69,'6A','6B','6C','6D',\
							'6E','6F',70,71,72,73,74,75,76,77,78,79,'7A','2E',21,'3F'] #Hex Code for Space + Lowercase Letters in Alphabetical Order + Ending Punctuation
		if first_column == True: 
			key = ((int('0x'+column_hex,16) ^ (int('0x'+str(cap_letter_hex[0+letter_count]),16)))) #Generated Key from XOR
		else:
			key = ((int('0x'+column_hex,16) ^ (int('0x'+str(lower_letter_hex[0+letter_count]),16)))) #Generated Key from XOR
		for i in pad:
			character = chr(int('0x'+i[first]+i[second],16) ^ key) #Takes Key, Cipher XOR with Key
			if character not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .?!":
				character = character + " DELETE "*2 #Yes I'm lazy
			#text_file.write(i[first]+i[second]+' could be: '+character+'\n') #Cipher Hex could be: Potential Character
			#
			text_file.write(":"+character+'\n') #Cipher Hex could be: Potential Character
			#								 #Will only print Potential Character (Either use this or Above not Both)
		#text_file.write("\n-------------------SEPARATOR-------------------\n\n") #Separator for New Potential Letter
		#
		text_file.write("\n-----\n\n") #Separator for New Potential Letter
		#								#Here's a smaller Separator better for 'only print Potential Character version'
		letter_count += 1 #Continue While Loop for Alphabetical Letter Descending
	first_column = False
	letter_count = 0 #Reset Letter Count for Next Column
	column_move += 1 #Continue While Loop for Column
	text_file.close()
text_file.close()
text_file = open("28. END.txt", "w")
text_file.write('Most likely...\n\nFullstops\nQuestion Marks\nExclamation Marks\n\netc...')
text_file.close()
text_file = open("0. Readme.txt", "w")
text_file.write("Now that the program has finished\nIt is time you use the Process of Elimination\
				 \n\nSpaces may have DELETE notice but may potentially be correct thus don't delete\n\
				 \nGood Luck\n-Jacky")
text_file.close()