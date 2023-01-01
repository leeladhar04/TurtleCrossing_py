from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANGE_X=(-350,350)
RANGE_Y=(-260,320)


class CarManager():
    def __init__(self):
        self.allcars=[]


    def car(self):
        random_chance=random.randint(1,8)
        if random_chance==1 or random_chance==3:

            car=Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=1.9)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(random.randint(340, 350), random.randint(-250, 320))
            self.allcars.append(car)


    def move(self,val):
        for car in self.allcars:
            new_x=car.xcor()-val
            new_pos=(new_x,car.ycor())
            car.goto(new_pos)







