import time
import turtle
from turtle import Screen
from player import Player
from car_generator import CarGenerator
from scoreboard import Scoreboard

screen = Screen()
screen.title("Tortuguita's Adventure")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_generator = CarGenerator()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
scoreboard.prior_game()

def initialize_game():
    scoreboard.start_game()
    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()
        scoreboard.update_scoreboard()

        car_generator.create_car()
        car_generator.move_car()

        # TODO: Detect collision with car
        for car in car_generator.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
                screen.onkey(screen.bye, "space")

        # TODO: Detect level up (Successfully crossed road)
        if player.successful_cross():
            player.go_to_start()
            car_generator.level_up()
            scoreboard.increase_level()

screen.onkey(initialize_game, "space")

turtle.done()