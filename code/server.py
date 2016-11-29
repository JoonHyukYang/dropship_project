import socket
import os
from functions import *

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
    printboard(BOARD, SIZE)
    print("상대를 기다리는중..")

    data = conn.recv(1024)
    decoded_data = bytes.decode(data)
    x, y = map(int, decoded_data.split(","))
    BOARD[x-1][y-1] = "○"

    printboard(BOARD, SIZE)
    x, y = getcor(name, "●", BOARD, SIZE)
    BOARD[x-1][y-1] = "●"

    data = str.encode(str(x) + "," + str(y))
    conn.sendall(data)

conn.close()
