from project.mastermind import Mastermind
from project.callback import Callback
from tkinter import *

game = Mastermind()
callback = Callback(game)

ROOT = Tk()

hs = ROOT.winfo_screenheight()
ws = ROOT.winfo_screenwidth()

ROOT.configure(background = '#050A02')
ROOT.title("Mastermind")
ROOT.geometry('%dx%d' %(ws,hs)) 

Button(ROOT, text = "Test the line", command = lambda : callback.victory_condition(hint_block,answer_block,color_block,ROOT)).place(relx = 0.45, rely = 0.3)
Button(ROOT, text = "Erase the line", command = lambda : callback.erase_row(color_block)).place(relx = 0.45, rely = 0.4)

number_block = callback.define_number(ROOT)
color_block = callback.define_color(ROOT)
hint_block = callback.define_hint(ROOT)
buttons_block = callback.button_color(ROOT,color_block)
answer_block = callback.define_answer(ROOT)

game.push_hidden_random()

ROOT.mainloop()
