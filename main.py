def testnumber(int):
	index = 2
	while index <= int:
		rem = int % index
		print(str(int) + " " + str(index) + " " + str(rem))
		if rem > 0:
			index += 1
		if int == index and rem == 0:
			print("Number is Prime")
			break
		if index < int and rem == 0:
			break
testnumber(input("num"))

