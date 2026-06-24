import random 

attempts = 0
secret_number = random.randint(1, 100)
won = False

while  attempts < 10:
    guess = int(input("enter the number"))
    attempts = attempts + 1

    if guess == secret_number:
        print("correct")
        won = True
        break
    elif guess < secret_number:
        print("too low")

    else:
        print("too high")

if not won:
    print("Game Over, correct number was", secret_number)

