import random 

#get random computer choice assining numbers to letters/string 
randomInt = random.randint(1,3)
if randomInt == 1: 
 computer = str("r")
elif randomInt == 2:
   computer = str("s")
elif randomInt == 3:
   computer = str("p")  
# determine winner
player = input("choose either rock (r), paper (p), or scissors (s)")  
if player == computer:
        print("Draw")
elif player == str("s") and computer == str("r")  or player == str("p") and computer == str("s") or player == str("r") and computer == str("p"):
        print("computer won")
elif player == str("s") and computer == str("p") or player == str("r") and computer == str("s") or player == str("p") and computer == str("r"):
        print("player won")
#user input for if they want keep playing
repeat = input("would you like to repeat?")
#while loop makes the code repeat if the user would like to. If not then the code/game ends
while repeat == str("yes") or repeat == str("Y") or repeat == str("y"):
        player = input("choose either rock (r), paper (p), or scissors (s)")
        if player == computer:
            print("Draw")
        elif player == str("s") and computer == str("r")  or player == str("p") and computer == str("s") or player == str("r") and computer == str("p"):
            print("computer won")
        elif player == str("s") and computer == str("p") or player == str("r") and computer == str("s") or player == str("p") and computer == str("r"):
            print("player won")
        repeat = input("would you like to repeat?")
if repeat == str("No") or str("N") or str("n"):
    print("Thank you for playing:)")