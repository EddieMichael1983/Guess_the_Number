#Guess the number

import random
num1 = random.randint(1,10)

counter = 1    #sets up counting function (starting at 1 because the user will guess at least one time)

while True:

    user_guess = input("Guess what number between 1 and 10 I'm thinking of?: ")
    user_guess = int(user_guess)

    if user_guess == num1:        #line 13 and 14 stop the program once the user has guessed correctly
        break
    counter = counter + 1         #line 15 continues to add to the count for each time the user guesses incorrectly

    if user_guess == num1:
        print("You got it!")

    elif user_guess > num1:
        print("Too high!")

    elif user_guess < num1:
        print("Too low!")

print(f"You guessed {counter} times")    #function showing the user how many times they guessed until getting the right number



#Additional Challenges to add later

#Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost.

#Tell the user whether their current guess is closer than their last.

#Swap the user with the computer: the user will pick a number, and the computer will guess until they get it right.
