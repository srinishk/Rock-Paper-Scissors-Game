from tkinter import *
from random import randint

win = Tk()
win.title("Rock, Paper, Scissors")
win.geometry("400x300")


global comp
num = randint(1,3)

if num == 1:
  comp = "ROCK"
elif num == 2:
  comp = "PAPER"
else:
  comp = "SCISSORS"

def compare1(pc):
  if pc == comp:
    lbl.config(text = f"Player choice is {pc} \nComputer choice is {comp}.\n Result is a Tie!")

  elif pc == "ROCK" and comp == "PAPER":
    lbl.config(text = f"Player choice is {pc} \nComputer choice is {comp}.\n You have lost.")

  elif pc == "ROCK" and comp == "SCISSORS":
    lbl.config(text = f"Player choice is {pc} \nComputer choice is {comp}.\n You won!")

  elif pc == "PAPER" and comp == "ROCK":
    lbl.config(text = f"Player choice is {pc} \nComputer choice is {comp}.\n You won!")

  elif pc == "PAPER" and comp == "SCISSORS":
    lbl.config(text = f"Player choice is {pc} \nComputer choice is {comp}.\n You have lost.")

  elif pc == "SCISSORS" and comp == "ROCK":
    lbl.config(text = f"Player choice is {pc} \nComputer choice is {comp}.\n You have lost.")

  elif pc == "SCISSORS" and comp == "PAPER":
    lbl.config(text = f"Player choice is {pc} \nComputer choice is {comp}.\n You won!")
  
  else:
    lbl.config(text = "Error")



def rock():
  compare1("ROCK")

def paper():
  compare1("PAPER")

def scissors():
  compare1("SCISSORS")
  

br = Button(win, text = "ROCK", width = 30, height = 3, command = rock)
bp = Button(win, text = "PAPER", width = 30, height = 3, command = paper)
bs = Button(win, text = "SCISSORS", width = 30, height = 3, command = scissors)

lbl = Label(win, text = comp, width = 30, height = 3)

br.pack(pady = 5)
bp.pack(pady = 5)
bs.pack(pady = 5)
lbl.pack()

win.mainloop()