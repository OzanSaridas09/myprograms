import math
start = 1
num = int(input("enter a value: "))
newStop = int(math.sqrt(num)) + 1
factorCount = 0
while start < newStop:
    if num % start == 0:
        dividend = num // start
        if start != dividend:
            factorCount += 2
        else:
            factorCount += 1
    start += 1
print(f"{num} has {factorCount} factors.")
        