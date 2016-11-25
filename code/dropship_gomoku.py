import os

class Board:
    """
    docstring for Board.\n
    made by yangjoonhyuk\n
    """

    SIZE = 15

    def __init__(self):
        self.board = [['+' for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        self.player1 = input("player1의 이름을 입력하시오 : ")
        self.player2 = input("player2의 이름을 입력하시오 : ")
        self.startgame()

    def printboard(self) :
        os.system("clear")
        print("   "+"".join(str(x+1).center(3) for x in range(self.SIZE)))
        for x in range(self.SIZE):
            print(str(x+1).rjust(2), end = " ")
            for y in range(self.SIZE):
                print(str(self.board[x][y]).center(3), end="" if y < self.SIZE-1 else "\n")

    def startgame(self):
        self.board[self.SIZE//2][self.SIZE//2] = "●"
        self.printboard()
        while True:
            while True:
                y = int(input(self.player2+"의 x좌표를 입력하시오 : "))
                x = int(input(self.player2+"의 y좌표를 입력하시오 : "))
                if x in range(1,self.SIZE+1) and y in range(1,self.SIZE+1) and self.board[x-1][y-1] == "+":
                    break
                else :
                    print("다시입력하세요")
            self.board[x-1][y-1] = "○"
            self.printboard()
            if self.check(x-1,y-1,"○"):
                print(self.player2+" win")
                break;
            while True:
                y = int(input(self.player1+"의 x좌표를 입력하시오 : "))
                x = int(input(self.player1+"의 y좌표를 입력하시오 : "))
                if self.check33(x-1, y-1) :
                    print("쌍삼입니다\n다시입력하세요")
                elif x in range(1,self.SIZE+1) and y in range(1,self.SIZE+1) and self.board[x-1][y-1] == "+":
                    break
                else :
                    print("다시입력하세요")
            self.board[x-1][y-1] = "●"
            self.printboard()
            if self.check(x-1,y-1,"●"):
                print(self.player1+" win")
                break;

    def check33(self, x, y):
        a = []
        for n in range(1,5):
            a.append(eval("self.check"+str(n)+"("+str(x)+","+str(y)+",\"●\")"))
        if a.count(3) >= 2 or a.count(4) >= 2:
            return True
        else :
            return False

    def check(self, x, y, mark):
        a = []
        for n in range(1,5):
            a.append(eval("self.check"+str(n)+"("+str(x)+","+str(y)+",\""+mark+"\")"))
        if 5 in a or (mark == "○" and True in [x >= 6 for x in a]):
            return True
        else :
            return False

    def check1(self, x, y, mark, d = 0):
        """가로방향"""
        if x in range(self.SIZE) and y in range(self.SIZE):
            if d == 0:
                return 1 + self.check1(x-1, y, mark, 1) + self.check1(x+1, y, mark, -1)
            elif d == 1:
                if self.board[x][y] == mark:
                    return 1 + self.check1(x-1, y, mark, 1)
                else :
                    return 0
            elif d == -1:
                if self.board[x][y] == mark:
                    return 1 + self.check1(x+1, y, mark, -1)
                else :
                    return 0
        else :
            return 0

    def check2(self, x, y, mark, d = 0):
        """세로방향"""
        if x in range(self.SIZE) and y in range(self.SIZE):
            if d == 0:
                return 1 + self.check2(x, y+1, mark, 1) + self.check2(x, y-1, mark, -1)
            elif d == 1:
                if self.board[x][y] == mark:
                    return 1 + self.check2(x, y+1, mark, 1)
                else :
                    return 0
            elif d == -1:
                if self.board[x][y] == mark:
                    return 1 + self.check2(x, y-1, mark, -1)
                else :
                    return 0
        else :
            return 0

    def check3(self, x, y, mark, d = 0):
        """\\대각선모양"""
        if x in range(self.SIZE) and y in range(self.SIZE):
            if d == 0:
                return 1 + self.check3(x-1, y-1, mark, 1) + self.check3(x+1, y+1, mark, -1)
            elif d == 1:
                if self.board[x][y] == mark:
                    return 1 + self.check3(x-1, y-1, mark, 1)
                else :
                    return 0
            elif d == -1:
                if self.board[x][y] == mark:
                    return 1 + self.check3(x+1, y+1, mark, -1)
                else :
                    return 0
        else :
            return 0

    def check4(self, x, y, mark, d = 0):
        """//대각선모양"""
        if x in range(self.SIZE) and y in range(self.SIZE):
            if d == 0:
                return 1 + self.check4(x-1, y+1, mark, 1) + self.check4(x+1, y-1, mark, -1)
            elif d == 1:
                if self.board[x][y] == mark:
                    return 1 + self.check4(x-1, y+1, mark, 1)
                else :
                    return 0
            elif d == -1:
                if self.board[x][y] == mark:
                    return 1 + self.check4(x+1, y-1, mark, -1)
                else :
                    return 0
        else :
            return 0

b = Board()
