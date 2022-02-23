
import random
import os
from time import sleep

#clear
clear= lambda : os.system("cls")

#start
print("Welcome to One line memory game")
print("By Yousef Abdalla")
print('FCAI-CU')
print()
print('Game Description:')
print("Choose two numbers, if their value is equal, you will get a point")
print('The most points will win')
print()

# Data
player1_score = 0
player2_score = 0
arr = []
list1 = []
list2=[]
list3 = []

#levels

def easy():
    global list1
    global list2
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = ["{A}", "{A}", '{B}', '{B}', '{C}', '{C}', '{D}', '{D}', '{E}', '{E}']
def medium():
    global list1
    global list2
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    list2 = ["{A}", "{A}", '{B}', '{B}', '{C}', '{C}', '{D}', '{D}', '{E}', '{E}', '{F}', '{F}', '{G}','{G}',"{H}",'{H}']
def hard():   
    global list1
    global list2
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    list2 = ["A", "A", 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J'] 
        
# randomize list every time you play
def random_list():
    global list2
    global arr
    for i in range(len(list2)):  
        i = random.choice(list2)
        arr.append(i)
        list2.remove(i)


def game():
    global player1_score
    global player2_score
    global list1
    global list2
    global arr

    #when the game will stop 
    while (len(list3) < len(list1)):

        print("p1 turn, p1_score: ", player1_score)
        print()
        print(*list1)

    #player inputs in one line
        a, b = map(int, input().split())

    #replace chosen numbers with its values
        list1[a - 1], arr[a - 1] = arr[a - 1], list1[a - 1]
        list1[b - 1], arr[b - 1] = arr[b - 1], list1[b - 1]
        
        print(*list1)
    #clear screen    
        sleep(3)
        clear()

        if (list1[a - 1] == list1[b - 1]):
            list1[b - 1] = "*"
            list1[a - 1] = "*"
            list3.append(1)
            list3.append(1)
            player1_score += 1
        
        else:
            list1[a - 1], arr[a - 1] = arr[a - 1], list1[a - 1]
            list1[b - 1], arr[b - 1] = arr[b - 1], list1[b - 1]

        print("p2 turn, p2_score: ", player2_score)
        print()
        print(*list1)
    
        a, b = map(int, input().split())

        list1[a - 1], arr[a - 1] = arr[a - 1], list1[a - 1]
        list1[b - 1], arr[b - 1] = arr[b - 1], list1[b - 1]
        print(*list1)

        sleep(3)
        clear()

        if list1[a - 1] == list1[b - 1]:
            list1[b - 1] = "*"
            list1[a - 1] = "*"

            list3.append(1)
            list3.append(1)
            
            #increase player if he gets it right 
            player2_score += 1
        
        #return replacement
        else:
            list1[a - 1], arr[a - 1] = arr[a - 1], list1[a - 1]
            list1[b - 1], arr[b - 1] = arr[b - 1], list1[b - 1]

#End game situations
def winner():
    if player1_score > player2_score:
        print("player#1 won")
    
    if player1_score < player2_score:
        print("player#2 won")
    
    if player1_score == player2_score:
        print('Draw')

sleep(5)
clear()

#ask for start
print("start?")
print("answer with YES or NO")
print()
start=input()


print("choose level")
print("answer with easy, medium, hard:")
print()
Level=input()

sleep(1)
clear()

#run the game
if start=="YES":
    if Level=='easy':
        easy()
        random_list()
        game()
        sleep(2)
        clear()
        winner()
        print('GG everybody')
        print()
        print("Thanks for trying our game")
#End

#run the game
if start=="YES":
    if Level=='medium':
        medium()
        random_list()
        game()
        sleep(2)
        clear()
        winner()
        print('GG everybody')
        print()
        print("Thanks for trying our game")
#End

#run the game
if start=="YES":
    if Level=='hard':
        hard()
        random_list()
        game()
        sleep(2)
        clear()
        winner()
        print()
        print('GG everybody')
        print()
        print("Thanks for trying our game")
#End



if start=="NO":
    print("Thanks for trying our game")
#End    
