#################################################################
#================================================================
#----------------------------------------------------------------
# TURTLE RACING
#----------------------------------------------------------------
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM4_V3 = {
# #================================================================
# #----------------------------------------------------------------
# from turtle import Turtle, Screen
# import random
# #----------------------------------------------------------------
# # SCREEN
# #----------------------------------------------------------------
# is_race_on = False

# screen = Screen()
# screen.setup(width=500, height=400)

# def turtle_game():
#     #----------------------------------------------------------------
#     # BET FUNCTIONS
#     #----------------------------------------------------------------
#     def user_bet():
#         user_bet = screen.textinput(title='How do you want to do this?', prompt="Would you like to bet based on 'name' or 'color':")
#         if user_bet.title() == 'Name':
#             user_bet = screen.textinput(title='Make your bet!', prompt="Timmy, Jimmy, Timothy, Jimothy, Tim, or Jim?")
#             return user_bet
#         else:
#             user_bet = screen.textinput(title='Make your bet!', prompt="Red, Orange, Yellow, Green, Blue, or Purple?")
#             return user_bet
#     #----------------------------------------------------------------
#     # TURTLES
#     #----------------------------------------------------------------
#     colors = ["red", "orange", "yellow", "green", "blue", "purple"]
#     names = ['Tim', 'Jim', 'Timmy', 'Jimmy', 'Timothy', 'Jimothy']

#     y_positions  = [-125, -75, -25, 25, 75, 125]

#     turtles = {}

#     for turtle_index in range(0, 6):
#         turtles[turtle_index] = [names[turtle_index]]
#         turt = Turtle(shape='turtle')
#         turt.color(colors[turtle_index])
#         turt.penup()
#         turt.setposition(x=-240, y=y_positions[turtle_index])
#         turt.write(arg=turtles[turtle_index])
#         turt.goto(x=-240, y=y_positions[turtle_index])
#         turt.pendown()
#         [turtles[turtle_index]] = [turt]
#         print(turt)

#     bet_value = user_bet()
#     print(bet_value)

#     if bet_value:
#         is_race_on = True

#     print(turtles)

#     while is_race_on:
#         for index in turtles:
#             if turtles[index].xcor() > 230:
#                 winner = turtles[index].pencolor()
#                 if winner == bet_value:
#                     is_race_on = False
#                     exit_or_not = screen.textinput(title=f"Winner! Your turtle, {winner}, was the fastest!", prompt="Would you like to play again? 'y' to play again, 'n' to exit:")
#                     if exit_or_not == 'n':
#                         is_race_on = False
#                         screen.bye()
#                     else:
#                         screen.clear()
#                         turtle_game()
#                 else:
#                     exit_or_not = screen.textinput(title=f"Loser! Turtle, {winner}, was the fastest!", prompt="Would you like to play again? 'y' to play again, 'n' to exit:")
#                     if exit_or_not == 'n':
#                         is_race_on = False
#                         screen.bye()
#                     else:
#                         screen.clear()
#                         turtle_game()
                
#             random_distance = random.randint(0, 10)
#             turtles[index].forward(random_distance)
    
# while screen.textinput(title='Want to bet on some Turtles?', prompt="Type 'y' to play, 'n' to exit:") == 'y':
#     screen.clear()
#     turtle_game()

# #----------------------------------------------------------------
# screen.exitonclick()
# #----------------------------------------------------------------
# #================================================================
}
#----------------------------------------------------------------
PROGRAM4_V2 = {
# #================================================================
# #----------------------------------------------------------------
# from turtle import Turtle, Screen
# import random
# #----------------------------------------------------------------
# # SCREEN
# #----------------------------------------------------------------
# screen = Screen()
# screen.setup(width=500, height=400)
# is_race_on = False
# #----------------------------------------------------------------
# # BET FUNCTIONS
# #----------------------------------------------------------------
# user_bet = screen.textinput(title='Make your bet!', prompt="Red, Orange, Yellow, Green, Blue, or Purple?")
# #----------------------------------------------------------------
# # TURTLES
# #----------------------------------------------------------------
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# y_positions  = [-125, -75, -25, 25, 75, 125]
# turtle_names = []

# for turtle_index in range(0, 6):
#     turt = Turtle(shape='turtle')
#     turt.color(colors[turtle_index])
#     turt.penup()
#     turt.goto(x=-240, y=y_positions(turtle_index))
#     turtle_names.append(turt)

# if user_bet:
#     is_race_on = True

# while is_race_on:
#     for index in turtle_names:
#         if index.xcor() > 230:
#             print(index.color())
#         random_distance = random.randint(0, 10)
#         index.forward(random_distance)

# #----------------------------------------------------------------
# screen.exitonclick()
# #----------------------------------------------------------------
# #================================================================
}
#----------------------------------------------------------------
PROGRAM4_V1 = {
# #================================================================
# #----------------------------------------------------------------
# from turtle import Turtle, Screen
# #----------------------------------------------------------------
# # SCREEN
# #----------------------------------------------------------------
# screen = Screen()
# screen.setup(width=500, height=400)
# #----------------------------------------------------------------
# # BET FUNCTIONS
# #----------------------------------------------------------------
# bet_choice = screen.textinput(title='How do you want to do this?', prompt="Would you like to bet based on 'name' or 'color':")
# if bet_choice.title == 'Name':
#     screen.textinput(title='Make your bet!', prompt="Timmy, Jimmy, Timothy, Jimothy, Tim, or Jim?")
# elif bet_choice.title == 'Turtle':
#     screen.textinput(title='Make your bet!', prompt="Red, Orange, Yellow, Green, Blue, or Purple?")
# else:
#     play_or_not = screen.textinput(title='You must make a bet to play.', prompt="Do you want to make a bet? Enter 'y' to keep playing, 'n' to exit:")
#     if play_or_not.title == 'Y':

# #----------------------------------------------------------------
# # TURTLES
# #----------------------------------------------------------------
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# names = ['timmy', 'jimmy', 'timothy', 'jimothy', 'tim', 'jim']

# y_positions  = [-125, -75, -25, 25, 75, 125]

# if bet_choice == 'name':
#     for turtle_index in range(0, 6):
#         timmy = Turtle(shape='turtle')
#         timmy.color(colors[turtle_index])
#         timmy.penup()
#         timmy.goto(x=-240, y=y_positions(turtle_index))
# else:
#     for turtle_index in range(0, 6):
#         timmy = Turtle(shape='turtle')
#         timmy.color(colors[turtle_index])
#         timmy.penup()
#         timmy.goto(x=-240, y=y_positions(turtle_index))


# #----------------------------------------------------------------
# screen.exitonclick()
# #----------------------------------------------------------------
# #================================================================
}
#----------------------------------------------------------------
PROGRAM4_V0 = {
#----------------------------------------------------------------
# #================================================================
# #----------------------------------------------------------------
# from turtle import Turtle, Screen
# #----------------------------------------------------------------
# # SCREEN
# #----------------------------------------------------------------
# screen = Screen()
# screen.setup(width=500, height=400)
# #----------------------------------------------------------------
# # BET FUNCTIONS
# #----------------------------------------------------------------
# bet_choice = screen.textinput(title='How do you want to do this?', prompt="Would you like to bet based on 'name' or 'color':")
# if bet_choice == 'name':
#     screen.textinput(title='Make your bet!', prompt="timmy, jimmy, timothy, jimothy, tim, or jim:")
# else:
#     screen.textinput(title='Make your bet!', prompt="red, orange, yellow, green, blue, or purple:")
# #----------------------------------------------------------------
# # TURTLES
# #----------------------------------------------------------------
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# timmy = Turtle(shape='turtle')
# timmy.color(colors[0])
# timmy.penup()
# timmy.goto(x=-240, y=125)

# jimmy = Turtle(shape='turtle')
# jimmy.color(colors[1])
# jimmy.penup()
# jimmy.goto(x=-240, y=75)

# timothy = Turtle(shape='turtle')
# timothy.color(colors[2])
# timothy.penup()
# timothy.goto(x=-240, y=25)

# jimothy = Turtle(shape='turtle')
# jimothy.color(colors[3])
# jimothy.penup()
# jimothy.goto(x=-240, y=-25)

# tim = Turtle(shape='turtle')
# tim.color(colors[4])
# tim.penup()
# tim.goto(x=-240, y=-75)

# jim = Turtle(shape='turtle')
# jim.color(colors[5])
# jim.penup()
# jim.goto(x=-240, y=-125)
# #----------------------------------------------------------------
# screen.exitonclick()
# #----------------------------------------------------------------
#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM3_V3 = {
# ----------------------------------------------------------------
#================================================================

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_left():
#     tim.lt(10)

# def turn_right():
#     tim.rt(10)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forward, 'w')
# screen.onkey(move_backward, 's')
# screen.onkey(turn_left, 'a')
# screen.onkey(turn_right, 'd')
# screen.onkey(clear, 'c')

# screen.exitonclick()

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V2 = {
# ----------------------------------------------------------------
#================================================================

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# screen.listen()
# screen.onkey(move_forward, 'w')
# screen.onkey(move_backward, 's')
# screen.onkey(turn_left, 'a')
# screen.onkey(turn_right, 'd')
# screen.exitonclick()

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V1 = {
#----------------------------------------------------------------
#================================================================

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)
    
# screen.listen()
# screen.onkey(key='space', fun=move_forward)
# screen.exitonclick()

# [TURTLE WINDOW POPS UP, CAN PRESS SPACE TO MOVE SPRITE FORWARD]
#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V0 = {
#----------------------------------------------------------------
#================================================================
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)
    
# screen.listen()
# screen.onkey(key='space', fun=move_forward())

# # ERROR

#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM2_V1 = {
#================================================================
# def my_function(a, b, c):
#     # DO THIS WITH
#     a
#     # THEN DO THIS WITH
#     b
#     # FINALLY DO THIS WITH
#     c

# my_function(1, 2, 3)
#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V0 = {
#================================================================
# def my_function(a, b, c):
#     # DO THIS WITH
#     a
#     # THEN DO THIS WITH
#     b
#     # FINALLY DO THIS WITH
#     c

# my_function(c=3, a=1, b=2)
#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM1_V2 = {
#================================================================

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# def calculator(n1, n2, func):
#     return func(n1, n2)

# result = calculator(2, 3, divide)
# print(result)

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V1 = {
#================================================================

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# def calculator(n1, n2, func):
#     return func(n1, n2)

# result = calculator(2, 3, multiply)
# print(result)

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V0 = {
#================================================================

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# def calculator(n1, n2, func):
#     return func(n1, n2)

# result = calculator(2, 3, add)
# print(result)

#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM0_V0 = {
#================================================================
# def function_a(something):
#     # DO THIS WITH 
#     SOMETHING
#     # THEN DO THIS
#     # FINALLY DO THIS

# def function_b():
#     # DO THIS

# function_a(function_b)
#================================================================
#----------------------------------------------------------------
}
#----------------------------------------------------------------
#================================================================
#################################################################

#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
# PROGRAM#_V# = {
#================================================================

#================================================================
# }
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------