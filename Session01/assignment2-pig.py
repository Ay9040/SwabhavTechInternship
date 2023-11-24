import secrets

while(True):
    score = 0
    turn = 1
    turnPoints = 0
    print("TURN", turn)
    while(score < 20):
        if(input("Roll or hold? (r/h):") == 'r'):
            die = secrets.SystemRandom().randint(1,6)
            print("Die: ", die)
            if(die == 1):
                turnPoints = 0 
                turn += 1
                print("Turn Over. No Score.\n")
                print("TURN", turn)
            else:
                turnPoints += die
                if(score + turnPoints >= 20):
                    score += turnPoints
                    print("Total Score: ", score)
                    break
        else:
            turn += 1
            score += turnPoints
            print("Total Score: ", score, "\n")
            print("TURN", turn)
    if(input("Play Again? (y/n):") == 'n'):
        break
    print()
