from turtle import Turtle

#directional constants
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

class Snek:
    
    def __init__(self):
        '''No parameters.
            Creates snek of length 3'''
        self.segments = self.make_snek()
        self.head = self.segments[0]
         
    def move(self):
        '''No parameters.
            Moves snek 20 pixels in direction of snek.head.
            No return.
        '''
        for segment in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.fd(20)
      
    
    def up(self):
        '''No parameters.
            Points snek head up.
            No return.
        '''
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def down(self):
        '''No parameters.
            Points snek head down.
            No return.
        '''
        if self.head.heading() != UP:
            self.head.seth(DOWN)
        
    def left(self):
        '''No parameters.
            Points snek head left.
            No return.
        '''
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
        
    def right(self):
        '''No parameters.
            Points snek head right.
            No return.
        '''
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    
        
    def check_collision(self):
        '''No parameters.
            Returns True if shake head has collided with body. 
            Returns False if not.
        '''
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
    
    def add_segment(self):
        '''No parameters.
            Add one segment to the end of this snek.
            No return.
        '''
        seg = Turtle("square")
        seg.color("white")
        seg.pensize(20)
        seg.penup()
        self.segments.append(seg)
    
    def make_snek(self):
        '''No parameters.
            Returns snek of length 3
        '''
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