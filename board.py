def printboard(board) :
    print("    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")
    for x in range(20):
        print(str(x+1).rjust(2), end = " ")
        for y in range(20):
            print(str(board[x][y]).rjust(2), end=" " if y < 19 else "\n")

board = [['+' for _ in range(20)] for _ in range(20)]

printboard(board)
