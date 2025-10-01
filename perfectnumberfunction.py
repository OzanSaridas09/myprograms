import math
def is_perfect(num):
    divider = 1
    total = 0
    while divider < num:
        if num % divider == 0:
            total += divider
        if divider == math.sqrt(num):
            break
        divider += 1
    return total == num
number = 2
while number <= 1000000:
    if is_perfect(number):
        print(f"{number} is perfect")
    number += 2