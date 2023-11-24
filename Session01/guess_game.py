import secrets

while(True):
    print("Guess Game")
    print("Numbers from 1 to 10")
    num = secrets.SystemRandom().randint(1,10)
    tries = 0
    while(True):
        g = int(input("Guess the number: "))
        if g < num:
            print("Too Low")
        elif g > num:
            print("Too High")
        else:
            tries += 1
            print("You got it in", tries, " tries")
            break
        tries += 1
    if input("Would you play again?(y/n)") == 'n':
        break
