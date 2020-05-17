play = True
while play == True:
    game_size = int(input("Enter the dimensions of game: "))
    l = [[0 for i in range(game_size)] for i in range(game_size)]
    win = False
    print("   "+"  ".join([str(i) for i in range(len(l))]))
    for count,row in enumerate(l):
        print(count,row)

    def user1_input():
        x = int(input('Enter x1:'))
        y = int(input('Enter y1:'))
        player1 = game(x,y,1)
        player1.game_print()

    def user2_input():
        x = int(input('Enter x2:'))
        y = int(input('Enter y2:'))
        player2 = game(x,y,2)
        player2.game_print()   

    def umpire(l,win):
        for row in l:
            if check(row,win):
                print(f"Congratulation player{row[0]} you'r winner Horizontally!!")
                return True
    
        for i in range(len(l)):
            list1 = []
            for row in l:
                list1.append(row[i])
            if check(list1,win):
                print(f"Congratulation player{list1[0]} you'r winner vertically!!")
                return True

        list2 =[]
        for i in range(len(l)):
            list2.append(l[i][i])
        if check(list2,win):
            print(f"Congratulation player{list2[0]} you'r winner Diagonally(\\)!!")
            return True

        list3 =[]
        for i,j in zip(reversed(range(len(l))), range(len(l))):
            list3.append(l[i][j])
        if check(list3,win):
            print(f"Congratulation player{list3[0]} you'r winner Diagonally(/)!!") 
            return True
   
    def check(x,win):
        if x.count(x[0]) == len(x) and x[0] != 0:
            win = True
            return win 

    class game:
        def __init__(self,x,y,player=0):
            self.x = x
            self.y = y
            self.z = player

        def game_print(self):
            try:
                if (l[self.y][self.x]) == 0:
                    (l[self.y][self.x]) = self.z 
                else:
                    print("Position already occupied")
                print("   "+"  ".join([str(i) for i in range(len(l))]))
                count=0
                for count,row in enumerate(l):
                    print(count,row)
            except IndexError as e:
                print('Error:Please enter Input from 0-2',e)
            except Exception as e:
                print('ERROR: Something  isn\'t right,',e)



    while win == False:
        user1_input()
        if umpire(l,win):
            again = input("Game is over do you want to play again? (y/n): ")
            if again.lower() == "y":
                print('Restarting')
                break
            elif again.lower() == "n":
                print("bye")
                play = False
                break
            else:
                print("Input is not valid thank you for playing...")
                play = False
                break   

        user2_input()
        if umpire(l,win):
            again = input("Game is over do you want to play again? (y/n): ")
            if again.lower() == "y":
                print('Restarting')
                break
            elif again.lower() == "n":
                print("bye")
                play = False
                break
            else:
                print("Input is not valid thank you for playing...")
                play = False
                break   


        