#Guess the number
import random
num1 = random.randint(1,10)

user_guess = input("Guess what number between 1 and 10 I'm thinking of?: ")
user_guess = int(user_guess)

if user_guess == num1:
    print("You got it!")

elif user_guess > num1:
    print("Too high!")

elif user_guess < num1:
    print("Too low!")
