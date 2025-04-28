"""
--- Spaces
U+0020	 
U+00A0	 
U+180E	᠎
U+2000	 
U+2001	 
U+2002	 
U+2003	 
U+2004	 
U+2005	 
U+2006	 
U+2007	 
U+2008	 
U+2009	 
U+200A	 
U+202F	 
U+205F	 
U+3000	　


--- Periods
U+200B	.  -
U+FEFF	.  ---
U+002E  .  space
"""

import time
import sys

def main():
	# Define variables
	encodeSourceChar = " "
	a0 = " "
	a1 = " "
	
	# Input Source
	source = input("Please gimme some source text:")
	print(source)
	time.sleep(0.3)

	# Add text to add (encode)
	add = input("Please gimme some text to add:")
	print(add)
	time.sleep(0.3)
	
	# Using join() + ord() + format()
	# Converting String to binary 	   (bits. 07b is lowest)
	resBinary = ''.join(format(ord(i), '08b') for i in add)
	
	# printing result
	resBinaryStr = str(resBinary)
	print("The string after binary conversion : " + resBinaryStr)
	time.sleep(0.3)
	
	# Count 0's and 1's and convert to String.
	spacesNeeded = len(resBinaryStr)
	print("Spaces needed to fit binary into: " + str(spacesNeeded))
	time.sleep(0.3)

	# Count spaces available.
	# Counter
	count = 0
	spacesAvailable = 0
	 
	# Loop for search each index
	for i in range(0, len(source)):
     
	    # Check each char
	    # is blank or not
	    if source[i] == " ":
	        count += 1
	        spacesAvailable = count
	
	print("Number of spaces available: " + str(spacesAvailable))
	if spacesAvailable >= spacesNeeded:
		print("Enough spaces. Continue coding.")
		time.sleep(0.3)

	if spacesAvailable < spacesNeeded:
		print("Not enough spaces. Restarting...")
		time.sleep(0.3)
		main()

	# Define/Reset count
	count = 0
	count0 = 0
	count1 = 0

	sourceList = list(source)
	print(sourceList)

	addList = list(resBinary)
	print(addList)

	addListLen = int(len(addList))
	print("addListLen is " + str(addListLen) + " characters/entries long.")

	for j in range(len(addList)):
		if addList[j] == '0':
			addList[j] = ' '
			count0 += 1
		if addList[j] == '1':
			addList[j] = ' '
			count1 += 1
	print("Count0: " + str(count0) + " + Count1: " + str(count1))
	print(str(addList))

	# Reset counts
	count = 0
	count0 = 0
	count1 = 0
	countK = 0
	countL = 0


	destList = sourceList

	for k in range(len(destList)):
		if countK == len(addList):
			break
		if destList[k] == ' ':
			destList[k] = addList[countK]
			# Debug: print(str(destList))
			countK += 1
			countL += 1
			
	print(str(destList))
	destListStr = str(destList)
	destListStr = destListStr.replace("', '","")
	destListStr = destListStr.replace("['","")
	destListStr = destListStr.replace("']","")
	destListStr = destListStr.replace("\xa0"," ")
#Dit stuk?
	with open('readme.txt', 'w') as f:
		f.write(str(destListStr))
		f.close()
	sys.stdout.write(destListStr)

	input("Press enter to exit;")

if __name__ == "__main__":
    main()

main()
