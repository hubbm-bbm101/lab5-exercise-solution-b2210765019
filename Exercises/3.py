import random 
number = random.randint(1,50)
guess_number = int(input("Enter your guess: "))
while guess_number != number:
    if guess_number < number:
        print("It is false.Increase your guess.")
    if guess_number > number:
        print("It is false.Decrease your guess.")
    guess_number = int(input("Enter your guess: ")) 
print("It is true.")