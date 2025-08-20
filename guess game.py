from random import randint

computer = randint(1,100)

guess = 1
try:
    while True:
        user_guess = int(input("enter your guess: "))
        if (user_guess > 101 or user_guess<-1 ):
            print("Please guess a number between 1 and 100.")
            continue
        if (user_guess != computer):
            if(user_guess>computer):
                print("guess lower number!")
            elif(user_guess<computer):
                print("guess user_guess higher number! ")
            guess += 1
        else:
            print(f"you guessed it  right ! in {guess} guess" )
            break

except ValueError:
    print("Invalid input! Please enter a valid number.")
