class TicTacToc:
    def __init__(self):
        self._board=[['']*3 for i in range(3)]
        self._player='X'

    def mark(self,i,j):
        if not ( 0<=i<=2 and 0<=j<=2 ):
            raise ValueError("Out of Index Your Cheack")
        if self._board[i][j]!='':
            raise ValueError("Your Cell is coupied")
        if self.winner() is not None:
            raise ValueError("Game is Complete")
        self._board[i][j]=self._player
        if self._player=='X':
            self._player='O'
        else:
            self._player='X'

    def winner(self):
        for i in 'XO':
            if self._is_win(i):
                return i
        return None

    def _is_win(self,mark):
        board = self._board  # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or
        mark == board[1][0] == board[1][1] == board[1][2] or  # row 1
        mark == board[2][0] == board[2][1] == board[2][2] or  # row 2
        mark == board[0][0] == board[1][0] == board[2][0] or  # column 0
        mark == board[0][1] == board[1][1] == board[2][1] or  # column 1
        mark == board[0][2] == board[1][2] == board[2][2] or  # column 2
        mark == board[0][0] == board[1][1] == board[2][2] or  # diagonal
        mark == board[0][2] == board[1][1] == board[2][0])

game=TicTacToc()
game.mark(0,0)
game.mark(1,0)
game.mark(0,1)
game.mark(1,1)
game.mark(2,2)
game.mark(1,2)

winner=game.winner()

if winner is None:
    print("Tie")
else:
    print("Winner Is x:")

