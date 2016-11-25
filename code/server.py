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
s.bind((HOST,PORT))
name = input("이름을 입력해주세요 : ")

s.listen(1)
conn, addr = s.accept()

data = str.encode(name+" : 오목온라인에 오신것을 환영합니다")
conn.sendall(data)
data = conn.recv(1024)
c_name = bytes.decode(data)
print(c_name+"님이 접속하셨습니다", addr[0])

while 1:
    data = conn.recv(1024)
    decoded_data = bytes.decode(data)
    print(decoded_data)
    # if decoded_data == "exit" : break
    x, y = map(int, decoded_data.split(","))
    BOARD[x-1][y-1] = "○"

    # print (decoded_data)
    printboard()
    cor = input("get cord ex) x,y : ")
    x, y = map(int, cor.split(","))
    BOARD[x-1][y-1] = "●"

    data = str.encode(cor)
    conn.sendall(data)
conn.close()
