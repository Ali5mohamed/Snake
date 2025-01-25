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
            
            
