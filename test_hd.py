from turtle import Turtle, Screen 
from snek import Snek

screen = Screen()
head = Turtle()



def up():
    head.seth(90)
    head.fd(20)

def down():
    head.seth(270)
    head.fd(20)

def left():
    head.seth(180)
    head.fd(20)
    
def right():
    head.seth(0)
    head.fd(20)

screen.listen()
screen.onkey(fun=up, key="w")
screen.onkey(fun=down, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")











screen.exitonclick() 