FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
      super().__init__()
      self.hideturtle()
      self.penup()
      
      self.level=1

    def show(self):
      self.goto(-270,250)
      self.write(f"Level: {self.level}","center", font=FONT)
      
