# 가로 연속 5개 확인
x = 1
j = 1
for i in range(20) :
    for j in range(16) :
        line = board[i][j]+board[i][j+1]+board[i][j+2]+board[i][j+3]+board[i][j+4]
        if (line == 5) :
            garo = 1
        else :
            garo = -1
# 세로 연속 5개 확인
for i in range(16) :
    for j in range(20) :
        line = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+3][j]+board[i+4][j]
        if (line == 5) :
            sero = 1
        else :
            sero = -1

# 오른 대각 연속 5개 확인

# 왼 대각 연속 5개 확인
