import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle=Player()
screen.onkey(fun=turtle.move_up,key="Up")

game_is_on = True
list_of_cars=[]
scoreboard=Scoreboard()
scoreboard.show()
new_car=CarManager()
list_of_cars.append(new_car)
level=1
while game_is_on:
  if list_of_cars[-1].xcor()<270:
    new_car=CarManager()
    list_of_cars.append(new_car)
  for _ in range (1,level):
    new_car.speed+=1
  for car in list_of_cars:
    car.drive()
    #detect if hit
    if turtle.distance(car)<40:
      if turtle.ycor()<car.ycor() and car.ycor()-turtle.ycor()<25:
        game_is_on=False
      if car.ycor()<turtle.ycor() and turtle.ycor()-car.ycor()<18:
        game_is_on=False
      if turtle.ycor()==car.ycor():
        game_is_on=False
      
  time.sleep(0.1)
  #detect if passed level
  if turtle.ycor()>280:
    turtle.start_over()
    scoreboard.level+=1
    scoreboard.clear()
    scoreboard.show()
    level+=1
  
  
    
    
  
  
  screen.update()
  
  
