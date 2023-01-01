import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager=CarManager()
player=Player()
scoreboard=Scoreboard()
scoreboard.display_score()

times=0

screen.listen()
screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_down,"Down")



game_is_on = True
val=5
while game_is_on:
    time.sleep(0.04)
    times+=1
    screen.update()
    car_manager.car()
    car_manager.move(val)

    for car in car_manager.allcars:
        if  car.distance(player)<20:
            game_is_on=False
            soreboard.game_over()
            break

    if player.ycor()>280:
        player.reset()
        scoreboard.increase_level()
        val+=5






screen.exitonclick()
