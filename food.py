from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        '''No parameters.
            Creates food turtle in random location
        '''
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.move_rand()
        
    def move_rand(self):
        '''No parameters.
            Returns random (x,y) coordinates between -280 and 280
        '''
        self.goto(
            random.randint(-280, 280), 
            random.randint(-280, 280)
            )
        
