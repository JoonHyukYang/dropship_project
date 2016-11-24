class Board:
    """
    docstring for Board.\n
    made by yangjoonhyuk\n
    """
    def __init__(self):
        self.board = [['+' for _ in range(20)] for _ in range(20)]
        self.startgame()


    def printboard(self) :
        print("    1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20")
        for x in range(20):
            print(str(x+1).rjust(2), end = " ")
            for y in range(20):
                print(str(self.board[x][y]).rjust(2), end=" " if y < 19 else "\n")

    def startgame(self):
        while True:
            self.printboard()
            x = int(input("player1의 x좌표를 입력하시오 : "))
            y = int(input("player1의 y좌표를 입력하시오 : "))
            self.board[x-1][y-1] = "●"
            # self.check()
            self.printboard()
            x = int(input("player2의 x좌표를 입력하시오 : "))
            y = int(input("player2의 y좌표를 입력하시오 : "))
            self.board[x-1][y-1] = "○"
            # self.check()

    def check(self):
        pass

b = Board()
