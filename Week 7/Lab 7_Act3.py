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

chessCharIdentifiers = [
    "RNBQKBNR",
    "PPPPPPPP",
    "pppppppp",
    "rnbqkbnr"
]  # piece identifiers
board = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]  # changing board
letters = "ABCDEFGH"  # letter identifiers for columns

moving = True
while moving:

    # print board
    print("\n\n")
    print("    A  B  C  D  E  F  G  H\n  _________________________")  # border and row coordinates
    for i in range(len(board) - 1, -1, -1):
        print(str(i + 1) + " |", end="")  # border and column coordinates
        for j in range(len(board[i])):
            piece = board[i][j]  # assign piece to the board's position
            spacing = 3  # amount of character spaces (+ 1) between each character
            print("\u0322" + piece.center(spacing), end='')  # print out the piece in the right spot
        print("| " + str(i + 1))  # border and column coordinates
    print("  _________________________\n    A  B  C  D  E  F  G  H")  # border and row coordinates

    # ask for move input
    move = input("Please enter a move in the format pE4 (piece, column, row).\nIf there are two of the piece you are"
                 " looking for, then enter\nthe row or column that the piece you want to move is unique\nto in the format"
                 " EpE4 (row of piece, piece, column, row). Enter \"stop\" to quit.\n")

    # stop if asked
    if move.lower() == "stop":
        print("\nQuitting.")
        break

    # interpret move
    if len(move) == 3:
        # if there are three arguments in the user input

        piece = move[0]  # the type of piece
        row = -1
        column = int(move[2]) - 1
        location = [-1, -1]  # the original location of the piece
        invalidColumn = False
        if column >= 8:
            invalidColumn = True

        # find piece
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == piece:
                    location = [i, j]  # set piece's original location
                    break

        # find row
        for i in range(len(letters)):
            if letters[i] == move[1].upper():
                row = i
                break

        # start over if move is invalid
        if location == [-1, -1] or row == -1 or (7 < column < 0) or invalidColumn:
            print("Invalid input or the piece could not be found.\n")
            continue

        # move piece
        board[location[0]][location[1]] = " "  # make the piece's original position blank
        board[column][row] = piece  # move the piece to the new position

    elif len(move) == 4:
        # if there are four arguments in the user input

        piece = move[1]  # the type of piece
        row = -1
        column = int(move[3]) - 1
        location = [-1, -1]  # the original location of the piece
        invalidColumn = False
        if column >= 8:
            invalidColumn = True

        # find piece
        if move[0].isnumeric():
            i = int(move[0]) - 1
            for j in range(len(board)):
                if piece == board[i][j]:
                    location = [i, j]
        else:
            j = -1
            for k in range(len(letters)):
                if move[0].upper() == letters[k]:
                    j = k
            for i in range(len(board)):
                if piece == board[i][j]:
                    location = [i, j]

        # find row
        for i in range(len(letters)):
            if letters[i] == move[2].upper():
                row = i
                break

        # start over if move is invalid
        if location == [-1, -1] or row == -1 or (0 <= column <= 7) or invalidColumn:
            print("Invalid input or the piece could not be found.\n")
            continue

        # move piece
        board[location[0]][location[1]] = " "
        board[column][row] = piece

    else:
        print("That was not a valid move input.\n")
        continue





