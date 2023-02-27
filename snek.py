from turtle import Turtle


RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

class Snek:
    
    def __init__(self):
        self.segments = self.make_snek()
        self.head = self.segments[0]
        
        
    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.fd(20)
      
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    
        
    
    def make_snek(self):
        x,y = 0,0
        snek = []
        for _ in range(3):
            seg = Turtle("square")
            seg.color("white")
            seg.pensize(20)
            seg.penup()
            seg.goto(x,y)
            snek.append(seg)
            x -= 20
            
        return snek