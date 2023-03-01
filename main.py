from turtle import Screen
import time
from snek import Snek
from food import Food
from scoreboard import Scoreboard

'''WALL constants define boundaries of game'''
LEFT_WALL = -280
RIGHT_WALL = 280
TOP_WALL = 280
BOTTOM_WALL = -280

'''Screen setup'''
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek :)=<")
screen.tracer(0)

'''Game objects setup'''
snek = Snek()
food = Food()
scoreboard = Scoreboard()

'''Listeners setup'''
screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

screen.update()


'''Starts game'''
game_on = True
while game_on:
    #move snek 20 pixels in direction of head
    snek.move()
    time.sleep(0.1)
    screen.update()
    
    #check if snake head contacts wall
    if not( (LEFT_WALL < snek.head.xcor() < RIGHT_WALL) and (BOTTOM_WALL < snek.head.ycor() < TOP_WALL) ):
        game_on = False
        
    
    #check if snake head conacts food
    if snek.head.distance(food) <= 15:
        food.move_rand()
        snek.add_segment()
        scoreboard.inc_score()
    
    #checks if shake head has collided with body
    if snek.check_collision():
        game_on = False

#When loop exits, prints game over to centre of screen
scoreboard.game_over()


screen.exitonclick()
