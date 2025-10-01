def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        divider = 3
        upper_limit = int(num**0.5) + 1
        while divider < max(upper_limit, 3):
            if num % divider == 0:
                return False
            divider += 2
        return True

num = 1
while num < 1000000:
    if is_prime(num):
        print(f"{num} is prime")
    num += 1