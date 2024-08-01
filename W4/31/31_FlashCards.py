################################################################>
#=========================================================>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 31_FlashCards = {
#=========================================================<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## IMPORTS
#-------------------------------------<
from tkinter import *
import pandas
import random
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## CONSTANTS
#-------------------------------------<
BACKGROUND_COLOR = "#B1DDC6"
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## GLOBAL DICTIONARIES
#-------------------------------------<
current_card = {}
to_learn = {}
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## TRY TO LOAD CSV
#-------------------------------------<
try:
    #-------------------------------------<
    # PANDAS RETRIEVE CSV
    #---------------------------<
    data = pandas.read_csv('./W4/31/Resources/data/words_left_to_learn.csv')
#:::::::::::::::::::::::::::::::::::::<
# EXCEPT IF CSV FILE WAS NOT FOUND, LOAD STARTER DATA
#---------------------------<
except FileNotFoundError:
    original_data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
#:::::::::::::::::::::::::::::::::::::<
# ELSE IF NO ERRORS OCCUR
#---------------------------<
else:
    #-------------------------------------<
    # ASSIGN CSV DATA TO PYTHON DICTIONARY
    #---------------------------<
    to_learn = data.to_dict(orient='records')
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## FUNCTIONS
#:::::::::::::::::::::::::::::::::::::<
## FUNCTION: NEXT CARD
#---------------------------<
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    #:::::::::::::::::::::::::::::::::::::<
    # WINDOW: FLIP CARD SETTINGS
    #---------------------------<
    flip_timer = window.after(5000, func=flip_card)
#:::::::::::::::::::::::::::::::::::::<
## FUNCTION: FLIP CARD
#---------------------------<
def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)
#:::::::::::::::::::::::::::::::::::::<
## FUNCTION: REMOVE CARD
#---------------------------<
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv('W4/31/Resources/data/words_left_to_learn.csv', index=False)
    next_card()
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# WINDOW
#:::::::::::::::::::::::::::::::::::::<
# WINDOW: DISPLAY SETTINGS 
#---------------------------<
window = Tk()
window.title('Flash Carder')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#:::::::::::::::::::::::::::::::::::::<
# WINDOW: FLIP CARD VARIABLE
#---------------------------<
flip_timer = window.after(5000, func=flip_card)
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## CANVAS
#:::::::::::::::::::::::::::::::::::::<
# CANVAS SIZE
#---------------------------<
canvas = Canvas(width=800, height=526)
#-------------------------------------<
# CANVAS: ASSIGN IMAGES TO CANVAS
#---------------<
card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
#-------------------------------------<
# CANVAS: ASSIGN DISPLAY TEXT
#---------------<
card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
#-------------------------------------<
# CANVAS: ASSIGN BACKGROUND SETTINGS
#---------------<
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## BUTTONS
#:::::::::::::::::::::::::::::::::::::<
# BUTTONS: ANSWER UNKNOWN BUTTON
#---------------------------<
unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
#---------------------------<
# UKNOWN: ALIGN IN CANVAS
#---------------<
unknown_btn.grid(row=1, column=0)
#:::::::::::::::::::::::::::::::::::::<
# BUTTONS: ANSWER KNOWN BUTTON
#---------------------------<
# KNOWN: ASSIGN IMG
#---------------<
known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
known_btn = Button(image=known_img, highlightthickness=0, command=is_known)
#---------------------------<
# KNOWN: ALIGN IN CANVAS
#---------------<
known_btn.grid(row=1, column=1)
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# CALL NEXT_CARD FUNCTION
#-------------------------------------<
next_card()
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# ALLOW WINDOW LAUNCH
#-------------------------------------<
window.mainloop()
#:::::::::::::::::::::::::::::::::::::\
#=========================================================<
# }
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# PROJECT: FLASH CARD PROGRAM - LEARNING THE FRENCH LANGUAGE 100 WORDS AT A TIME
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V18 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## GLOBAL DICTIONARIES
# #-------------------------------------<
# current_card = {}
# to_learn = {}
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## TRY TO LOAD CSV
# #-------------------------------------<
# try:
#     #-------------------------------------<
#     # PANDAS RETRIEVE CSV
#     #---------------------------<
#     data = pandas.read_csv('./W4/31/Resources/data/words_left_to_learn.csv')
# #:::::::::::::::::::::::::::::::::::::<
# # EXCEPT IF CSV FILE WAS NOT FOUND, LOAD STARTER DATA
# #---------------------------<
# except FileNotFoundError:
#     original_data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
#     to_learn = original_data.to_dict(orient='records')
# #:::::::::::::::::::::::::::::::::::::<
# # ELSE IF NO ERRORS OCCUR
# #---------------------------<
# else:
#     #-------------------------------------<
#     # ASSIGN CSV DATA TO PYTHON DICTIONARY
#     #---------------------------<
#     to_learn = data.to_dict(orient='records')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
#     #:::::::::::::::::::::::::::::::::::::<
#     # WINDOW: FLIP CARD SETTINGS
#     #---------------------------<
#     flip_timer = window.after(5000, func=flip_card)
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: REMOVE CARD
# #---------------------------<
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     data = pandas.DataFrame(to_learn)
#     data.to_csv('W4/31/Resources/data/words_left_to_learn.csv', index=False)
#     next_card()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD VARIABLE
# #---------------------------<
# flip_timer = window.after(5000, func=flip_card)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=is_known)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: FULL FUNCTIONALITY
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V17 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## GLOBAL DICTIONARIES
# #-------------------------------------<
# current_card = {}
# to_learn = {}
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## TRY TO LOAD CSV
# #-------------------------------------<
# try:
#     #-------------------------------------<
#     # PANDAS RETRIEVE CSV
#     #---------------------------<
#     data = pandas.read_csv('./W4/31/Resources/data/words_left_to_learn.csv')
# #:::::::::::::::::::::::::::::::::::::<
# # EXCEPT IF CSV FILE WAS NOT FOUND, LOAD STARTER DATA
# #---------------------------<
# except FileNotFoundError:
#     original_data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
#     to_learn = original_data.to_dict(orient='records')
# #:::::::::::::::::::::::::::::::::::::<
# # ELSE IF NO ERRORS OCCUR
# #---------------------------<
# else:
#     #-------------------------------------<
#     # ASSIGN CSV DATA TO PYTHON DICTIONARY
#     #---------------------------<
#     to_learn = data.to_dict(orient='records')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
#     #:::::::::::::::::::::::::::::::::::::<
#     # WINDOW: FLIP CARD SETTINGS
#     #---------------------------<
#     flip_timer = window.after(5000, func=flip_card)
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: REMOVE CARD
# #---------------------------<
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     data = pandas.DataFrame(to_learn)
#     data.to_csv('W4/31/Resources/data/words_left_to_learn.csv')
#     next_card()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD VARIABLE
# #---------------------------<
# flip_timer = window.after(5000, func=flip_card)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=is_known)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: FULL FUNCTIONARLITY, HOWEVER RECORD NUMBER IS INPUT TO OUTPUT CSV MORE THAN ONCE
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V16 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/words_left_to_learn.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## DICTIONARIES
# #-------------------------------------<
# current_card = {}

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
#     #:::::::::::::::::::::::::::::::::::::<
#     # WINDOW: FLIP CARD SETTINGS
#     #---------------------------<
#     flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: REMOVE CARD
# #---------------------------<
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     data = pandas.DataFrame(to_learn)
#     data.to_csv('W4/31/Resources/data/words_left_to_learn.csv')
#     next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD VARIABLE
# #---------------------------<
# flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=is_known)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: IF WORDS_LEFT_TO_LEARN.CSV IS NOT PRESENT, PROGRAM WILL CRASH

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V15 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## DICTIONARIES
# #-------------------------------------<
# current_card = {}

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
#     #:::::::::::::::::::::::::::::::::::::<
#     # WINDOW: FLIP CARD SETTINGS
#     #---------------------------<
#     flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: REMOVE CARD
# #---------------------------<
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     data = pandas.DataFrame(to_learn)
#     data.to_csv('W4/31/Resources/data/words_left_to_learn.csv')
#     next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD VARIABLE
# #---------------------------<
# flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=is_known)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: CURRENTLY KNOWN WORDS WILL STILL BE LOADED ON PROGRAM RELOAD, INSTEAD OF THE UNKNONWN_CSV

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V14 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## DICTIONARIES
# #-------------------------------------<
# current_card = {}

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
#     #:::::::::::::::::::::::::::::::::::::<
#     # WINDOW: FLIP CARD SETTINGS
#     #---------------------------<
#     flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: REMOVE CARD
# #---------------------------<
# def is_known():
#     to_learn.remove(current_card)
#     print(len(to_learn))
#     next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD VARIABLE
# #---------------------------<
# flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=is_known)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: FULLY FUNCTIONAL, HOWEVER CARDS WILL BE UNAVAILABLE AFTER IS_KNOWN = YES UNTIL PROGRAM RESTART

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V13 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## DICTIONARIES
# #-------------------------------------<
# current_card = {}

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card, flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
#     #:::::::::::::::::::::::::::::::::::::<
#     # WINDOW: FLIP CARD SETTINGS
#     #---------------------------<
#     flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD VARIABLE
# #---------------------------<
# flip_timer = window.after(5000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: CARD FLIPS AS INTENDED

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V12 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## DICTIONARIES
# #-------------------------------------<
# current_card = {}

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
#     #:::::::::::::::::::::::::::::::::::::<
#     # WINDOW: FLIP CARD SETTINGS
#     #---------------------------<
#     window.after(3000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: TIMER WORKS CORRECTLY, HOWEVER TIMER DOES NOT ACCOUNT FOR MULTIPLE CLICKS IN QUICK SUCCESSION

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V11 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## DICTIONARIES
# #-------------------------------------<
# current_card = {}

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French', fill='black')
#     canvas.itemconfig(card_word, text=current_card['French'], fill='black')
#     canvas.itemconfig(card_background, image=card_front_img)
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD SETTINGS
# #---------------------------<
# window.after(3000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: CARD FORMAT MAINTAINED, CARD DOES NOT FLIP BETWEEN BACK AND FRONT AFTER FIRST CARD

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V10 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## DICTIONARIES
# #-------------------------------------<
# current_card = {}

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     global current_card
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French')
#     canvas.itemconfig(card_word, text=current_card['French'])
# #:::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: FLIP CARD
# #---------------------------<
# def flip_card():
#     canvas.itemconfig(card_title, text='English', fill='white')
#     canvas.itemconfig(card_word, text=current_card['English'], fill='white')
#     canvas.itemconfig(card_background, image=card_back_img)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: DISPLAY SETTINGS 
# #---------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# #:::::::::::::::::::::::::::::::::::::<
# # WINDOW: FLIP CARD SETTINGS
# #---------------------------<
# window.after(3000, func=flip_card)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGES TO CANVAS
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# card_back_img = PhotoImage(file='./W4/31/Resources/images/card_back.png')
# card_background = canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: CARD FLIPPING PARTIALLY FUNCTIONAL, THE CARD RETAINS WRONG FORMAT ON FLIP

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V9 = {
# #=========================================================<
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French')
#     canvas.itemconfig(card_word, text=current_card['French'])

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # CALL NEXT_CARD FUNCTION
# #-------------------------------------<
# next_card()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: WINDOW SHOWS AFTER REMOVAL OF SPECIFIED X= AND Y= VALUES

# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V8 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French')
#     canvas.itemconfig(card_word, text=current_card['French'])

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(400, 263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(400, 263, text='word', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: WINDOW SHOWS AFTER REMOVAL OF SPECIFIED X= AND Y= VALUES
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V7 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(card_title, text='French')
#     canvas.itemconfig(card_word, text=current_card['French'])

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(x=400, y=263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# card_title = canvas.create_text(x=400, y=150, text='Title', font=('Arial', 40, 'italic'))
# card_word = canvas.create_text(x=400, y=263, text='word', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # ERROR: WINDOW FAILS TO LOAD, INDEXERROR REGARDING CREATE_IMAGE
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V6 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas
# import random

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# #-------------------------------------<
# # ASSIGN CSV DATA TO PYTHON DICTIONARY
# #---------------------------<
# to_learn = data.to_dict(orient='records')

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     current_card = random.choice(to_learn)
#     print(current_card['French'])

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(x=400, y=263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# canvas.create_text(x=400, y=150, text='Title', font=('Arial', 40, 'italic'))
# canvas.create_text(x=400, y=263, text='word', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: CODE IS PRINTED CORRECTLY FORMATTED, HOWEVER WINDOW IS NON-FUNCTIONAL
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V5 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS ASSIGNMENT
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# to_learn = data.to_dict()
# print(to_learn)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     pass

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(x=400, y=263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# canvas.create_text(x=400, y=150, text='Title', font=('Arial', 40, 'italic'))
# canvas.create_text(x=400, y=263, text='word', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: PRINTED RESULTS CORRECT, BUT ORDER IS DIFFICULT TO READ
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V4 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *
# import pandas

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PANDAS ASSIGNMENT
# #-------------------------------------<
# data = pandas.read_csv('./W4/31/Resources/data/french_words.csv')
# print(data)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## FUNCTION: NEXT CARD
# #---------------------------<
# def next_card():
#     pass

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(x=400, y=263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# canvas.create_text(x=400, y=150, text='Title', font=('Arial', 40, 'italic'))
# canvas.create_text(x=400, y=263, text='word', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0, command=next_card)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # ERROR: TUPLE INDEX OUT OF RANGE IN REGARDS TO CREATE_IMAGE
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V3 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(x=400, y=263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# canvas.create_text(x=400, y=150, text='Title', font=('Arial', 40, 'italic'))
# canvas.create_text(x=400, y=263, text='word', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img, highlightthickness=0)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img, highlightthickness=0)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V2 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS
# #:::::::::::::::::::::::::::::::::::::<
# # CANVAS SIZE
# #---------------------------<
# canvas = Canvas(width=800, height=526)
# #-------------------------------------<
# # CANVAS: ASSIGN IMAGE (FRONT)
# #---------------<
# card_front_img = PhotoImage(file='./W4/31/Resources/images/card_front.png')
# canvas.create_image(x=400, y=263, image=card_front_img)
# #-------------------------------------<
# # CANVAS: ASSIGN DISPLAY TEXT
# #---------------<
# canvas.create_text(x=400, y=150, text='Title', font=('Arial', 40, 'italic'))
# canvas.create_text(x=400, y=263, text='word', font=('Arial', 60, 'bold'))
# #-------------------------------------<
# # CANVAS: ASSIGN BACKGROUND SETTINGS
# #---------------<
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## BUTTONS
# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER UNKNOWN BUTTON
# #---------------------------<
# unknown_img = PhotoImage(file='./W4/31/Resources/images/wrong.png')
# unknown_btn = Button(image=unknown_img)
# #---------------------------<
# # UKNOWN: ALIGN IN CANVAS
# #---------------<
# unknown_btn.grid(row=1, column=0)

# #:::::::::::::::::::::::::::::::::::::<
# # BUTTONS: ANSWER KNOWN BUTTON
# #---------------------------<
# # KNOWN: ASSIGN IMG
# #---------------<
# known_img = PhotoImage(file='./W4/31/Resources/images/right.png')
# known_btn = Button(image=known_img)
# #---------------------------<
# # KNOWN: ALIGN IN CANVAS
# #---------------<
# known_btn.grid(row=1, column=1)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # ALLOW WINDOW LAUNCH
# #-------------------------------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V1 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------------<
# from tkinter import *

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # WINDOW
# #-------------------------------------<
# window = Tk()
# window.title('Flash Carder')
# window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #-------------------------------------<
# # ERROR: WINDOW DOES NOT LAUNCH
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CONSTANTS
# #-------------------------------------<
# BACKGROUND_COLOR = "#B1DDC6"
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
#################################################################