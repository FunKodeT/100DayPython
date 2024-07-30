#################################################################
#================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FINAL PROGRAM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##---------------------------------------------------------------
## IMPORTS
##---------------------------------------------------------------
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
##---------------------------------------------------------------
## SCREEN SETTINGS
##---------------------------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
##---------------------------------------------------------------
## CREATE ENTITY
##---------------------------------------------------------------
snake = Snake()
food = Food()
scoreboard = Scoreboard()
##---------------------------------------------------------------
## CONTROL SNAKE
##---------------------------------------------------------------
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
##---------------------------------------------------------------
## GAME SETTINGS
##---------------------------------------------------------------
game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_running = False
        scoreboard.game_over()
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            game_is_running = False
            scoreboard.game_over()

##---------------------------------------------------------------
## CODE END
##---------------------------------------------------------------
screen.exitonclick()
##---------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V7 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time
# ##---------------------------------------------------------------
# ## SCREEN SETTINGS
# ##---------------------------------------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)
# ##---------------------------------------------------------------
# ## CREATE ENTITY
# ##---------------------------------------------------------------
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
# ##---------------------------------------------------------------
# ## CONTROL SNAKE
# ##---------------------------------------------------------------
# screen.listen()
# screen.onkey(snake.up, 'Up')
# screen.onkey(snake.down, 'Down')
# screen.onkey(snake.left, 'Left')
# screen.onkey(snake.right, 'Right')
# ##---------------------------------------------------------------
# ## GAME SETTINGS
# ##---------------------------------------------------------------
# game_is_running = True
# while game_is_running:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     # DETECT COLLISION W/FOOD
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()
#     # DETECT COLLISION W/WALL
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_running = False
#         scoreboard.game_over()
#     # DETECT COLLISION W/TAIL
#     for i in snake.segments[1:]:
#         if snake.head.distance(i) < 10:
#             game_is_running = False
#             scoreboard.game_over()

# ##---------------------------------------------------------------
# ## CODE END
# ##---------------------------------------------------------------
# screen.exitonclick()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V6 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time
# ##---------------------------------------------------------------
# ## SCREEN SETTINGS
# ##---------------------------------------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)
# ##---------------------------------------------------------------
# ## CREATE ENTITY
# ##---------------------------------------------------------------
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
# ##---------------------------------------------------------------
# ## CONTROL SNAKE
# ##---------------------------------------------------------------
# screen.listen()
# screen.onkey(snake.up, 'Up')
# screen.onkey(snake.down, 'Down')
# screen.onkey(snake.left, 'Left')
# screen.onkey(snake.right, 'Right')
# ##---------------------------------------------------------------
# ## GAME SETTINGS
# ##---------------------------------------------------------------
# game_is_running = True
# while game_is_running:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     # DETECT COLLISION W/FOOD
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()
#     # DETECT COLLISION W/WALL
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_running = False
#         scoreboard.game_over()
#     # DETECT COLLISION W/TAIL
#     for i in snake.segments:
#         if i == snake.head:
#             pass
#         if snake.head.distance(i) < 10:
#             game_is_running = False
#             scoreboard.game_over()
#     # IF HEAD COLLIDES WITH ANY SEGMENT IN THE TAIL, TRIGGER GAME_OVER

# ##---------------------------------------------------------------
# ## CODE END
# ##---------------------------------------------------------------
# screen.exitonclick()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V5 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time
# ##---------------------------------------------------------------
# ## SCREEN SETTINGS
# ##---------------------------------------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)
# ##---------------------------------------------------------------
# ## CREATE ENTITY
# ##---------------------------------------------------------------
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
# ##---------------------------------------------------------------
# ## CONTROL SNAKE
# ##---------------------------------------------------------------
# screen.listen()
# screen.onkey(snake.up, 'Up')
# screen.onkey(snake.down, 'Down')
# screen.onkey(snake.left, 'Left')
# screen.onkey(snake.right, 'Right')
# ##---------------------------------------------------------------
# ## GAME SETTINGS
# ##---------------------------------------------------------------
# game_is_running = True
# while game_is_running:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     # DETECT COLLISION W/FOOD
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         scoreboard.increase_score()
#     # DETECT COLLISION W/WALL
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_running = False
#         scoreboard.game_over()
# ##---------------------------------------------------------------
# ## CODE END
# ##---------------------------------------------------------------
# screen.exitonclick()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V4 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time
# ##---------------------------------------------------------------
# ## SCREEN SETTINGS
# ##---------------------------------------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)
# ##---------------------------------------------------------------
# ## CREATE ENTITY
# ##---------------------------------------------------------------
# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()
# ##---------------------------------------------------------------
# ## CONTROL SNAKE
# ##---------------------------------------------------------------
# screen.listen()
# screen.onkey(snake.up, 'Up')
# screen.onkey(snake.down, 'Down')
# screen.onkey(snake.left, 'Left')
# screen.onkey(snake.right, 'Right')
# ##---------------------------------------------------------------
# ## GAME SETTINGS
# ##---------------------------------------------------------------
# game_is_running = True
# while game_is_running:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     # DETECT COLLISION W/FOOD
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         scoreboard.increase_score()
# ##---------------------------------------------------------------
# ## CODE END
# ##---------------------------------------------------------------
# screen.exitonclick()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V3 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Screen
# from snake import Snake
# from food import Food
# import time
# ##---------------------------------------------------------------
# ## SCREEN SETTINGS
# ##---------------------------------------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)
# ##---------------------------------------------------------------
# ## CREATE ENTITY
# ##---------------------------------------------------------------
# snake = Snake()
# food = Food()
# ##---------------------------------------------------------------
# ## CONTROL SNAKE
# ##---------------------------------------------------------------
# screen.listen()
# screen.onkey(snake.up, 'Up')
# screen.onkey(snake.down, 'Down')
# screen.onkey(snake.left, 'Left')
# screen.onkey(snake.right, 'Right')
# ##---------------------------------------------------------------
# ## GAME SETTINGS
# ##---------------------------------------------------------------
# game_is_running = True
# while game_is_running:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     # DETECT COLLISION W/FOOD
#     if snake.head.distance(food) < 15:
#         food.refresh()
# ##---------------------------------------------------------------
# ## CODE END
# ##---------------------------------------------------------------
# screen.exitonclick()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V2 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Screen
# from snake import Snake
# from food import Food
# import time
# ##---------------------------------------------------------------
# ## SCREEN SETTINGS
# ##---------------------------------------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)
# ##---------------------------------------------------------------
# ## CREATE ENTITY
# ##---------------------------------------------------------------
# snake = Snake()
# food = Food()
# ##---------------------------------------------------------------
# ## CONTROL SNAKE
# ##---------------------------------------------------------------
# screen.listen()
# screen.onkey(snake.up, 'Up')
# screen.onkey(snake.down, 'Down')
# screen.onkey(snake.left, 'Left')
# screen.onkey(snake.right, 'Right')
# ##---------------------------------------------------------------
# ## GAME SETTINGS
# ##---------------------------------------------------------------
# game_is_running = True
# while game_is_running:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     # DETECT COLLISION W/FOOD
#     if snake.head.distance(food) < 15:
#         print('nom nom nom')
# ##---------------------------------------------------------------
# ## CODE END
# ##---------------------------------------------------------------
# screen.exitonclick()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V1 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Screen, Turtle
# from snake import Snake
# import time
# ##---------------------------------------------------------------
# ## SCREEN SETTINGS
# ##---------------------------------------------------------------
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)
# ##---------------------------------------------------------------
# ## CREATE SNAKE
# ##---------------------------------------------------------------
# snake = Snake()
# ##---------------------------------------------------------------
# ## CONTROL SNAKE
# ##---------------------------------------------------------------
# screen.listen()
# screen.onkey(snake.up, 'Up')
# screen.onkey(snake.down, 'Down')
# screen.onkey(snake.left, 'Left')
# screen.onkey(snake.right, 'Right')
# ##---------------------------------------------------------------
# ## GAME SETTINGS
# ##---------------------------------------------------------------
# game_is_running = True
# while game_is_running:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
# ##---------------------------------------------------------------
# ## CODE END
# ##---------------------------------------------------------------
# screen.exitonclick()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################