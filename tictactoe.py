import random
import time

Board = ['-','-','-',
        '-','-','-',
        '-','-','-']
comp_board = [i for i in range(9)]


def main():
    print("Welcome to tick-tac-toe!")
    time.sleep(.5)
    input("Press enter key to start the game.\n")
    time.sleep(1)
    moves = 9
    print("\nHere is the Board")
    display_board()
    print("\n")
    if toss() == True:
        print("Congrats! You will play first.")
        time.sleep(1)
        while moves > 0:
            playermove()
            print("\nPlayer plays the move")
            moves -= 1
            if winchecker() == True:
                break
            else:
                pass
            display_board()
            if moves == 0:
                print("It's a tie.")
                break
            time.sleep(1.5)
            computermove()
            print("\nComputer plays the move")
            moves -= 1
            if winchecker() == True:
                break
            else:
                pass
            display_board()
            if moves == 0:
                print("It's a tie.")
                break
    
    else:
        print("Sorry, Computer will play first.")
        while moves > 0:
            time.sleep(1)
            computermove()
            print("\nComputer plays the move.")
            moves -= 1
            if winchecker() == True:
                break
            else:
                pass
            display_board()
            if moves == 0:
                print("It's a tie.")
                break
            playermove()
            print("\nPlayer plays the move.")
            moves -= 1
            if winchecker() == True:
                break
            else:
                pass
            display_board()
            if moves == 0:
                print("It's a tie.")
                break
        

def display_board():
    print( Board[0]+"|"+Board[1] +"|"+Board[2]+"\n"+
              Board[3]+"|"+Board[4]+"|"+Board[5]+
              "\n"+
              Board[6]+"|"+Board[7]+"|"+Board[8])
    

def winchecker():
    for i in range(3):
        if Board[i] == Board[i+3] == Board[i+6] == "P":
            display_board()
            print("\nCongratulations!! You won the game.")
            return True
        elif Board[i] == Board[i+3] == Board[i+6] == "C":
            display_board()
            print("\nSorry, Computer wins the game :(")
            return True
        else:
            pass
    
    for i in range(0,9,3):
        if Board[i] == Board[i+1] == Board[i+2] == "P":
            display_board()
            print("\nCongratulations!! You won the game.")
            return True
        elif Board[i] == Board[i+1] == Board[i+2] == "C":
            display_board()
            print("\nSorry, Computer wins the game :(")
            return True
        else:
            pass
    if Board[0] == Board[4] == Board[8] == "P" or Board[2] == Board[4] == Board[6] == "P":
        display_board()
        print("\nCongratulations!! You won the game.")
        return True
    elif Board[0] == Board[4] == Board[8] == "C" or Board[2] == Board[4] == Board[6] == "C":
        display_board()
        print("\nSorry, Computer wins the game :(")
        return True
    else:
        pass 


def playermove():
    a = int(input("\nSelect the position of your mark: "))
    if a <= 9 and Board[a-1] == "-":
        Board[a-1] = "P"
        comp_board.remove(a-1)
        pass
    else:
        print("Please input a valid position.")
        playermove()

def computermove():
    for i in range(0,9,3):
        if Board[i] == Board[i+1] == "C" and Board[i+2] == "-":
            Board[i+2] = "C"
            comp_board.remove(i+2)
            return True
        elif Board[i+1] == Board[i+2] == "C" and Board[i] == "-":
            Board[i] = "C"
            comp_board.remove(i)
            return True
        elif Board[i] == Board[i+2] == "C" and Board[i+1] == "-":
            Board[i+1] = "C"
            comp_board.remove(i+1)
            return True
        else:
            pass
    for i in range(3):
        if Board[i] == Board[i+3] == "C" and Board[i+6] == "-":
            Board[i+6] = "C"
            comp_board.remove(i+6)
            return True
        elif Board[i] == Board[i+6] == "C" and Board[i+3] == "-":
            Board[i+3] = "C"
            comp_board.remove(i+3)
            return True
        elif Board[i+3] == Board[i+6] == "C" and Board[i] == "-":
            Board[i] = "C"
            comp_board.remove(i)
            return True
        else:
            pass
    
    for i in range(0,9,3):
        if Board[i] == Board[i+1] == "P" and Board[i+2] == "-":
            Board[i+2] = "C"
            comp_board.remove(i+2)
            return True
        elif Board[i+1] == Board[i+2] == "P" and Board[i] == "-":
            Board[i] = "C"
            comp_board.remove(i)
            return True
        elif Board[i] == Board[i+2] == "P" and Board[i+1] == "-":
            Board[i+1] = "C"
            comp_board.remove(i+1)
            return True
        else:
            pass
    for i in range(3):
        if Board[i] == Board[i+3] == "P" and Board[i+6] == "-":
            Board[i+6] = "C"
            comp_board.remove(i+6)
            return True
        elif Board[i] == Board[i+6] == "P" and Board[i+3] == "-":
            Board[i+3] = "C"
            comp_board.remove(i+3)
            return True
        elif Board[i+3] == Board[i+6] == "P" and Board[i] == "-":
            Board[i] = "C"
            comp_board.remove(i)
            return True
        else:
            pass
    a = random.choice(comp_board)
    comp_board.remove(a)
    Board[a] = "C"
    pass

                                                            
def toss():
    toss_result =  random.randint(0,1)
    if toss_result == 0:
        return True
    else:
        return False

main()
while True:
    time.sleep(2)
    q = input("\n\nDo you want to play again?\na)yes\nb)no\n(a/b) -> ").lower().strip()
    if q == "a":
        print("\n\n\n")
        Board = ['-','-','-',
                '-','-','-',
                '-','-','-']
        comp_board = [i for i in range(9)]
        main()
    else:
        print("\n\nThanks for playing tick-tac-toe.\n")
        time.sleep(1)
        print("Created by Arko Chowdhury")
        time.sleep(2)
        print("Special Thanks to Ahammad Shawki")
        time.sleep(3)
        break
