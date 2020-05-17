import curses
from curses import wrapper
from test3 import *
import numpy as np

def main(stdscr,l,xy):
    
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)

    def print_board(l):
        try:
            for i in range(len(l)):
                for j in range(0,((len(l)-1)*dimensions)+1,dimensions):
                    stdscr.addstr(i,j,str(l[int(i)][int(j/dimensions)]),curses.A_BOLD)
        except curses.error:
            text1 = "Please increase terminal height "
            print_string(stdscr,text1)

    def print_string(stdscr,text):
        stdscr.clear()
        try:   
           stdscr.addstr(dimensions+1,0,text,curses.A_ITALIC)
        except curses.error:
            stdscr.addstr(0,((len(l)-1)*dimensions)+1,text,curses.A_ITALIC)
        stdscr.refresh()

    win = False
    while win == False:
        add_2_board(l,xy)
        print_board(l)
        key = stdscr.getch()
        
        stdscr.clear()
        if key == curses.KEY_LEFT or key == ord('a'):
            hori_move_left(l)
        elif key == curses.KEY_RIGHT or key == ord('d'):
            hori_move_right(l)
        elif key == curses.KEY_DOWN or key == ord('s'):
            verti_move_down(l)    
        elif key == curses.KEY_UP or key == ord('w'):
            verti_move_up(l)
        win,text = end_decider(l,xy)
    stdscr.clear()
    print_string(stdscr,text)
    print_board(l)
    stdscr.refresh()
    stdscr.getkey()

game = True
while game == True:
    try:
        dimensions = int(input("Please enter desired dimensions: "))
        xy = int(input("Enter Chalenging no: "))
    except (ValueError,NameError):
        dimensions = 4
        xy = 2048
    l = np.array([[0 for row in range(dimensions)] for col in range(dimensions)])
    stdscr = curses.initscr()
    wrapper(main,l,xy)
    again = input("Do you wanna play again(y/n): ")
    if again.lower() == "n":
        print("Thank you for playing..")
        game = False
        break
    elif again.lower() == "y":
        game = True
    else:
        print("Not a GOOD input bye. o(一︿一+)o")
        game = False
        break

