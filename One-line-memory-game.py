
import random
import os
from time import sleep

#clear
clear= lambda : os.system("cls")

#start
print("Welcome to One line memory game")
print("By Yousef Abdalla Attia")
print('FCAI-CU')
print()
print('Game Description:')
print("Choose two numbers, if their value is equal, you will get a point")
print('The most points will win')
print()

# Data
player1_score = 0
player2_score = 0
random_char_list = []
numbers = []
characters=[]
check_Win_list = []

#levels

def easy():
    global numbers
    global characters
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    characters = ["{A}", "{A}", '{B}', '{B}', '{C}', '{C}', '{D}', '{D}', '{E}', '{E}']

def medium():
    global numbers
    global characters
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    characters = ["{A}", "{A}", '{B}', '{B}', '{C}', '{C}', '{D}', '{D}', '{E}', '{E}', '{F}', '{F}', '{G}','{G}',"{H}",'{H}']

def hard():   
    global numbers
    global characters
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    characters = ["A", "A", 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J'] 
        
# randomize list every time you play
def random_list():
    global characters
    global random_char_list
    for i in range(len(characters)):  
        i = random.choice(characters)
        random_char_list.append(i)
        characters.remove(i)

#run 
running = True


def game():
    running = True
    global player1_score
    global player2_score
    global numbers
    global characters
    global random_char_list

    #game loop
    while running:

        print("p1 turn, p1_score: ", player1_score)
        print()
        print(*numbers)
        

    #player1 inputs in one line
        a, b = map(int, input().split())

    #replace chosen numbers with its values
        numbers[a - 1], random_char_list[a - 1] = random_char_list[a - 1], numbers[a - 1]
        numbers[b - 1], random_char_list[b - 1] = random_char_list[b - 1], numbers[b - 1]
        
        print(*numbers)
    #clear screen    
        sleep(3)
        clear()

        if (numbers[a - 1] == numbers[b - 1]):
            numbers[b - 1] = "*"
            numbers[a - 1] = "*"
            check_Win_list.append('*')
            check_Win_list.append('*')
            player1_score += 1
        
        else:
            numbers[a - 1], random_char_list[a - 1] = random_char_list[a - 1], numbers[a - 1]
            numbers[b - 1], random_char_list[b - 1] = random_char_list[b - 1], numbers[b - 1]
        if (len(check_Win_list) == len(numbers))  :
            running = False  
            

        print("p2 turn, p2_score: ", player2_score)
        print()
        print(*numbers)
        
        #player inputs in one line
        a, b = map(int, input().split())

        numbers[a - 1], random_char_list[a - 1] = random_char_list[a - 1], numbers[a - 1]
        numbers[b - 1], random_char_list[b - 1] = random_char_list[b - 1], numbers[b - 1]
        print(*numbers)

        sleep(3)
        clear()

        if numbers[a - 1] == numbers[b - 1]:
            numbers[b - 1] = "*"
            numbers[a - 1] = "*"

            check_Win_list.append('*')
            check_Win_list.append("*")
            
            #increase player if he gets it right 
            player2_score += 1
        
        #return replacement
        else:
            numbers[a - 1], random_char_list[a - 1] = random_char_list[a - 1], numbers[a - 1]
            numbers[b - 1], random_char_list[b - 1] = random_char_list[b - 1], numbers[b - 1]
        if (len(check_Win_list) == len(numbers))  :
            running = False      

#End game situations
def winner():
    if player1_score > player2_score:
        print("player#1 won")
    
    if player1_score < player2_score:
        print("player#2 won")
    
    if player1_score == player2_score:
        print('Draw')

sleep(4)
clear()

#ask for start
print("start?")
print("answer with YES or NO")
print('1 for YES, 2 for NO ')
print()
start=int(input())


print("choose level")
print("answer with Easy, Medium or Hard:")
print('1 for Easy')
print('2 for Medium')
print('3 for Hard')

print()
Level=int(input())

sleep(1)
clear()

#run the game
if start== 1:
    if Level == 1:
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
if start==1:
    if Level == 2:
        medium()
        random_list()
        game()
        sleep(1)
        clear()
        winner()
        print('GG everybody')
        print()
        print("Thanks for trying our game")
#End

#run the game
if start == 1:
    if Level == 3:
        hard()
        random_list()
        game()
        sleep(1)
        clear()
        winner()
        print()
        print('GG everybody')
        print()
        print("Thanks for trying our game")
#End



if start == 2:
    print("Thanks for trying our game")
#End    



