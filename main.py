'''
this was made by Saviorizm
Goals - reduce opacity of turtle fill to show colors beneath

'''


import turtle
from random import randint
from settings import *
from ColabTurtlePlus.Turtle import *


pen = turtle.Turtle()
turtle.setup(WIDTH, HEIGHT)
# pen.initializeTurtle()



def draw_random_line(horizontal = False,vertical = False): 
  pen.speed(0) 
  if horizontal:
    pen.penup()
    pen.goto(randint(-WIDTH,WIDTH),HEIGHT)
    pen.begin_fill()
    pen.fillcolor(randint(1, 255)/255, randint(1, 255)/255, randint(1, 255)/255)
    # pen.fillcolor(r,g,b,a)
    # pen.setfillopacity(45)
    xpos_one, ypos_one = pen.position()
    pen.pendown()
    pen.goto(randint(-WIDTH,WIDTH),-HEIGHT)
    xpos_two, ypos_two = pen.position()
    
    if xpos_one - WIDTH/2 > 0:
      closer_top = "right"
      print(closer_top)
    else:
      closer_top = "left"
      print(closer_top)

    if xpos_two - WIDTH/2 > 0:
      closer_bottom = "right"
      print(closer_bottom)
    else:
      closer_bottom = "left"
      print(closer_bottom)
    if closer_top == "right":
      pen.goto(WIDTH/2,-HEIGHT/2)
      pen.goto(WIDTH/2,HEIGHT/2)
      pen.end_fill()
    if closer_top == "left":
      pen.goto(-WIDTH/2,-HEIGHT/2)
      pen.goto(-WIDTH/2,HEIGHT/2)
      pen.end_fill()
  

  if vertical:
    pen.penup()
    pen.goto(-WIDTH,randint(-HEIGHT,HEIGHT))
    pen.begin_fill()
    pen.fillcolor(randint(1, 255)/255, randint(1, 255)/255, randint(1, 255)/255)
    # pen.setfillopacity(45)
    xpos_one, ypos_one = pen.position()
    pen.pendown()
    pen.goto(HEIGHT,randint(-HEIGHT,HEIGHT))
    xpos_two, ypos_two = pen.position()

    if ypos_one - HEIGHT/2 > 0:
      closer_left = "top"
      print(closer_left)
    else:
      closer_left = "bottom"
      print(closer_left)

    if ypos_two - HEIGHT/2 > 0:
      closer_right = "top"
      print(closer_right)
    else:
      closer_right = "bottom"
      print(closer_right)
    if closer_left == "top":
      pen.goto(WIDTH/2,HEIGHT/2)
      pen.goto(-WIDTH/2,HEIGHT/2)
      pen.end_fill()
    if closer_right == "bottom":
      pen.goto(WIDTH/2,-HEIGHT/2)
      pen.goto(-WIDTH/2,-HEIGHT/2)
      pen.end_fill()

for i in range(100):
  draw_random_line(True)
  # print("Horizontal line")
for i in range(100):
  draw_random_line(False, True)
  # print("vertical line")

turtle.done()
