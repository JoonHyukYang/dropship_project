import os

SIZE = 15
BOARD = [['+' for _ in range(SIZE)] for _ in range(SIZE)]
BOARD[SIZE//2][SIZE//2] = "●"

HOST = '127.0.0.1'
PORT = 50007

def printboard(board, size) :
    os.system("clear")
    print("  "+"".join(str(n+1).rjust(3) for n in range(size)))
    for i in range(size):
        print(str(i+1).rjust(2), end = " ")
        for j in range(size):
            print(str(board[i][j]).rjust(2), end=" " if j < size-1 else "\n")

def getcor(name, mark, board, size) :
    while True:
        x = input(name+"의 x좌표를 입력하시오 : ")
        y = input(name+"의 y좌표를 입력하시오 : ")
        if x.isdigit() and y.isdigit():
            x, y = map(int, [x, y])
            # if check33(y-1, x-1) and mark == "●":
            #     print("쌍삼입니다\n다시입력하세요")
            if x in range(1,size+1) and y in range(1,size+1) and board[y-1][x-1] == "+":
                break
            else :
                print("다시입력하세요")
        else :
            print("다시입력하세요")
    return (y, x)
