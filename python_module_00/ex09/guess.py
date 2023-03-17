import random

if __name__ == "__main__":
    ret = random.randint(1, 5)
    attempts = 0
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 ", end='')
    print("to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!")
    while (42):
        attempts += 1
        inp = input("\nWhat's your guess between 1 and 99?\n")
        if (inp == "exit"):
            print("Goodbye!")
            exit()
        try:
            if (int(inp) == 42):
                print("The answer to the ultimate question of life, ", end='')
                print("the universe and everything is 42.")
        except Exception:
            print("Insert a number between 1 and 99")
            continue
        if (int(inp) == ret):
            if (attempts == 1):
                print("Congratulations! You got it on your first try!")
            else:
                print(f"You won in {attempts} attempts!")
            exit(0)
        elif (int(inp) > ret and int(inp) < 100):
            print("Too high!")
        elif (int(inp) < ret and int(inp) > 0):
            print("Too low!")
