from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        '''No parameters.
            Creates scoreboard at top of Screen. Starts at 0.
        '''
        super().__init__()
        self.score = 0
        
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,280)
        self.write_score()
        
        
    def inc_score(self, increment=1):
        '''increment=1 by default.
            Adds increment to score.
            No return.
        '''
        self.score += increment
        self.clear()
        self.write_score()
        
    def write_score(self):
        '''No parameters.
            Writes score to scoreboard.
            No return.
        '''
        self.write(arg=f"Score: {self.score}",
                   move=False,
                   align="center",
                   font=('Arial',12,"bold")
                   )
        
    def game_over(self):
        '''No parameters.
            Writes 'GAME OVER' to centre of screen.
            No return.'''
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align="center", font="Arial")
        