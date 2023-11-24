import secrets

point = 0

while(True):
    dice1 = secrets.SystemRandom().randint(1,6)
    dice2 = secrets.SystemRandom().randint(1,6)
    total = dice1 + dice2
    print("You rolled", dice1, "+", dice2, "=", total)
    if total in [7,11] and point == 0:
        print("You win!!!")
        break
    elif total in [2,3,12] and point == 0:
        print("You lose!")
        break
    elif point == 0:
        point = total
    elif total == 7:
        print("You lose!")
        break
    elif point == total:
        print("You win!!!")
        break

