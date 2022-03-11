#open input file
file = open('input', 'r')

#initialise initial floor as 0 and position in the input list
floor = int(0)
position = int(0)

while 1:
	#read each character
	char = file.read(1)
	if not char:
		break
	if char == '(':
		floor += 1
		position += 1
	if char == ')':
		floor -= 1
		position += 1
	if floor < 0:
		print(position)
		break
file.close()
