import random
while True:
    try:
        level = int("level: ")
        break
    except:
        pass
random_number = random.randit(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too small")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
    except:
        pass
    