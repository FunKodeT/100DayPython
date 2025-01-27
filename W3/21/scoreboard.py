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
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
##---------------------------------------------------------------
## SCOREBOARD CLASS
##---------------------------------------------------------------
class Scoreboard(Turtle):
    ##---------------------------------------------------------------
    ## DEFINE SCORE
    ##---------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()    
    ##---------------------------------------------------------------
    ## DEFINE UPDATE SCORE
    ##---------------------------------------------------------------
    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    ##---------------------------------------------------------------
    ## DEFINE GAME OVER
    ##---------------------------------------------------------------
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
    ##---------------------------------------------------------------
    ## DEFINE INCREASE SCORE
    ##---------------------------------------------------------------
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
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
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## CONSTANTS
# ##---------------------------------------------------------------
# ALIGNMENT = 'center'
# FONT = ('Courier', 24, 'normal')
# ##---------------------------------------------------------------
# ## SCOREBOARD CLASS
# ##---------------------------------------------------------------
# class Scoreboard(Turtle):
#     ##---------------------------------------------------------------
#     ## DEFINE SCORE
#     ##---------------------------------------------------------------
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color('white')
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()    
#     ##---------------------------------------------------------------
#     ## DEFINE UPDATE SCORE
#     ##---------------------------------------------------------------
#     def update_scoreboard(self):
#         self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
#     ##---------------------------------------------------------------
#     ## DEFINE GAME OVER
#     ##---------------------------------------------------------------
#     def game_over(self):
#         self.goto(0, 0)
#         self.write('GAME OVER', align=ALIGNMENT, font=FONT)
#     ##---------------------------------------------------------------
#     ## DEFINE INCREASE SCORE
#     ##---------------------------------------------------------------
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V6 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## CONSTANTS
# ##---------------------------------------------------------------
# ALIGNMENT = 'center'
# FONT = ('Courier', 24, 'normal')
# ##---------------------------------------------------------------
# ## SCOREBOARD CLASS
# ##---------------------------------------------------------------
# class Scoreboard(Turtle):
#     ##---------------------------------------------------------------
#     ## DEFINE SCORE
#     ##---------------------------------------------------------------
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color('white')
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()    
#     ##---------------------------------------------------------------
#     ## DEFINE UPDATE SCORE
#     ##---------------------------------------------------------------
#     def update_scoreboard(self):
#         self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
#     ##---------------------------------------------------------------
#     ## DEFINE INCREASE SCORE
#     ##---------------------------------------------------------------
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V5 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## CONSTANTS
# ##---------------------------------------------------------------
# ALIGNMENT = 'center'
# FONT = ('Arial', 24, 'normal')
# ##---------------------------------------------------------------
# ## SCOREBOARD CLASS
# ##---------------------------------------------------------------
# class Scoreboard(Turtle):
#     ##---------------------------------------------------------------
#     ## DEFINE SCORE
#     ##---------------------------------------------------------------
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color('white')
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()    
#     ##---------------------------------------------------------------
#     ## DEFINE UPDATE SCORE
#     ##---------------------------------------------------------------
#     def update_scoreboard(self):
#         self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
#     ##---------------------------------------------------------------
#     ## DEFINE INCREASE SCORE
#     ##---------------------------------------------------------------
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()
# ##---------------------------------------------------------------
# ## RESULTS
# ##---------------------------------------------------------------
# # WARNING: WORKS BUT CHANGE FONT
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V4 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## SCOREBOARD CLASS
# ##---------------------------------------------------------------
# class Scoreboard(Turtle):
#     ##---------------------------------------------------------------
#     ## DEFINE SCORE
#     ##---------------------------------------------------------------
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color('white')
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()    
#     ##---------------------------------------------------------------
#     ## DEFINE UPDATE SCORE
#     ##---------------------------------------------------------------
#     def update_scoreboard(self):
#         self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
#     ##---------------------------------------------------------------
#     ## DEFINE INCREASE SCORE
#     ##---------------------------------------------------------------
#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()
# ##---------------------------------------------------------------
# ## RESULTS
# ##---------------------------------------------------------------
# # WARNING: WORKS FINE BUT SHE DOESNT LIKE HARD CODED STUFF
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V3 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## SCOREBOARD CLASS
# ##---------------------------------------------------------------
# class Scoreboard(Turtle):
#     ##---------------------------------------------------------------
#     ## DEFINE SCORE
#     ##---------------------------------------------------------------
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color('white')
#         self.penup()
#         self.goto(0, 270)
#         self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
#         self.hideturtle()  
#     ##---------------------------------------------------------------
#     ## DEFINE INCREASE SCORE
#     ##---------------------------------------------------------------
#     def increase_score(self):
#         self.score += 1
#         self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
# ##---------------------------------------------------------------
# ## RESULTS
# ##---------------------------------------------------------------
# # ERROR: WORKS BUT OVERLAPS WITHOUT REMOVAL
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V2 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from turtle import Turtle
# ##---------------------------------------------------------------
# ## SCOREBOARD CLASS
# ##---------------------------------------------------------------
# class Scoreboard(Turtle):
#     ##---------------------------------------------------------------
#     ## DEFINE SELF
#     ##---------------------------------------------------------------
#     def __init__(self):
#         super().__init__()
#         ##---------------------------------------------------------------
#         ## DEFINE SCORE
#         ##---------------------------------------------------------------
#         self.score = 0
#         ##---------------------------------------------------------------
#         ## SCORE DISPLAY
#         ##---------------------------------------------------------------
#         self.color('white')
#         self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
#         self.hideturtle()  
#         self.goto(0, 270)
# ##---------------------------------------------------------------
# ## RESULTS
# ##---------------------------------------------------------------
# # ERROR: DRAWS LINE
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
# ## SCOREBOARD CLASS
# ##---------------------------------------------------------------
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
#         self.color('white')
# ##---------------------------------------------------------------
# ## RESULTS
# ##---------------------------------------------------------------
# # ERROR: NOT VISIBLE
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################