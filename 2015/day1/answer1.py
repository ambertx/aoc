#open input file
file = open('input', 'r')

#initialise variable to track current floor
floor = int(0)

#loop through input
while 1:
	#read each character
	char = file.read(1)
	if not char:
		break
	if char == '(':
		floor += 1
	if char == ')':
		floor -= 1
file.close()

print(floor)
