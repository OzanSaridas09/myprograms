# Rollercoaster ride program
# input
placeInLine = int(input("enter your place in line"))
numCars = int(input("enter the nuber of cars"))
capacity = int(input("enter the capacity per car"))

# processing
totalCapacity = numCars * capacity

if totalCapacity >= placeInLine:
    print("Yes")
else:
    print("No")