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
        new_position = square
        game_dict = {
            9 : 34,
            54 : 19,
            40 : 64,
            90 : 48,
            67 : 86, 
            99 : 77
        }
        if new_position in game_dict:
            square = game_dict[new_position]
    print(f"You are now at square {square}")