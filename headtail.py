from random import choice
while True:
    print("Welcome to our heads or tails game!")
    print("Please choose either heads or tails")
    while True:
        userInput = input("User's choice: ")
        userInput = userInput.lower() 
        if userInput in {"heads", "tails", "head", "tail"}:
            break
        else:
            print("Please type in either heads or tails. :")
    flipResult = choice(["heads", "tails"])
    print(f"The computer flipped: {flipResult}.")
    if userInput in ("heads", "head") and flipResult == "heads":
        print("The user guessed correctly!")
    elif userInput in ("tail", "tails") and flipResult == "tails":
        print("The user guessed correctly!")
    else: 
        print("You guessed wrong.")
    while True:
        userInput = input("Want to exit?: Yes/no: ")
        if userInput.lower() == "yes":
            break
        elif userInput.lower() != "no":
            print("Please enter a valid input. Yes/no: ")
        else:
            break
    if userInput.lower() == "yes":
        break