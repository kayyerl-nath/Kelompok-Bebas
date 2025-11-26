from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#e5de00"
FOOD_COLOR = "#de0a26"
BACKGROUND_COLOR = "#000000"

class Snake:
  pass 

class Food:
  pass

def next_turn():
  pass

def change_direction():
  pass

def check_collisiions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print(("GAME OVER"))
            return True
        
    return False

def game_over():
  pass


window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'


label = Label(window, text="Score.{}".format(score), font = ('Consolas'))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.mainloop()
