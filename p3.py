# Donuts
donutCount = int(input("Enter the number of donuts: "))
events = int(input("Enter the number of events: "))

# we stop when no donut or no event
currentEvent = 1 # PERSONALLY I DO 0
while currentEvent <= events and donutCount >= 0:
    eventType = input("+ or -?")
    donutAmount = int(input("Enter donut amount: "))
    if eventType == "+":
        donutCount = donutCount + donutAmount
    elif eventType == "-":
        donutCount = donutCount - donutAmount
    else:
        print("Invalid input")
    events -= 1
# end of while
print(f"At the end of our events we have {donutCount} donuts left")