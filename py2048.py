import curses
from curses import wrapper
import numpy as np
import random as rdm
import time
### Functions to be used ####
def spidy(l):
    random_list = []
    x = 0
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j] == 0:
                list1 = [i,j]
                random_list.append(list1)
            elif l[i][j] > x:
                x = l[i][j]
    return random_list,x                 

def add_2_board(l,xy):
    random_list,x = spidy(l)
    if len(random_list) > 0:
        l2 = rdm.choice(random_list)
        l[l2[0]][l2[1]] = 2
        

def end_decider(l,xy):
    random_list,x = spidy(l)
    if len(random_list) == 0 and len(l) == 1:
        if x == xy:
            win = True
            text = "what a swiping victory"
        else:
            win = True
            text = "Game over no more moves available"    
        return win,text
    elif len(random_list) == 0 and len(l) > 1:
        win = True
        text = "Game over no more moves available"
        return win,text
    elif x == xy:
        if xy == 2048:
            win = False
            text = "Congratulations winner" 
        else:
            win = True
            text = "Congratulations winner"
        return win,text
    else:
        win = False
        text = "Good going"
        return win,text

def hori_move_left(l):
    for row in l:
        for j in range(0,len(l)-1,1):
            y = 1
            craowling = True
            while craowling == True and j+y<=(len(l)-1):
                if row[j] == 0 and row[j] < row[j+y]:
                    row[j],row[j+y] = row[j+y],row[j]
         
                elif row[j] == row[j+y] and row[j] != 0:
                    row[j] = row[j]+row[j+y]
                    row[j+y] = 0 
                    craowling = False      
                
                elif row[j] != row[j+y] and row[j+y] != 0:
                    craowling = False 
                y += 1        
    return l         

def hori_move_right(l):
    for row in l:
        for j in range((len(row)-1),0,-1):
            y = 1
            craowling = True
            while craowling == True and j-y >= 0:
                if row[j] == 0 and row[j] < row[j-y]:
                    row[j],row[j-y] = row[j-y],row[j]
                    
                elif row[j] == row[j-y] and row[j] != 0:
                    row[j] = row[j]+row[j-y]
                    row[j-y] = 0 
                    craowling = False      
                
                elif row[j] != row[j-y] and row[j-y] != 0:
                    craowling = False    
                y += 1        
    return l           

def verti_move_down(l):
    l = hori_move_right(l.transpose()).transpose()
    return l

def verti_move_up(l):
    l = hori_move_left(l.transpose()).transpose()
    return l
######____________________#############

###### wrapper function starts here ########
def main(stdscr,l,xy):
    
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
            time.sleep(2)

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
        else:
            print_string(stdscr,"Use either arrow keys or wasd keys")
            time.sleep(0.7)  
        win,text = end_decider(l,xy)
        print_string(stdscr,text)
    
    stdscr.clear()
    print_string(stdscr,text)
    print_board(l)
    stdscr.refresh()
    stdscr.getkey()
####### wrapper function ends here #############

######## Everything starts here ############ 
game = True
while game == True:
    try:
        dimensions = int(input("Please enter desired dimensions: "))
        xy = 2**int(input("Enter power of 2 chalenging for you: "))     
    except (ValueError,NameError):
        dimensions = 4
        xy = 2048
    print(f"Your Target is: {xy} ")
    time.sleep(1)
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
########## Everything ends here ###########
