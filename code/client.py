import socket
import os
# from dropship_gomoku import Gomoku

def printboard() :
    os.system("clear")
    print("   "+"".join(str(n+1).rjust(3) for n in range(SIZE)))
    for i in range(SIZE):
        print(str(i+1).rjust(2), end = " ")
        for j in range(SIZE):
            print(str(BOARD[i][j]).rjust(2), end=" " if j < SIZE-1 else "\n")

SIZE = 15
BOARD = [['+' for _ in range(SIZE)] for _ in range(SIZE)]
BOARD[SIZE//2][SIZE//2] = "●"

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = input("이름을 입력해주세요 : ")

s.connect((HOST, PORT))
data = s.recv(1024)
decoded_data = bytes.decode(data)
print(decoded_data)
s.sendall(str.encode(name))


while 1:
    printboard()
    cor = input("get cord ex) x,y : ")
    x, y = map(int, cor.split(","))
    BOARD[x-1][y-1] = "○"

    data = str.encode(cor)
    s.sendall(data)

    data = s.recv(1024)
    decoded_data = bytes.decode(data)
    x, y = map(int, decoded_data.split(","))
    BOARD[x-1][y-1] = "●"

s.close()
