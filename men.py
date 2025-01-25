from turtle import Turtle , Screen
from snak import Snake
from food import Food
import time
from skor import Score
import pandas




window = Screen()
window.setup(800,800)
window.bgcolor("black")
window.title("SNAKE GEM")
window.tracer(0)

sam = Snake()
food = Food()
score = Score()
#sam.move()

gem_on = True

while gem_on:
  sam.move()
  window.update()
  time.sleep(0.1)
  window.listen()
  window.onkey(sam.up,"Up")
  window.onkey(sam.down,"Down")
  window.onkey(sam.right,"Right")
  window.onkey(sam.left,"Left")
  if sam.head.distance(food) <15:
    food.appear()
    sam.extent()
    score.increase_score()
    
  if sam.head.xcor() > 370 or sam.head.xcor() < -370 or sam.head.ycor() > 370 or sam.head.ycor() < -370 :
    gem_on = False
    score.gem_over()
  for i in sam.turtles[:-1]:
    if sam.head.distance(i) < 10:
        gem_on = False
        score.gem_over()















window.exitonclick()            
            
            