from tkinter import *
import sys
from functools import partial

class Callback():
    def __init__(self, game):
        self.test = 1
        self.game = game
        self.counter_paw = 0
        self.victory = False

    
    def define_number(self, window) :
        array = []
        for row in range(10) :
            array.append(Canvas(window, background = "#B2C2BB", highlightthickness= 0))
            array[row].place(relx = 0.1, y = 100 + 52 * row, height = 50, width = 50)
            array[row].create_text(25, 25, text = str(self.game.get_board_game()[row][0]))
        return array

    def define_color(self, window) :
        array = []
        for row in range(10) :
            array.append([])
            for colums in range(4) :
                array[row].append(Canvas(window, background = "#B2C2BB", highlightthickness= 0))
                array[row][colums].place(relx = 0.135 + 0.035 * colums, y = 100 + 52 * row, height = 50, width = 50)
                array[row][colums].create_oval(25+2, 25+2, 25-2, 25-2, fill = "#000000")
        return array
    
    def draw_big_canvas(self,window,array,row,colums):
        array[row].append(Canvas(window, background = "#B2C2BB", highlightthickness= 0))
        array[row][colums].place(relx = 0.2755, y = 100 + 52 * row, height = 50, width = 50)
    
    def draw_small_canvas(self,array,row,colums,x_pos,y_pos):
        array[row].append(Canvas(array[row][0], background = "#B2C2BB", highlightthickness= 0))
        array[row][colums].place(x = x_pos, y = y_pos, height = 25, width = 25)
        array[row][colums].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "black")
    
    def switch_draw_hint(self,window,array,row,colums):
        switcher={
            0 : partial(self.draw_big_canvas,window,array,row,colums),
            1 : partial(self.draw_small_canvas,array,row,colums,0,0),
            2 : partial(self.draw_small_canvas,array,row,colums,0,25),
            3 : partial(self.draw_small_canvas,array,row,colums,25,0),
            4 : partial(self.draw_small_canvas,array,row,colums,25,25)
        }
        func = switcher.get(colums)
        return func()

    def define_hint(self, window) :
        array = []
        for row in range(10) :
            array.append([])
            for colums in range(5) :
                self.switch_draw_hint(window,array,row,colums)
        return array

    def define_answer(self,window):
        array = []
        for row in range(4) :
            array.append(Canvas(window, background = "#050A02", highlightthickness= 0))
            array[row].place(relx = 0.135 + 0.035 * row, y = 650, height = 50, width = 50)
            array[row].create_oval(25+2, 25+2, 25-2, 25-2, fill = "#FFFFFF")
        return array

    def draw_button_color(self,array,hexa,number,color_block):
        array[number].create_oval(25+10, 25+10, 25-10, 25-10, fill = hexa)
        array[number].bind('<Button-1>', lambda event: self.add_color(event, number+1, hexa, color_block))
    
    def switch_button_color(self,array,number,color_block):
        switcher={
            0 : partial(self.draw_button_color,array,"red",number,color_block),
            1 : partial(self.draw_button_color,array,"blue",number,color_block),
            2 : partial(self.draw_button_color,array,"yellow",number,color_block),
            3 : partial(self.draw_button_color,array,"purple",number,color_block),
            4 : partial(self.draw_button_color,array,"orange",number,color_block),
            5 : partial(self.draw_button_color,array,"green",number,color_block)
        }
        func = switcher.get(number)
        return func()

    def button_color(self, window, color_block):
        array = []
        for row in range(6) :
            array.append(Canvas(window, background = "#050A02", highlightthickness= 0))
            array[row].place(relx = 0.1 + 0.035 * row, y = 37.5, height = 50, width = 50)
            self.switch_button_color(array,row,color_block)
        return array

    def erase_row(self, color_block):
        self.game.backspace_row()
        for row in range(4):
            color_block[self.game.get_actual_pos()-1][row].delete("all")
            color_block[self.game.get_actual_pos()-1][row].create_oval(25+2, 25+2, 25-2, 25-2, fill = "#000000")
        self.counter_paw = 0

    def add_color(self, event, color, hexa, color_block):
        if(self.counter_paw<4):
            self.game.add_color_row(color,self.counter_paw+1)
            color_block[self.game.get_actual_pos()-1][self.counter_paw].delete("all")
            color_block[self.game.get_actual_pos()-1][self.counter_paw].create_oval(25+10, 25+10, 25-10, 25-10, fill = hexa)
            self.counter_paw+=1

    def test_row(self, hint_block):
        self.game.test_row()
        for i in range(5,9):
            hint_block[self.game.get_actual_pos()-1][i-4].delete("all")
            if self.game.get_board_game()[self.game.get_actual_pos()-1][i] == 1 :
                hint_block[self.game.get_actual_pos()-1][i-4].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "red")
            elif self.game.get_board_game()[self.game.get_actual_pos()-1][i] == -1 :
                hint_block[self.game.get_actual_pos()-1][i-4].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "white")
            else :
                hint_block[self.game.get_actual_pos()-1][i-4].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "black")
        self.counter_paw = 0
        
    def draw_answer(self,answer_block,number,hexa):
        answer_block[number].create_oval(25+10, 25+10, 25-10, 25-10, fill = hexa)
    
    def switch_draw_answer(self,number,pos,answer_block):
        switcher={
            1 : partial(self.draw_answer,answer_block,pos,"red"),
            2 : partial(self.draw_answer,answer_block,pos,"blue"),
            3 : partial(self.draw_answer,answer_block,pos,"yellow"),
            4 : partial(self.draw_answer,answer_block,pos,"purple"),
            5 : partial(self.draw_answer,answer_block,pos,"orange"),
            6 : partial(self.draw_answer,answer_block,pos,"green")
        }
        func = switcher.get(number)
        return func()

    def victory_condition(self,hint_block,answer_block,color_block,window):
        if self.counter_paw == 4:
            self.test_row(hint_block)
            self.victory = self.game.victory_condition()
            if (self.victory):
                for i in range(len(self.game.get_board_hidden())):
                    answer_block[i].delete("all")
                    self.switch_draw_answer(self.game.get_board_hidden()[i],i,answer_block)
                self.victory_popup(window,hint_block,color_block,answer_block)
            elif self.game.get_actual_pos() > 10 :
                for i in range(len(self.game.get_board_hidden())):
                    answer_block[i].delete("all")
                    self.switch_draw_answer(self.game.get_board_hidden()[i],i,answer_block)
                self.gameover_popup(window,hint_block,color_block,answer_block)

    def get_victory(self):
        return self.victory

    def victory_popup(self,window,hint_block,color_block,answer_block):
        VICTORY = Toplevel(window)
        VICTORY.title("Victoire")
        VICTORY.config(background = "#050A02")
        VICTORY.geometry("%dx%d+%d+%d" % (500,200,(window.winfo_screenwidth()/2)-100,(window.winfo_screenheight()/2)-200))
        img_victory = Canvas(VICTORY, background = "#050A02", highlightthickness= 0)
        img_victory.place(x = 125, y = 50, height = 100,width = 250)
        img_victory.create_text(125,50,text= "VICTOIRE !",fill = "white")
        Button(VICTORY, text = "Quitter", command = lambda : self.destroy_window(window,VICTORY)).place(x = 275, y = 160, height = 25,width = 75)
        Button(VICTORY, text = "ReJouer", command = lambda : self.reset_window(VICTORY,hint_block,color_block,answer_block)).place(x = 155, y = 160, height = 25,width = 75)
        VICTORY.transient(window)
        VICTORY.grab_set()
        window.wait_window(VICTORY)
        

    def gameover_popup(self,window,hint_block,color_block,answer_block):
        GAMEOVER = Toplevel(window)
        GAMEOVER.title("Game Over")
        GAMEOVER.config(background = "#050A02")
        GAMEOVER.geometry("%dx%d+%d+%d" % (500,200,(window.winfo_screenwidth()/2)-100,(window.winfo_screenheight()/2)-200))
        img_gameover = Canvas(GAMEOVER, background = "#050A02", highlightthickness= 0)
        img_gameover.place(x = 125, y = 50, height = 100,width = 250)
        img_gameover.create_text(125,50,text= "GAME OVER !",fill = "white")
        Button(GAMEOVER, text = "Quitter", command = lambda : self.destroy_window(window,GAMEOVER)).place(x = 275, y = 160, height = 25,width = 75)
        Button(GAMEOVER, text = "ReJouer", command = lambda : self.reset_window(GAMEOVER,hint_block,color_block,answer_block)).place(x = 155, y = 160, height = 25,width = 75)
        GAMEOVER.transient(window)
        GAMEOVER.grab_set()
        window.wait_window(GAMEOVER)

    def destroy_window(self,window,sub_window):
        sub_window.destroy()
        window.destroy()
        sys.exit(0)

    def reset_window(self,sub_window,hint_block,color_block,answer_block):
        sub_window.destroy()
        self.game.reset_board()
        self.game.push_hidden_random()
        for row in range(10):
            for colums in range(4):
                hint_block[row][colums+1].delete("all")
                color_block[row][colums].delete("all")
                hint_block[row][colums+1].create_oval(12.5+5, 12.5+5, 12.5-5, 12.5-5, fill = "#000000")
                color_block[row][colums].create_oval(25+2, 25+2, 25-2, 25-2, fill = "#000000")
        for row in range(4):
            answer_block[row].delete("all")
            answer_block[row].create_oval(25+2, 25+2, 25-2, 25-2, fill = "#FFFFFF")
