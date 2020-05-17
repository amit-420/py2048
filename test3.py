import random as rdm

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
                               