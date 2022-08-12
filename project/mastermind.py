import random

class Mastermind:
    def __init__(self):
        self.board_color = [1,2,3,4,5,6]
        self.board_game = Mastermind.new_board()
        self.board_hidden = []
        self.actual_pos = 1

    @staticmethod
    def new_board():
        board = []
        for i in range(10):
            board.append([])
            for j in range(9):
                if j == 0:
                    board[i].append(i+1)
                else:
                    board[i].append(0)
        return board
    
    def backspace_row(self):
        for i in range(1,5):
            self.board_game[self.actual_pos-1][i] = 0
    
    def test_row(self):
        for i in range(1,5):
            j = 0
            while j < len(self.board_hidden):
                if self.board_game[self.actual_pos-1][i] == self.board_hidden[i-1]:
                    self.board_game[self.actual_pos-1][i+4] = 1
                    break
                elif self.board_game[self.actual_pos-1][i] == self.board_hidden[j]:
                    self.board_game[self.actual_pos-1][i+4] = -1
                    break
                if j == len(self.board_hidden)-1:
                    self.board_game[self.actual_pos-1][i+4] = 0
                j+=1
    
    def add_color_row(self,color,pos):
        self.board_game[self.actual_pos-1][pos] = color
    
    def push_hidden_random(self):
        for i in range(4):
            self.board_hidden.append(random.choice(self.board_color))
    
    def victory_condition(self):
        if (self.board_game[self.actual_pos-1][5:9] == [1,1,1,1]):
            return True
        else :
            self.actual_pos+=1
            return False
        
    def get_actual_pos(self):
        return self.actual_pos

    def get_board_game(self):
        return self.board_game
    
    def get_board_hidden(self):
        return self.board_hidden
    
    def reset_board(self):
        for row in range(10):
            for colums in range(9):
                if colums != 0:
                    self.board_game[row][colums] = 0
        for i in range(4):
            self.board_hidden.pop()
        self.actual_pos = 1