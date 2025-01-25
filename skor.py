from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore() 
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.ubdate_scoreboard()
        
        
    def ubdate_scoreboard(self):
        self.write(f"score: {self.score}  high score:{self.highscore}", align="center" , font=("Arial" , 24 , "normal"))    
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.ubdate_scoreboard()    
        
    def gem_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()#حفظ أعلى نتيجة عند انتهاء اللعبة
        
        self.write(f"------------- Game Over -------------\n\nfinal Score: {self.score}\n\n High score: {self.highscore}" , align="center" , font=("Arial" , 24 , "normal"))
            
    #حفظ أعلى نتيجة في ملف      
    def save_highscore(self):
        with open ("date.txt" , "w") as my_file:
            my_file.write(str(self.highscore)) 
               
    def read_highscore(self):
        """قراءة أعلى نتيجة من ملف"""
        try:
            with open("date.txt", "r") as my_file:
                return int(my_file.read())
        except FileNotFoundError:
            return 0        
            
            
# from turtle import Turtle , Screen
# from snak import Snake
# from food import Food
# import time
# from skor import Score



# window = Screen()
# window.setup(800,800)
# window.bgcolor("black")
# window.title("SNAKE GEM")
# window.tracer(0)

# sam = Snake()
# food = Food()
# score = Score()
# #sam.move()

# gem_on = True

# while gem_on:
#   sam.move()
#   window.update()
#   time.sleep(0.1)
#   window.listen()
#   window.onkey(sam.up,"Up")
#   window.onkey(sam.down,"Down")
#   window.onkey(sam.right,"Right")
#   window.onkey(sam.left,"Left")
#   if sam.head.distance(food) <15:
#     food.appear()
#     sam.extent()
#     score.increase_score()
    
#   if sam.head.xcor() > 370 or sam.head.xcor() < -370 or sam.head.ycor() > 370 or sam.head.ycor() < -370 :
#     gem_on = False
#     score.gem_over()















# window.exitonclick()            
            
            