# One-line-memory-game
Guessing game with python
. One line memory game. In this game, 10 characters are chosen. Each character is repeated 
twice. The characters are put in random order. Each player picks two numbers between 1 and 
20. The two characters in these positions are shown and the rest are covered with their 
position number. If the two characters match, the player wins a point and these two 
characters are covered with * from now on. The screen is cleared and the remaining 
character positions are displayed for the next player. When all characters are covered with *, 
the game ends and the player with the biggest score wins. 
Example:
Welcome: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
Player#1 – score 0: 11, 13
Welcome: 1 2 3 4 5 6 7 8 9 0 A 2 C 4 5 6 7 8 9 0
Screen is cleared.
Welcome: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
Player#2– score 0: 6, 11
Welcome: 1 2 3 4 5 A 7 8 9 0 A 2 3 4 5 6 7 8 9 0
Screen is cleared.
Welcome: 1 2 3 4 5 * 7 8 9 0 * 2 3 4 5 6 7 8 9 0
Player#1– score 0: 1, 8
Welcome: C 2 3 4 5 * 7 B 9 0 * 2 3 4 5 6 7 8 9 0
Screen is cleared.
Welcome: 1 2 3 4 5 * 7 8 9 0 * 2 3 4 5 6 7 8 9 0
Player#2– score 1: 1, 13
Welcome: C 2 3 4 5 * 7 8 9 0 * 2 C 4 5 6 7 8 9 0
Screen is cleared.
Welcome: * 2 3 4 5 * 7 8 9 0 * 2 * 4 5 6 7 8 9 0
Player#1– score 0: 2, 16
Welcome: * F 3 4 5 * 7 8 9 0 * 2 * 4 5 F 7 8 9 0
Screen is cleared.
Welcome: * * 3 4 5 * 7 8 9 0 * 2 * 4 5 * 7 8 9 0
Player#2– score 2: 19, 20
Welcome: * * 3 4 5 * 7 8 9 0 * 2 * 4 5 * 7 8 D E
Screen is cleared.
…………. Repeat until one of them wins
