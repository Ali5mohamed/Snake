from turtle import Turtle

class Snake:
    
    def __init__(self):
        self.turtles = []
        self.positans = [(-40,0) , (-20,0) , (0,0)]
        self.cret_snake()
        self.head = self.turtles[-1]
        
        
    def cret_snake(self):
        for i in  range(len(self.positans)):
        
            new_snake = Turtle("square")  
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(self.positans[i]) 
            self.turtles.append(new_snake) 
            
            
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i +1].pos()) 
            
        self.head.forward(20)
        
    def extent(self):
        new =Turtle("square")  
        new.color("white")
        new.penup()
        new.goto(self.turtles[0].pos())
        self.turtles.insert(0,new)
            
    def up(self):
        self.head.setheading(90)
                
    def down(self):
        self.head.setheading(270) 
               
    def right(self):
        self.head.setheading(0)    
            
    def left(self):
        self.head.setheading(180)        