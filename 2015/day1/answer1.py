file = open('input', 'r')

floor = int(0)

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
