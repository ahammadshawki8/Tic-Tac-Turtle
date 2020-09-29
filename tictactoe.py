import random
import time
import turtle
from math import sqrt

Board = ['-','-','-',
        '-','-','-',
        '-','-','-']
comp_board = [i for i in range(9)]


def main():
    print("Welcome to Tick-Tac-Turtle!")
    time.sleep(.5)
    print("Version 2.0\n")
    time.sleep(.5)
    input("Press enter key to start the game.\n")
    time.sleep(1)
    level = int(input("Choose your level :\n0. Easy\n1. Medium\n(0/1) -> ").strip())
    if level == 0:
        computermove = computermove0
    else:
        computermove = computermove1
    moves = 9
    print("\nHere is the Board")
    display_board()
    display_board_new()
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
    print(Board[0]+"|"+Board[1] +"|"+Board[2]+"\n"+
              Board[3]+"|"+Board[4]+"|"+Board[5]+
              "\n"+
              Board[6]+"|"+Board[7]+"|"+Board[8])


    

def winchecker():
    for i in range(3):
        if Board[i] == Board[i+3] == Board[i+6] == "O":
            display_board()
            draw_strike(i,i+6)
            print("\nCongratulations!! You won the game.")
            return True
        elif Board[i] == Board[i+3] == Board[i+6] == "X":
            display_board()
            draw_strike(i,i+6)
            print("\nSorry, Computer wins the game :(")
            return True
        else:
            pass
    
    for i in range(0,9,3):
        if Board[i] == Board[i+1] == Board[i+2] == "O":
            display_board()
            draw_strike(i,i+2)
            print("\nCongratulations!! You won the game.")
            return True
        elif Board[i] == Board[i+1] == Board[i+2] == "X":
            display_board()
            draw_strike(i,i+2)
            print("\nSorry, Computer wins the game :(")
            return True
        else:
            pass
    if Board[0] == Board[4] == Board[8] == "O": 
        display_board()
        draw_strike(0,8)
        print("\nCongratulations!! You won the game.")
        return True
    elif Board[2] == Board[4] == Board[6] == "O":
        display_board()
        draw_strike(2,6)
        print("\nCongratulations!! You won the game.")
        return True
    elif Board[0] == Board[4] == Board[8] == "X":
        display_board()
        draw_strike(0,8)
        print("\nSorry, Computer wins the game :(")
        return True
    elif Board[2] == Board[4] == Board[6] == "X":
        display_board()
        draw_strike(2,6)
        print("\nSorry, Computer wins the game :(")
        return True

    else:
        pass 


def playermove():
    a = int(input("\nSelect the position of your mark: "))
    if a <= 9 and Board[a-1] == "-":
        Board[a-1] = "O"
        pos = get_coords(a-1)
        draw_circle(pos,"blue")
        comp_board.remove(a-1)
        pass
    else:
        print("Please input a valid position.")
        playermove()

def computermove0():
    a = random.choice(comp_board)
    pos = get_coords(a)
    draw_cross(pos,"red")
    comp_board.remove(a)
    Board[a] = "X"
    pass

def computermove1():
    for i in range(0,9,3):
        if Board[i] == Board[i+1] == "X" and Board[i+2] == "-":
            Board[i+2] = "X"
            pos = get_coords(i+2)
            draw_cross(pos,"red")
            comp_board.remove(i+2)
            return True

        elif Board[i+1] == Board[i+2] == "X" and Board[i] == "-":
            Board[i] = "X"
            pos = get_coords(i)
            draw_cross(pos,"red")
            comp_board.remove(i)
            return True

        elif Board[i] == Board[i+2] == "X" and Board[i+1] == "-":
            Board[i+1] = "X"
            pos = get_coords(i+1)
            draw_cross(pos,"red")
            comp_board.remove(i+1)
            return True
        else:
            pass

    for i in range(3):
        if Board[i] == Board[i+3] == "X" and Board[i+6] == "-":
            Board[i+6] = "X"
            pos = get_coords(i+6)
            draw_cross(pos,"red")
            comp_board.remove(i+6)
            return True
        elif Board[i] == Board[i+6] == "X" and Board[i+3] == "-":
            Board[i+3] = "X"
            pos = get_coords(i+3)
            draw_cross(pos,"red")
            comp_board.remove(i+3)
            return True
        elif Board[i+3] == Board[i+6] == "X" and Board[i] == "-":
            Board[i] = "X"
            pos = get_coords(i)
            draw_cross(pos,"red")
            comp_board.remove(i)
            return True
        else:
            pass
    
    for i in range(0,9,3):
        if Board[i] == Board[i+1] == "O" and Board[i+2] == "-":
            Board[i+2] = "X"
            pos = get_coords(i+2)
            draw_cross(pos,"red")
            comp_board.remove(i+2)
            return True
        elif Board[i+1] == Board[i+2] == "O" and Board[i] == "-":
            Board[i] = "X"
            pos = get_coords(i)
            draw_cross(pos,"red")
            comp_board.remove(i)
            return True
        elif Board[i] == Board[i+2] == "O" and Board[i+1] == "-":
            Board[i+1] = "X"
            pos = get_coords(i+1)
            draw_cross(pos,"red")
            comp_board.remove(i+1)
            return True
        else:
            pass
    for i in range(3):
        if Board[i] == Board[i+3] == "O" and Board[i+6] == "-":
            Board[i+6] = "X"
            pos = get_coords(i+6)
            draw_cross(pos,"red")
            comp_board.remove(i+6)
            return True
        elif Board[i] == Board[i+6] == "O" and Board[i+3] == "-":
            Board[i+3] = "X"
            pos = get_coords(i+3)
            draw_cross(pos,"red")
            comp_board.remove(i+3)
            return True
        elif Board[i+3] == Board[i+6] == "O" and Board[i] == "-":
            Board[i] = "X"
            pos = get_coords(i)
            draw_cross(pos,"red")
            comp_board.remove(i)
            return True
        else:
            pass
    a = random.choice(comp_board)
    pos = get_coords(a)
    draw_cross(pos,"red")
    comp_board.remove(a)
    Board[a] = "X"
    pass

                                                            
def toss():
    toss_result =  random.randint(0,1)
    if toss_result == 0:
        return True
    else:
        return False



def get_coords(pos):
    coords_map = {0:[-130,125],1:[-40,125],2:[50,125],3:[-130,35],4:[-40,35],5:[50,35],6:[-130,-55],7:[-40,-55],8:[50,-55]}
    return coords_map[pos]



def draw_strike(start,end):
    pen = turtle.Turtle()
    start_pos = get_coords(start)
    end_pos = get_coords(end)
    pen.penup()
    pen.goto(start_pos)
    pen.pendown()
    pen.goto(end_pos)
    pen.hideturtle()
    



def draw_circle(pos,pcolor):
    pen = turtle.Turtle()
    pen.color(pcolor)
    pos[1] -= 25

    pen.penup()
    pen.goto(pos)
    pen.pendown()

    pen.circle(25)
    pen.hideturtle()
    pen.left(90)

def draw_cross(pos,pcolor):
    pen = turtle.Turtle()
    pen.color(pcolor)
    pos[0] -= 25
    pos[1] -= 25

    pen.penup()
    pen.goto(pos)
    pen.left(45)
    pen.pendown()
    pen.forward(50*sqrt(2))
    pen.left(45)


    pen.penup()
    pen.goto((pos[0]+50,pos[1]))
    pen.left(45)
    pen.pendown()
    pen.forward(50*sqrt(2))
    pen.right(45)
    pen.hideturtle()


def display_board_new():
    pen = turtle.Turtle()

    pen.penup()
    pen.goto((-85,-100))
    pen.left(90)
    pen.pendown()
    pen.forward(270)


    pen.penup()
    pen.goto((5,170))
    pen.left(180)
    pen.pendown()
    pen.forward(270)
    pen.right(180)

    pen.penup()
    pen.goto((95,-10))
    pen.left(90)
    pen.pendown()
    pen.forward(270)
    pen.right(90)

    pen.penup()
    pen.goto((-175,80))
    pen.left(270)
    pen.pendown()
    pen.forward(270)
    pen.right(270)
    pen.hideturtle()







main()
while True:
    time.sleep(4)
    import turtle
    turtle.clearscreen()
    q = input("\n\nDo you want to play again?\na)yes\nb)no\n(a/b) -> ").lower().strip()
    if q == "a":
        print("\n\n\n")
        Board = ['-','-','-',
                '-','-','-',
                '-','-','-']
        comp_board = [i for i in range(9)]
        main()
    else:
        print("\n\nThanks for playing Tick-Tac-Turtle.")
        time.sleep(1)
        print("Created by Arko Chowdhury & Ahammad Shawki.")
        time.sleep(4)
        break
