def ootifier(ootinput, oot):
	vowels_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
	new_string = []
	string_list = list(ootinput)

	for char in string_list:
		for char2 in vowels_list:
			if char == char2:
				new_string.append(oot)
				break
		else:
			new_string.append(char)

	return(''.join(new_string))




input_str = input('ENTER PHRASE TO BE OOTIFIED: ')

oot = 'oot'

print()
if len(input_str) < 20:
    print("INPUT:", input_str)

print("OOTIFIED:",
	ootifier(input_str, oot))
