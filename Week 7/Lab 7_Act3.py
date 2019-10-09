# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Justin Compton
# Braden Alexander
# Josh Wood
# Troy Hays
# Course/Section: ENGR 102-201/216/522
# Assignment: Lab 7 3
# Date: 9 October 2019

from math import *

chessChars = [
    "♜♞♝♛♚♝♞♜",
    "♟♟♟♟♟♟♟♟",
    "♙♙♙♙♙♙♙♙",
    "♖♘♗♕♔♗♘♖"
]
chessCharIdentifiers = [
    "RNBQKBNR",
    "PPPPPPPP",
    "pppppppp",
    "rnbqkbnr"
]

board = [
    "RNBQKBNR",
    "PPPPPPPP",
    "        ",
    "        ",
    "        ",
    "        ",
    "pppppppp",
    "rnbqkbnr"
]

# print board
print("__________")
for i in range(len(board)):
    print("|", end="")
    for j in range(len(board[i])):
        piece = board[i][j]
        for x in range(len(chessChars)):
            for y in range(len(chessChars[x])):
                if piece == chessCharIdentifiers[x][y]:
                    piece = chessChars[x][y]
                    break
        print(piece, end='')
    print("|")
print("__________")
# print("__________")
