#################################################################
#================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FINAL PROGRAM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##---------------------------------------------------------------
## IMPORTS
##---------------------------------------------------------------
from turtle import Turtle
##---------------------------------------------------------------
## CONSTANTS
##---------------------------------------------------------------
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
##---------------------------------------------------------------
## SNAKE CLASS
##---------------------------------------------------------------
class Snake:
    ##---------------------------------------------------------------
    ## INITIALIZE SNAKE FUNCTIONS
    ##---------------------------------------------------------------
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    ##---------------------------------------------------------------
    ## CREATE SNAKE SEGMENTS
    ##---------------------------------------------------------------
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    ##---------------------------------------------------------------
    ## ADD SNAKE SEGMENTS
    ##---------------------------------------------------------------
    def add_segment(self, position):
            if self.segments == []:
                new_segment = Turtle(shape='triangle')
                new_segment.tilt(180)
                new_segment.color('red')
                new_segment.penup()
                new_segment.goto(position)
                self.segments.append(new_segment)
            else:
                new_segment = Turtle('square')
                new_segment.color('green')
                new_segment.penup()
                new_segment.goto(position)
                self.segments.append(new_segment)
    ##---------------------------------------------------------------
    ## EXTEND SNAKE SEGMENTS
    ##---------------------------------------------------------------
    def extend(self):
        # ADD A NEW SEGMENT TO THE SNAKE
        self.add_segment(self.segments[-1].position())
    ##---------------------------------------------------------------
    ## MOVE SNAKE SEGMENTS
    ##---------------------------------------------------------------
    def move(self):
        """
            Moves the snake based on user input.
        """
        for i in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    ##---------------------------------------------------------------
    ## CONTROL SNAKE -> UP
    ##---------------------------------------------------------------
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    ##---------------------------------------------------------------
    ## CONTROL SNAKE -> DOWN
    ##---------------------------------------------------------------
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    ##---------------------------------------------------------------
    ## CONTROL SNAKE -> LEFT
    ##---------------------------------------------------------------
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    ##---------------------------------------------------------------
    ## CONTROL SNAKE -> RIGHT
    ##---------------------------------------------------------------
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
##---------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V1 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## CONSTANTS
# ##---------------------------------------------------------------
# STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
# ##---------------------------------------------------------------
# ## SNAKE CLASS
# ##---------------------------------------------------------------
# class Snake:
#     ##---------------------------------------------------------------
#     ## INITIALIZE SNAKE FUNCTIONS
#     ##---------------------------------------------------------------
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
#     ##---------------------------------------------------------------
#     ## CREATE SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)

#     ##---------------------------------------------------------------
#     ## ADD SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def add_segment(self, position):
#             if self.segments == []:
#                 new_segment = Turtle(shape='triangle')
#                 new_segment.tilt(180)
#                 new_segment.color('red')
#                 new_segment.penup()
#                 new_segment.goto(position)
#                 self.segments.append(new_segment)
#             else:
#                 new_segment = Turtle('square')
#                 new_segment.color('green')
#                 new_segment.penup()
#                 new_segment.goto(position)
#                 self.segments.append(new_segment)
#     ##---------------------------------------------------------------
#     ## EXTEND SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def extend(self):
#         # ADD A NEW SEGMENT TO THE SNAKE
#         self.add_segment(self.segments[-1].position())
#     ##---------------------------------------------------------------
#     ## MOVE SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def move(self):
#         """
#             Moves the snake based on user input.
#         """
#         for i in range(len(self.segments) -1, 0, -1):
#             new_x = self.segments[i - 1].xcor()
#             new_y = self.segments[i - 1].ycor()
#             self.segments[i].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> UP
#     ##---------------------------------------------------------------
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> DOWN
#     ##---------------------------------------------------------------
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> LEFT
#     ##---------------------------------------------------------------
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> RIGHT
#     ##---------------------------------------------------------------
#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V0 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## CONSTANTS
# ##---------------------------------------------------------------
# STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
# ##---------------------------------------------------------------
# ## SNAKE CLASS
# ##---------------------------------------------------------------
# class Snake:
#     ##---------------------------------------------------------------
#     ## INITIALIZE SNAKE FUNCTIONS
#     ##---------------------------------------------------------------
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
#     ##---------------------------------------------------------------
#     ## CREATE SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)

#     ##---------------------------------------------------------------
#     ## ADD SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def add_segment(self, position):
#             new_segment = Turtle('square')
#             new_segment.color('white')
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)
#     ##---------------------------------------------------------------
#     ## EXTEND SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def extend(self):
#         # ADD A NEW SEGMENT TO THE SNAKE
#         self.add_segment(self.segments[-1].position())
#     ##---------------------------------------------------------------
#     ## MOVE SNAKE SEGMENTS
#     ##---------------------------------------------------------------
#     def move(self):
#         """
#             Moves the snake based on user input.
#         """
#         for i in range(len(self.segments) -1, 0, -1):
#             new_x = self.segments[i - 1].xcor()
#             new_y = self.segments[i - 1].ycor()
#             self.segments[i].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> UP
#     ##---------------------------------------------------------------
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> DOWN
#     ##---------------------------------------------------------------
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> LEFT
#     ##---------------------------------------------------------------
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)
#     ##---------------------------------------------------------------
#     ## CONTROL SNAKE -> RIGHT
#     ##---------------------------------------------------------------
#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################




