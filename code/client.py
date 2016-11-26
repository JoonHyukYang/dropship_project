import socket
import os
from functions import *

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
    printboard(BOARD, SIZE)
    x, y = getcor(name, "○", BOARD, SIZE)
    BOARD[x-1][y-1] = "○"

    data = str.encode(str(x) + "," + str(y))
    s.sendall(data)

    printboard(BOARD, SIZE)
    print("상대를 기다리는중..")

    data = s.recv(1024)
    decoded_data = bytes.decode(data)
    x, y = map(int, decoded_data.split(","))
    BOARD[x-1][y-1] = "●"

s.close()
