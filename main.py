from turtle import Screen, Turtle
import time
from snek import Snek

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek :)=<")
screen.tracer(0)

snek = Snek()
screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

screen.update()


game_on = True
while game_on:
    snek.move()
    time.sleep(0.1)
    screen.update()











screen.exitonclick()
