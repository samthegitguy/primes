def testnumber(int, printdata):
	index = 2
	if printdata == False:
		print("Please wait(this may take 5-10 minutes based on the input number and your computer specifications.")
	if int == 1 or int == 0:
		print("Srsly?")
	while index <= int:
		if int % 2 > 0:
			if index % 2 > 0:
				rem = int % index
				if printdata == True:
					print(str(int) + " " + str(index) + " " + str(rem))
				if rem > 0:
					index += 1
				if int == index and rem == 0:
					print("Number is Prime")
					break
				if index < int and rem == 0:
					print("Number is composite")
					break
			else: index +=1
		else:
			print("Number is an even number, what were you thinking????")
			break
while True:
	rawinputdebug = raw_input("Want to display debugging data? ").lower()
	if rawinputdebug == "yes":
		printdata = True
		break
	elif rawinputdebug == "no":
		printdata = False
		break
	else:
		print("Please enter a valid Yes Or No answer")
testnumber(input("What number are we checking today?"), printdata)

