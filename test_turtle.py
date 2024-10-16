##from turtle import *
##s = Screen(); t = Turtle()
##color = input("What color would you like the pen to be?\n")
##t.fillcolor(color)
##t.color(color)
##t.width(10)
##s.listen()
##ondrag(t.goto)
##mainloop()

import turtle
from turtle import Screen, Turtle

screen = Screen()
t = Turtle("turtle")
t.speed(-1)
color = input("What color would you like the pen to be?\n")
t.fillcolor(color)
t.color(color)
t.width(10)

def dragging(x, y):  # These parameters will be the mouse position
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight():
    t.clear()

def main():  # This will run the program
    turtle.listen()
    
    t.ondrag(dragging)  # When we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()  # This will continue running main() 

main()
