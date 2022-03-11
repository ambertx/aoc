import readline

#initialise variable to track total area
totalArea = int(0)

#open input file
with open('input', 'r') as file:
    #intialise variables for sides of boxes
    l = int(0)
    w = int(0)
    h = int(0)

    #while there is data loop through file
    while line := file.readline():
        line.rstrip() #strip trailing characters

        currentList = line.split('x') #split file by the x

        currentList = list(map(int, currentList)) #cast list to int

        #sort in ascending order as we need to calaculate spare paper
        currentList.sort()

        #assign values to the sides
        l = currentList[0]
        w = currentList[1]
        h = currentList[2]

        #calculate area and add to total area
        totalArea += (3*l*w) + (2*w*h) + (2*l*h)

#print total area
print(totalArea)