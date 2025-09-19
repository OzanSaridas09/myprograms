square = 1
validRoll = False
print("Welcome to snakes and ladders!")
while True:
    while True:
        roll = int(input("Enter rolled number: "))
        if roll > 6 or roll < 1:
            print(f"Please enter a valid roll. Rolling a {roll} is not possible")
            print("")
        else:
            break
        
    square = square + roll
    if square >= 100:
        print("You hit square 100. You win!")
        while True:
            userInput = input("Want to play again?: Yes/no: ")
            if userInput.lower() == "yes":
                square = 1
                break
            elif userInput.lower() != "no":
                print("Please enter a valid input. Yes/no: ")
            else:
                break
        if userInput.lower() == "no":
            break
    else:
        if square == 9:
            square += 25
            print(f"You landed on a ladder!")
        elif square == 40:
            square += 24
            print(f"You landed on a ladder!")
        elif square == 67:
            square += 19
            print(f"You landed on a ladder!")
        elif square == 54:
            square -= 35
            print(f"Oops! You landed on a snake!")
        elif square == 90:
            square -= 42
            print(f"Oops! You landed on a snake!")
        elif square == 99:
            square -= 22
            print(f"Oops! You landed on a snake!")
    print("------------------------------------------------------------------------------------")
    print(f"You are now at square {square}")
    print("------------------------------------------------------------------------------------")