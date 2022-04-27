from turtle import Turtle
from scoreboard import Scoreboard
import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    
    def __init__(self):
      
      super().__init__()
      self.create_car()
    def create_car(self):
      self.color(random.choice(COLORS))
      self.penup()
      self.shape("square")
      self.setheading(180)
      self.shapesize(1,3)
      self.speed=5
      self.goto(300,random.randint(-250,250))
    def drive(self):
      self.forward(self.speed)
   
    
    
