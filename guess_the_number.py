import random

# i made this game to practice python
# learned about random module from youtube

my_number = random.randint(1, 100)
my_attempts = 0
my_limit = 7

print("welcome to my guessing game!")
print("guess a number between 1 and 100")

# while loop was hard to understand at first
while my_attempts < my_limit:
    my_guess = int(input("enter your guess: "))
    my_attempts += 1
    my_remaining = my_limit - my_attempts

    if my_guess == my_number:
        print("correct!! you got it in " + str(my_attempts) + " attempts")
        break
    elif my_guess < my_number:
        print("too low! remaining chances: " + str(my_remaining))
    else:
        print("too high! remaining chances: " + str(my_remaining))
else:
    print("you lost! the number was " + str(my_number))
    print("better luck next time!")
