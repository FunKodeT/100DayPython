################################################################>
#===============================================================>
# FINAL PROGRAM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#:::::::::::::::::::::::::::::::::::::::::::::::<
## IMPORTS
#-------------------------------<
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
#:::::::::::::::::::::::::::::::::::::::::::::::<
## PASSWORD GENERATOR FUNCTION
#-------------------------------<
def gen_password():
    #:::::::::::::::::::::::::::::::::::::::::::::::<
    ## LISTS OF CHARACTERS
    #-------------------------------<
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
    #:::::::::::::::::::::::::::::::::::::::::::::::<
    ## LIST COMPREHENSION
    #-------------------------------<
    # COMPREHENSION: LETTERS
    #---------------<
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    #-------------------------------<
    # COMPREHENSION: NUMBERS
    #---------------<
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    #-------------------------------<
    # COMPREHENSION: SYMBOLS
    #---------------<
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    #:::::::::::::::::::::::::::::::::::::::::::::::<
    # LIST ASSIGNMENT FROM COMPREHENSION
    #---------------<
    password_list = password_letters + password_numbers + password_symbols
    #:::::::::::::::::::::::::::::::::::::::::::::::<
    # RANDOM SHUFFLE OF LIST ASSIGNMENT
    #---------------<
    shuffle(password_list)
    #-------------------------------<
    # ASSIGNMENT TO STRING VARIABLE
    #---------------<
    password = ''.join(password_list)
    #-------------------------------<
    # STRING TO ENTRY INSERTION
    #---------------<
    password_entry.insert(0, password)
    pyperclip.copy(password)
#:::::::::::::::::::::::::::::::::::::::::::::::<
## SAVE PASSWORD
#-------------------------------<
def save():
    #-------------------------------<
    ## GET USER INPUTS
    #---------------<
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #-------------------------------<
    ## ESTABLISH JSON FORMAT
    #---------------<
    new_data = {
        website: {
        'email': email,
        'password': password,
    }}
    #:::::::::::::::::::::::::::::::::::::::::::::::<
    ## IF INVALID OR MISSING INPUTS
    #-------------------------------<
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title='Oops', message='All fields required, please try again.')
    #:::::::::::::::::::::::::::::::::::::::::::::::<
    ## ELSE IF INPUTS VALID, SAVE TO FILE
    #-------------------------------<
    else:
        #:::::::::::::::::::::::::::::::::::::::::::::::<
        ## TRY TO OPEN AND READ JSON FILE
        #-------------------------------<
        try:
            with open('data.json', 'r') as data_file:
                #-------------------------------<
                ## READ DATA FROM JSON FILE
                #---------------<
                data = json.load(data_file)
        #-------------------------------<
        ## EXCEPT IF JSON FILE WAS NOT FOUND
        #---------------<
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        #-------------------------------<
        ## ELSE IF NO ERRORS
        #---------------<
        else:
            #-------------------------------<
            ## UPDATE DATA FROM JSON FILE
            #---------------<
            data.update(new_data)
            #:::::::::::::::::::::::::::::::::::::::::::::::<
            ## OPEN AND WRITE TO JSON FILE
            #-------------------------------<
            with open('data.json', 'w') as data_file:
                #-------------------------------<
                ## ADD DATA TO JSON FILE
                #---------------<
                json.dump(new_data, data_file, indent=4)
            #-------------------------------<
            ## REMOVE SAVED ENTRIES FROM GUI
            #---------------<
        finally:
            #-------------------------------<
            ## ALWAYS DELETE ENTRIES FROM GUI WHETHER ERROR OCCURS OR NOT
            #---------------<
            website_entry.delete(0, END)
            password_entry.delete(0, END)
#:::::::::::::::::::::::::::::::::::::::::::::::<
## SEARCH EXISTING DATA FUNCTION
#-------------------------------<
def find_data():
    #-------------------------------<
    ## RETRIEVE USER INPUT IN WEBSITE ENTRY
    #---------------<
    website = website_entry.get()
    #:::::::::::::::::::::::::::::::::::::::::::::::<
    ## TRY TO OPEN SPECIFIED JSON FILE
    #-------------------------------<
    try:
        with open(data.json) as data_file:
            data = json.load(data_file)
    #-------------------------------<
    ## EXCEPT IF JSON FILE DOES NOT EXIST
    #---------------<
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No data found.')
    #-------------------------------<
    ## ELSE IF NO ERROR OCCURS
    #---------------<
    else:
        #-------------------------------<
        ## IF USER INPUT MATCHES EXISTING DATA
        #---------------<
        if website in data:
            #-------------------------------<
            ## RETRIEVE DATA
            #---------------<
            email = data[website]['email']
            password = data[website]['password']
            #-------------------------------<
            ## DISPLAY DATA FOR USER
            #---------------<
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        #-------------------------------<
        ## ELSE IF USER INPUT DOES NOT MATCH EXISTING DATA
        #---------------<
        else:
            #-------------------------------<
            ## DISPLAY MESSAGEBOX INFORMING USER OF MISSING DATA
            #---------------<
            messagebox.showinfo(title='Error', message=f'No details for {website} are available.')
#:::::::::::::::::::::::::::::::::::::::::::::::<
## UI SETUP
#-------------------------------<
# TKINTER WINDOW SETTINGS
#---------------<
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
#-------------------------------<
# TKINTER CANVAS SETTINGS
#---------------<
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='W3/30/Resources/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
#:::::::::::::::::::::::::::::::::::::::::::::::<
## CANVAS LABELS
#-------------------------------<
# LABELS: WEBSITE
#---------------<
website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)
#-------------------------------<
# LABELS: EMAIL || USERNAME
#---------------<
email_label = Label(text='Email/Username: ')
email_label.grid(row=2, column=0)
#-------------------------------<
# LABELS: PASSWORD
#---------------<
password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)
#:::::::::::::::::::::::::::::::::::::::::::::::<
## CANVAS ENTRIES
#-------------------------------<
# ENTRIES: WEBSITE
#---------------<
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
#-------------------------------<
## ENTRIES: EMAIL || USERNAME
#---------------<
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, 'cooteybug@gmail.com')
#-------------------------------<
## ENTRIES: PASSWORD
#---------------<
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
#:::::::::::::::::::::::::::::::::::::::::::::::<
## CANVAS BUTTONS
#-------------------------------<
## BUTTONS: SEARCH FOR EXISTING DATA
#---------------<
search_button = Button(text='Search', width=13, command=find_data)
search_button.grid(row=1, column=2)
#-------------------------------<
## BUTTONS: GENERATE RANDOM PASSWORD
#---------------<
generate_password_button = Button(text='Generate Password', command=gen_password)
generate_password_button.grid(row=3, column=3)
#-------------------------------<
## BUTTONS: SAVE INFORMATION TO FILE
#---------------<
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
#:::::::::::::::::::::::::::::::::::::::::::::::<
## WINDOW INITIALIZATION
#---------------<
window.mainloop()
#:::::::::::::::::::::::::::::::::::::::::::::::<
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#===============================================================>
################################################################>
#===============================================================>
# PROJECT: PASSWORD MANAGER ERROR HANDLING
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM5_V6 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------<
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PASSWORD GENERATOR FUNCTION
# #-------------------------------<
# def gen_password():
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LISTS OF CHARACTERS
#     #-------------------------------<
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LIST COMPREHENSION
#     #-------------------------------<
#     # COMPREHENSION: LETTERS
#     #---------------<
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     #-------------------------------<
#     # COMPREHENSION: NUMBERS
#     #---------------<
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     #-------------------------------<
#     # COMPREHENSION: SYMBOLS
#     #---------------<
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # LIST ASSIGNMENT FROM COMPREHENSION
#     #---------------<
#     password_list = password_letters + password_numbers + password_symbols
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # RANDOM SHUFFLE OF LIST ASSIGNMENT
#     #---------------<
#     shuffle(password_list)
#     #-------------------------------<
#     # ASSIGNMENT TO STRING VARIABLE
#     #---------------<
#     password = ''.join(password_list)
#     #-------------------------------<
#     # STRING TO ENTRY INSERTION
#     #---------------<
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SAVE PASSWORD
# #-------------------------------<
# def save():
#     #-------------------------------<
#     ## GET USER INPUTS
#     #---------------<
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     #-------------------------------<
#     ## ESTABLISH JSON FORMAT
#     #---------------<
#     new_data = {
#         website: {
#         'email': email,
#         'password': password,
#     }}
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## IF INVALID OR MISSING INPUTS
#     #-------------------------------<
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## ELSE IF INPUTS VALID, SAVE TO FILE
#     #-------------------------------<
#     else:
#         #:::::::::::::::::::::::::::::::::::::::::::::::<
#         ## TRY TO OPEN AND READ JSON FILE
#         #-------------------------------<
#         try:
#             with open('data.json', 'r') as data_file:
#                 #-------------------------------<
#                 ## READ DATA FROM JSON FILE
#                 #---------------<
#                 data = json.load(data_file)
#         #-------------------------------<
#         ## EXCEPT IF JSON FILE WAS NOT FOUND
#         #---------------<
#         except FileNotFoundError:
#             with open('data.json', 'w') as data_file:
#                 json.dump(new_data, data_file, indent=4)
#         #-------------------------------<
#         ## ELSE IF NO ERRORS
#         #---------------<
#         else:
#             #-------------------------------<
#             ## UPDATE DATA FROM JSON FILE
#             #---------------<
#             data.update(new_data)
#             #:::::::::::::::::::::::::::::::::::::::::::::::<
#             ## OPEN AND WRITE TO JSON FILE
#             #-------------------------------<
#             with open('data.json', 'w') as data_file:
#                 #-------------------------------<
#                 ## ADD DATA TO JSON FILE
#                 #---------------<
#                 json.dump(new_data, data_file, indent=4)
#             #-------------------------------<
#             ## REMOVE SAVED ENTRIES FROM GUI
#             #---------------<
#         finally:
#             #-------------------------------<
#             ## ALWAYS DELETE ENTRIES FROM GUI WHETHER ERROR OCCURS OR NOT
#             #---------------<
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SEARCH EXISTING DATA FUNCTION
# #-------------------------------<
# def find_data():
#     #-------------------------------<
#     ## RETRIEVE USER INPUT IN WEBSITE ENTRY
#     #---------------<
#     website = website_entry.get()
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## TRY TO OPEN SPECIFIED JSON FILE
#     #-------------------------------<
#     try:
#         with open(data.json) as data_file:
#             data = json.load(data_file)
#     #-------------------------------<
#     ## EXCEPT IF JSON FILE DOES NOT EXIST
#     #---------------<
#     except FileNotFoundError:
#         messagebox.showinfo(title='Error', message='No data found.')
#     #-------------------------------<
#     ## ELSE IF NO ERROR OCCURS
#     #---------------<
#     else:
#         #-------------------------------<
#         ## IF USER INPUT MATCHES EXISTING DATA
#         #---------------<
#         if website in data:
#             #-------------------------------<
#             ## RETRIEVE DATA
#             #---------------<
#             email = data[website]['email']
#             password = data[website]['password']
#             #-------------------------------<
#             ## DISPLAY DATA FOR USER
#             #---------------<
#             messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
#         #-------------------------------<
#         ## ELSE IF USER INPUT DOES NOT MATCH EXISTING DATA
#         #---------------<
#         else:
#             #-------------------------------<
#             ## DISPLAY MESSAGEBOX INFORMING USER OF MISSING DATA
#             #---------------<
#             messagebox.showinfo(title='Error', message=f'No details for {website} are available.')
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## UI SETUP
# #-------------------------------<
# # TKINTER WINDOW SETTINGS
# #---------------<
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# #-------------------------------<
# # TKINTER CANVAS SETTINGS
# #---------------<
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/30/Resources/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS LABELS
# #-------------------------------<
# # LABELS: WEBSITE
# #---------------<
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# #-------------------------------<
# # LABELS: EMAIL || USERNAME
# #---------------<
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# #-------------------------------<
# # LABELS: PASSWORD
# #---------------<
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS ENTRIES
# #-------------------------------<
# # ENTRIES: WEBSITE
# #---------------<
# website_entry = Entry(width=21)
# website_entry.grid(row=1, column=1)
# website_entry.focus()
# #-------------------------------<
# ## ENTRIES: EMAIL || USERNAME
# #---------------<
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# #-------------------------------<
# ## ENTRIES: PASSWORD
# #---------------<
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS BUTTONS
# #-------------------------------<
# ## BUTTONS: SEARCH FOR EXISTING DATA
# #---------------<
# search_button = Button(text='Search', width=13, command=find_data)
# search_button.grid(row=1, column=2)
# #-------------------------------<
# ## BUTTONS: GENERATE RANDOM PASSWORD
# #---------------<
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# #-------------------------------<
# ## BUTTONS: SAVE INFORMATION TO FILE
# #---------------<
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## WINDOW INITIALIZATION
# #---------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #---------------<
# # SUCCESS: DATA LOADED FROM JSON FILE WILL BE CONVERTED TO PYTHON DICTIONARY FORMAT
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM5_V5 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------<
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PASSWORD GENERATOR FUNCTION
# #-------------------------------<
# def gen_password():
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LISTS OF CHARACTERS
#     #-------------------------------<
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LIST COMPREHENSION
#     #-------------------------------<
#     # COMPREHENSION: LETTERS
#     #---------------<
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     #-------------------------------<
#     # COMPREHENSION: NUMBERS
#     #---------------<
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     #-------------------------------<
#     # COMPREHENSION: SYMBOLS
#     #---------------<
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # LIST ASSIGNMENT FROM COMPREHENSION
#     #---------------<
#     password_list = password_letters + password_numbers + password_symbols
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # RANDOM SHUFFLE OF LIST ASSIGNMENT
#     #---------------<
#     shuffle(password_list)
#     #-------------------------------<
#     # ASSIGNMENT TO STRING VARIABLE
#     #---------------<
#     password = ''.join(password_list)
#     #-------------------------------<
#     # STRING TO ENTRY INSERTION
#     #---------------<
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SAVE PASSWORD
# #-------------------------------<
# def save():
#     #-------------------------------<
#     ## GET USER INPUTS
#     #---------------<
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     #-------------------------------<
#     ## ESTABLISH JSON FORMAT
#     #---------------<
#     new_data = {
#         website: {
#         'email': email,
#         'password': password,
#     }}
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## IF INVALID OR MISSING INPUTS
#     #-------------------------------<
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## ELSE IF INPUTS VALID, SAVE TO FILE
#     #-------------------------------<
#     else:
#         #:::::::::::::::::::::::::::::::::::::::::::::::<
#         ## TRY TO OPEN AND READ JSON FILE
#         #-------------------------------<
#         try:
#             with open('data.json', 'r') as data_file:
#                 #-------------------------------<
#                 ## READ DATA FROM JSON FILE
#                 #---------------<
#                 data = json.load(data_file)
#         #-------------------------------<
#         ## EXCEPT IF JSON FILE WAS NOT FOUND
#         #---------------<
#         except FileNotFoundError:
#             with open('data.json', 'w') as data_file:
#                 json.dump(new_data, data_file, indent=4)
#         #-------------------------------<
#         ## ELSE IF NO ERRORS
#         #---------------<
#         else:
#             #-------------------------------<
#             ## UPDATE DATA FROM JSON FILE
#             #---------------<
#             data.update(new_data)
#             #:::::::::::::::::::::::::::::::::::::::::::::::<
#             ## OPEN AND WRITE TO JSON FILE
#             #-------------------------------<
#             with open('data.json', 'w') as data_file:
#                 #-------------------------------<
#                 ## ADD DATA TO JSON FILE
#                 #---------------<
#                 json.dump(new_data, data_file, indent=4)
#             #-------------------------------<
#             ## REMOVE SAVED ENTRIES FROM GUI
#             #---------------<
#         finally:
#             #-------------------------------<
#             ## ALWAYS DELETE ENTRIES FROM GUI WHETHER ERROR OCCURS OR NOT
#             #---------------<
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SEARCH EXISTING DATA FUNCTION
# #-------------------------------<
# def find_data():
#     #-------------------------------<
#     ## RETRIEVE USER INPUT IN WEBSITE ENTRY
#     #---------------<
#     website = website_entry.get()
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## OPEN JSON FILE
#     #-------------------------------<
#     with open(data.json) as data_file:
#         data = json.load(data_file)
#         #-------------------------------<
#         ## IF USER INPUT MATCHES EXISTING DATA
#         #---------------<
#         if website in data:
#             #-------------------------------<
#             ## RETRIEVE DATA AND DISPLAY IN MESSAGEBOX FOR USER
#             #---------------<
#             email = data[website]['email']
#             password = data[website]['password']
#             messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## UI SETUP
# #-------------------------------<
# # TKINTER WINDOW SETTINGS
# #---------------<
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# #-------------------------------<
# # TKINTER CANVAS SETTINGS
# #---------------<
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/30/Resources/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS LABELS
# #-------------------------------<
# # LABELS: WEBSITE
# #---------------<
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# #-------------------------------<
# # LABELS: EMAIL || USERNAME
# #---------------<
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# #-------------------------------<
# # LABELS: PASSWORD
# #---------------<
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS ENTRIES
# #-------------------------------<
# # ENTRIES: WEBSITE
# #---------------<
# website_entry = Entry(width=21)
# website_entry.grid(row=1, column=1)
# website_entry.focus()
# #-------------------------------<
# ## ENTRIES: EMAIL || USERNAME
# #---------------<
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# #-------------------------------<
# ## ENTRIES: PASSWORD
# #---------------<
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS BUTTONS
# #-------------------------------<
# ## BUTTONS: SEARCH FOR EXISTING DATA
# #---------------<
# search_button = Button(text='Search', width=13, command=find_data)
# search_button.grid(row=1, column=2)
# #-------------------------------<
# ## BUTTONS: GENERATE RANDOM PASSWORD
# #---------------<
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# #-------------------------------<
# ## BUTTONS: SAVE INFORMATION TO FILE
# #---------------<
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## WINDOW INITIALIZATION
# #---------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #---------------<
# # SUCCESS: DATA LOADED FROM JSON FILE WILL BE CONVERTED TO PYTHON DICTIONARY FORMAT
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM5_V4 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------<
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PASSWORD GENERATOR
# #-------------------------------<
# # CHARACTER LISTS
# #---------------<
# def gen_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LIST COMPREHENSION
#     #-------------------------------<
#     # COMPREHENSION: LETTERS
#     #---------------<
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     #-------------------------------<
#     # COMPREHENSION: NUMBERS
#     #---------------<
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     #-------------------------------<
#     # COMPREHENSION: SYMBOLS
#     #---------------<
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # LIST ASSIGNMENT FROM COMPREHENSION
#     #---------------<
#     password_list = password_letters + password_numbers + password_symbols
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # RANDOM SHUFFLE OF LIST ASSIGNMENT
#     #---------------<
#     shuffle(password_list)
#     #-------------------------------<
#     # ASSIGNMENT TO STRING VARIABLE
#     #---------------<
#     password = ''.join(password_list)
#     #-------------------------------<
#     # STRING TO ENTRY INSERTION
#     #---------------<
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SAVE PASSWORD
# #-------------------------------<
# def save():
#     #-------------------------------<
#     ## GET USER INPUTS
#     #---------------<
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     #-------------------------------<
#     ## ESTABLISH JSON FORMAT
#     #---------------<
#     new_data = {
#         website: {
#         'email': email,
#         'password': password,
#     }}
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## IF INVALID OR MISSING INPUTS
#     #-------------------------------<
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## ELSE IF INPUTS VALID, SAVE TO FILE
#     #-------------------------------<
#     else:
#         #:::::::::::::::::::::::::::::::::::::::::::::::<
#         ## TRY TO OPEN AND READ JSON FILE
#         #-------------------------------<
#         try:
#             with open('data.json', 'r') as data_file:
#                 #-------------------------------<
#                 ## READ DATA FROM JSON FILE
#                 #---------------<
#                 data = json.load(data_file)
#         #-------------------------------<
#         ## EXCEPT IF JSON FILE WAS NOT FOUND
#         #---------------<
#         except FileNotFoundError:
#             with open('data.json', 'w') as data_file:
#                 json.dump(new_data, data_file, indent=4)
#         #-------------------------------<
#         ## ELSE IF NO ERRORS
#         #---------------<
#         else:
#             #-------------------------------<
#             ## UPDATE DATA FROM JSON FILE
#             #---------------<
#             data.update(new_data)
#             #:::::::::::::::::::::::::::::::::::::::::::::::<
#             ## OPEN AND WRITE TO JSON FILE
#             #-------------------------------<
#             with open('data.json', 'w') as data_file:
#                 #-------------------------------<
#                 ## ADD DATA TO JSON FILE
#                 #---------------<
#                 json.dump(new_data, data_file, indent=4)
#             #-------------------------------<
#             ## REMOVE SAVED ENTRIES FROM GUI
#             #---------------<
#         finally:
#             #-------------------------------<
#             ## ALWAYS DELETE ENTRIES FROM GUI WHETHER ERROR OCCURS OR NOT
#             #---------------<
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## UI SETUP
# #-------------------------------<
# # TKINTER WINDOW SETTINGS
# #---------------<
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# #-------------------------------<
# # TKINTER CANVAS SETTINGS
# #---------------<
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/30/Resources/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS LABELS
# #-------------------------------<
# # LABELS: WEBSITE
# #---------------<
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# #-------------------------------<
# # LABELS: EMAIL || USERNAME
# #---------------<
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# #-------------------------------<
# # LABELS: PASSWORD
# #---------------<
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS ENTRIES
# #-------------------------------<
# # ENTRIES: WEBSITE
# #---------------<
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# #-------------------------------<
# ## ENTRIES: EMAIL || USERNAME
# #---------------<
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# #-------------------------------<
# ## ENTRIES: PASSWORD
# #---------------<
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS BUTTONS
# #-------------------------------<
# ## BUTTONS: GENERATE RANDOM PASSWORD
# #---------------<
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# #-------------------------------<
# ## BUTTONS: SAVE INFORMATION TO FILE
# #---------------<
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## WINDOW INITIALIZATION
# #---------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #---------------<
# # SUCCESS: DATA LOADED FROM JSON FILE WILL BE CONVERTED TO PYTHON DICTIONARY FORMAT
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM5_V3 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------<
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PASSWORD GENERATOR
# #-------------------------------<
# # CHARACTER LISTS
# #---------------<
# def gen_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LIST COMPREHENSION
#     #-------------------------------<
#     # COMPREHENSION: LETTERS
#     #---------------<
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     #-------------------------------<
#     # COMPREHENSION: NUMBERS
#     #---------------<
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     #-------------------------------<
#     # COMPREHENSION: SYMBOLS
#     #---------------<
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # LIST ASSIGNMENT FROM COMPREHENSION
#     #---------------<
#     password_list = password_letters + password_numbers + password_symbols
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # RANDOM SHUFFLE OF LIST ASSIGNMENT
#     #---------------<
#     shuffle(password_list)
#     #-------------------------------<
#     # ASSIGNMENT TO STRING VARIABLE
#     #---------------<
#     password = ''.join(password_list)
#     #-------------------------------<
#     # STRING TO ENTRY INSERTION
#     #---------------<
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SAVE PASSWORD
# #-------------------------------<
# def save():
#     #-------------------------------<
#     ## GET USER INPUTS
#     #---------------<
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     #-------------------------------<
#     ## ESTABLISH JSON FORMAT
#     #---------------<
#     new_data = {
#         website: {
#         'email': email,
#         'password': password,
#     }}
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## IF INVALID OR MISSING INPUTS
#     #-------------------------------<
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## ELSE IF INPUTS VALID, SAVE TO FILE
#     #-------------------------------<
#     else:
#         #:::::::::::::::::::::::::::::::::::::::::::::::<
#         ## OPEN AND READ JSON FILE
#         #-------------------------------<
#         with open('data.json', 'r') as data_file:
#             #-------------------------------<
#             ## READ DATA FROM JSON FILE
#             #---------------<
#             data = json.load(data_file)
#             print(type(data))
#             #-------------------------------<
#             ## UPDATE DATA FROM JSON FILE
#             #---------------<
#             data.update(new_data)
#         #:::::::::::::::::::::::::::::::::::::::::::::::<
#         ## OPEN AND WRITE TO JSON FILE
#         #-------------------------------<
#         with open('data.json', 'w') as data_file:
#             #-------------------------------<
#             ## ADD DATA TO JSON FILE
#             #---------------<
#             json.dump(new_data, data_file, indent=4)
#             #-------------------------------<
#             ## REMOVE SAVED ENTRIES FROM GUI
#             #---------------<
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## UI SETUP
# #-------------------------------<
# # TKINTER WINDOW SETTINGS
# #---------------<
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# #-------------------------------<
# # TKINTER CANVAS SETTINGS
# #---------------<
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/30/Resources/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS LABELS
# #-------------------------------<
# # LABELS: WEBSITE
# #---------------<
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# #-------------------------------<
# # LABELS: EMAIL || USERNAME
# #---------------<
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# #-------------------------------<
# # LABELS: PASSWORD
# #---------------<
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS ENTRIES
# #-------------------------------<
# # ENTRIES: WEBSITE
# #---------------<
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# #-------------------------------<
# ## ENTRIES: EMAIL || USERNAME
# #---------------<
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# #-------------------------------<
# ## ENTRIES: PASSWORD
# #---------------<
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS BUTTONS
# #-------------------------------<
# ## BUTTONS: GENERATE RANDOM PASSWORD
# #---------------<
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# #-------------------------------<
# ## BUTTONS: SAVE INFORMATION TO FILE
# #---------------<
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## WINDOW INITIALIZATION
# #---------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #---------------<
# # SUCCESS: DATA LOADED FROM JSON FILE WILL BE CONVERTED TO PYTHON DICTIONARY FORMAT
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM5_V2 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------<
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PASSWORD GENERATOR
# #-------------------------------<
# # CHARACTER LISTS
# #---------------<
# def gen_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LIST COMPREHENSION
#     #-------------------------------<
#     # COMPREHENSION: LETTERS
#     #---------------<
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     #-------------------------------<
#     # COMPREHENSION: NUMBERS
#     #---------------<
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     #-------------------------------<
#     # COMPREHENSION: SYMBOLS
#     #---------------<
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # LIST ASSIGNMENT FROM COMPREHENSION
#     #---------------<
#     password_list = password_letters + password_numbers + password_symbols
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # RANDOM SHUFFLE OF LIST ASSIGNMENT
#     #---------------<
#     shuffle(password_list)
#     #-------------------------------<
#     # ASSIGNMENT TO STRING VARIABLE
#     #---------------<
#     password = ''.join(password_list)
#     #-------------------------------<
#     # STRING TO ENTRY INSERTION
#     #---------------<
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SAVE PASSWORD
# #-------------------------------<
# def save():
#     #-------------------------------<
#     ## GET USER INPUTS
#     #---------------<
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     #-------------------------------<
#     ## ESTABLISH JSON FORMAT
#     #---------------<
#     new_data = {
#         website: {
#         'email': email,
#         'password': password,
#     }}
#     #-------------------------------<
#     ## IF INVALID OR MISSING INPUTS
#     #---------------<
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     #-------------------------------<
#     ## ELSE IF INPUTS VALID, SAVE TO FILE
#     #---------------<
#     else:
#         #-------------------------------<
#         ## OPEN JSON FILE WITH WRITE ATTRIBUTE
#         #---------------<
#         with open('data.json', 'w') as data_file:
#             #-------------------------------<
#             ## ADD DATA TO JSON FILE
#             #---------------<
#             json.dump(new_data, data_file, indent=4)
#             #-------------------------------<
#             ## READ DATA FROM JSON FILE
#             #---------------<
#             data = json.load(data_file)
#             print(type(data))
#             #-------------------------------<
#             ## REMOVE SAVED ENTRIES FROM GUI
#             #---------------<
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## UI SETUP
# #-------------------------------<
# # TKINTER WINDOW SETTINGS
# #---------------<
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# #-------------------------------<
# # TKINTER CANVAS SETTINGS
# #---------------<
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/30/Resources/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS LABELS
# #-------------------------------<
# # LABELS: WEBSITE
# #---------------<
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# #-------------------------------<
# # LABELS: EMAIL || USERNAME
# #---------------<
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# #-------------------------------<
# # LABELS: PASSWORD
# #---------------<
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS ENTRIES
# #-------------------------------<
# # ENTRIES: WEBSITE
# #---------------<
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# #-------------------------------<
# ## ENTRIES: EMAIL || USERNAME
# #---------------<
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# #-------------------------------<
# ## ENTRIES: PASSWORD
# #---------------<
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS BUTTONS
# #-------------------------------<
# ## BUTTONS: GENERATE RANDOM PASSWORD
# #---------------<
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# #-------------------------------<
# ## BUTTONS: SAVE INFORMATION TO FILE
# #---------------<
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## WINDOW INITIALIZATION
# #---------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CODE RESULTS
# #---------------<
# # SUCCESS: DATA LOADED FROM JSON FILE WILL BE CONVERTED TO PYTHON DICTIONARY FORMAT
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM5_V1 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------<
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PASSWORD GENERATOR
# #-------------------------------<
# # CHARACTER LISTS
# #---------------<
# def gen_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LIST COMPREHENSION
#     #-------------------------------<
#     # COMPREHENSION: LETTERS
#     #---------------<
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     #-------------------------------<
#     # COMPREHENSION: NUMBERS
#     #---------------<
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     #-------------------------------<
#     # COMPREHENSION: SYMBOLS
#     #---------------<
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # LIST ASSIGNMENT FROM COMPREHENSION
#     #---------------<
#     password_list = password_letters + password_numbers + password_symbols
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # RANDOM SHUFFLE OF LIST ASSIGNMENT
#     #---------------<
#     shuffle(password_list)
#     #-------------------------------<
#     # ASSIGNMENT TO STRING VARIABLE
#     #---------------<
#     password = ''.join(password_list)
#     #-------------------------------<
#     # STRING TO ENTRY INSERTION
#     #---------------<
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SAVE PASSWORD
# #-------------------------------<
# def save():
#     #-------------------------------<
#     ## GET USER INPUTS
#     #---------------<
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     #-------------------------------<
#     ## ESTABLISH JSON FORMAT
#     #---------------<
#     new_data = {
#         website: {
#         'email': email,
#         'password': password,
#     }}
#     #-------------------------------<
#     ## IF INVALID OR MISSING INPUTS
#     #---------------<
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     #-------------------------------<
#     ## ELSE IF INPUTS VALID, SAVE TO FILE
#     #---------------<
#     else:
#         #-------------------------------<
#         ## OPEN JSON FILE WITH WRITE ATTRIBUTE
#         #---------------<
#         with open('data.json', 'w') as data_file:
#             #-------------------------------<
#             ## ADD DATA TO JSON FILE
#             #---------------<
#             json.dump(new_data, data_file, indent=4)
#             #-------------------------------<
#             ## READ DATA FROM JSON FILE
#             #---------------<
#             data = json.read(data_file)
#             print(data)
#             #-------------------------------<
#             ## REMOVE SAVED ENTRIES FROM GUI
#             #---------------<
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## UI SETUP
# #-------------------------------<
# # TKINTER WINDOW SETTINGS
# #---------------<
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# #-------------------------------<
# # TKINTER CANVAS SETTINGS
# #---------------<
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/30/Resources/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS LABELS
# #-------------------------------<
# # LABELS: WEBSITE
# #---------------<
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# #-------------------------------<
# # LABELS: EMAIL || USERNAME
# #---------------<
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# #-------------------------------<
# # LABELS: PASSWORD
# #---------------<
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS ENTRIES
# #-------------------------------<
# # ENTRIES: WEBSITE
# #---------------<
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# #-------------------------------<
# ## ENTRIES: EMAIL || USERNAME
# #---------------<
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# #-------------------------------<
# ## ENTRIES: PASSWORD
# #---------------<
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS BUTTONS
# #-------------------------------<
# ## BUTTONS: GENERATE RANDOM PASSWORD
# #---------------<
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# #-------------------------------<
# ## BUTTONS: SAVE INFORMATION TO FILE
# #---------------<
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## WINDOW INITIALIZATION
# #---------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
#:::::::::::::::::::::::::::::::::::::::::::::::<
## SUCCESS: DATA FROM JSON FILE WILL BE PRINTED TO CONSOLE IN PYTHON DICTIONARY FORMAT
#---------------<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM5_V0 = {
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## IMPORTS
# #-------------------------------<
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# import json
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## PASSWORD GENERATOR
# #-------------------------------<
# # CHARACTER LISTS
# #---------------<
# def gen_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     ## LIST COMPREHENSION
#     #-------------------------------<
#     # COMPREHENSION: LETTERS
#     #---------------<
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     #-------------------------------<
#     # COMPREHENSION: NUMBERS
#     #---------------<
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     #-------------------------------<
#     # COMPREHENSION: SYMBOLS
#     #---------------<
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # LIST ASSIGNMENT FROM COMPREHENSION
#     #---------------<
#     password_list = password_letters + password_numbers + password_symbols
#     #:::::::::::::::::::::::::::::::::::::::::::::::<
#     # RANDOM SHUFFLE OF LIST ASSIGNMENT
#     #---------------<
#     shuffle(password_list)
#     #-------------------------------<
#     # ASSIGNMENT TO STRING VARIABLE
#     #---------------<
#     password = ''.join(password_list)
#     #-------------------------------<
#     # STRING TO ENTRY INSERTION
#     #---------------<
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## SAVE PASSWORD
# #-------------------------------<
# def save():
#     #-------------------------------<
#     ## GET USER INPUTS
#     #---------------<
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     #-------------------------------<
#     ## ESTABLISH JSON FORMAT
#     #---------------<
#     new_data = {
#         website: {
#         'email': email,
#         'password': password,
#     }}
#     #-------------------------------<
#     ## IF INVALID OR MISSING INPUTS
#     #---------------<
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     #-------------------------------<
#     ## ELSE IF INPUTS VALID, SAVE TO FILE
#     #---------------<
#     else:
#         #-------------------------------<
#         ## OPEN AND WRITE TO SPECIFIED JSON FILE
#         #---------------<
#         with open('data.json', 'w') as data_file:
#             json.dump(new_data, data_file, indent=4)
#             #-------------------------------<
#             ## REMOVE SAVED ENTRIES FROM GUI
#             #---------------<
#             website_entry.delete(0, END)
#             password_entry.delete(0, END)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## UI SETUP
# #-------------------------------<
# # TKINTER WINDOW SETTINGS
# #---------------<
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# #-------------------------------<
# # TKINTER CANVAS SETTINGS
# #---------------<
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/30/Resources/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS LABELS
# #-------------------------------<
# # LABELS: WEBSITE
# #---------------<
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# #-------------------------------<
# # LABELS: EMAIL || USERNAME
# #---------------<
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# #-------------------------------<
# # LABELS: PASSWORD
# #---------------<
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS ENTRIES
# #-------------------------------<
# # ENTRIES: WEBSITE
# #---------------<
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# #-------------------------------<
# ## ENTRIES: EMAIL || USERNAME
# #---------------<
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# #-------------------------------<
# ## ENTRIES: PASSWORD
# #---------------<
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## CANVAS BUTTONS
# #-------------------------------<
# ## BUTTONS: GENERATE RANDOM PASSWORD
# #---------------<
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# #-------------------------------<
# ## BUTTONS: SAVE INFORMATION TO FILE
# #---------------<
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# ## WINDOW INITIALIZATION
# #---------------<
# window.mainloop()
# #:::::::::::::::::::::::::::::::::::::::::::::::<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
# PROJECT: NATO PHONETIC ALPHABET ERROR HANDLING
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM4_V2 = {
# #================================================================
# ## IMPORTS
# ##---------------------------------------------------------------
# import pandas
# #================================================================
# ## CSV DATA EXTRACTION
# ##---------------------------------------------------------------
# data = pandas.read_csv('./W3/30/Resources/nato_phonetic_alphabet.csv')
# #================================================================
# # PHONETIC ALPHABET DICTIONARY
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # DICTIONARY VARIABLE
# ##---------------------------------------------------------------
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# ##---------------------------------------------------------------
# # PRINT DICTIONARY TO CONSOLE
# ##---------------------------------------------------------------
# print(phonetic_dict)
# #================================================================
# # PHONETICIZE USER INPUT
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # USER INPUT
# ##---------------------------------------------------------------
# def generate_phonetics():
#     word = input('Enter a word: ').upper()
#     ##---------------------------------------------------------------
#     # TRY TO ASSIGN LIST VALUES BASED ON INPUT CHARACTERS
#     ##---------------------------------------------------------------
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     ##---------------------------------------------------------------
#     # EXCEPT IF USER INPUTS CHARACTERS THAT ARE NOT LETTERS
#     ##---------------------------------------------------------------
#     except KeyError:
#         print('Function requires only letters.')
#         generate_phonetics()
#     ##---------------------------------------------------------------
#     # ELSE IF EVERYTHING RUNS FINE PRINT OUTPUT
#     ##---------------------------------------------------------------
#     else:
#         print(output_list)
# ##---------------------------------------------------------------
# # PRINT RESULT OF USER INPUT LIST
# ##---------------------------------------------------------------
# generate_phonetics()
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM4_V1 = {
# #================================================================
# ## IMPORTS
# ##---------------------------------------------------------------
# import pandas
# #================================================================
# ## CSV DATA EXTRACTION
# ##---------------------------------------------------------------
# data = pandas.read_csv('./W3/30/Resources/nato_phonetic_alphabet.csv')
# #================================================================
# # PHONETIC ALPHABET DICTIONARY
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # DICTIONARY VARIABLE
# ##---------------------------------------------------------------
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# ##---------------------------------------------------------------
# # PRINT DICTIONARY TO CONSOLE
# ##---------------------------------------------------------------
# print(phonetic_dict)
# #================================================================
# # PHONETICIZE USER INPUT
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # USER INPUT
# ##---------------------------------------------------------------
# word = input('Enter a word: ').upper()
# ##---------------------------------------------------------------
# # ASSIGN LIST VALUES BASED ON INPUT CHARACTERS
# ##---------------------------------------------------------------
# output_list = [phonetic_dict[letter] for letter in word]
# ##---------------------------------------------------------------
# # PRINT RESULT OF USER INPUT LIST
# ##---------------------------------------------------------------
# print(output_list)
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM4_V0 = {
# #================================================================
# ## IMPORTS
# ##---------------------------------------------------------------
# import pandas
# #================================================================
# ## CSV DATA EXTRACTION
# ##---------------------------------------------------------------
# data = pandas.read_csv('nato_phonetic_alphabet.csv')
# #================================================================
# # PHONETIC ALPHABET DICTIONARY
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # DICTIONARY VARIABLE
# ##---------------------------------------------------------------
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# ##---------------------------------------------------------------
# # PRINT DICTIONARY TO CONSOLE
# ##---------------------------------------------------------------
# print(phonetic_dict)
# #================================================================
# # PHONETICIZE USER INPUT
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # USER INPUT
# ##---------------------------------------------------------------
# word = input('Enter a word: ').upper()
# ##---------------------------------------------------------------
# # ASSIGN LIST VALUES BASED ON INPUT CHARACTERS
# ##---------------------------------------------------------------
# output_list = [phonetic_dict[letter] for letter in word]
# ##---------------------------------------------------------------
# # PRINT RESULT OF USER INPUT LIST
# ##---------------------------------------------------------------
# print(output_list)
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
# PRACTICAL EXAMPLE VIA SUMMARIZING FACEBOOK LIKES EXERCISE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM3_V1 = {
# #================================================================
# ## FACEBOOK LIKES CALCULATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## FACEBOOK POST METADATA
# ##---------------------------------------------------------------
# facebook_posts = eval(input([{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]))
# ##---------------------------------------------------------------
# #================================================================
# # PROVIDE INTEGER STARTING VARIABLE
# ##---------------------------------------------------------------
# total_likes = 0
# #================================================================
# # LOOP THROUGH POSTS
# ##---------------------------------------------------------------
# for post in facebook_posts:
#     ##---------------------------------------------------------------
#     # TRY TO SUMMARIZE TOTAL LIKES INTO EXISTING VARIABLE
#     ##---------------------------------------------------------------
#     try:
#         total_likes = total_likes + post['Likes']
#     ##---------------------------------------------------------------
#     # IF EXCEPTION DUE TO KEYERROR IN TOTAL_LIKES, PASS OVER OFFENDING DATA
#     ##---------------------------------------------------------------
#     except KeyError:
#         pass
# #================================================================
# # PRINT RESULT
# ##---------------------------------------------------------------
# print(total_likes)
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM3_V0 = {
# #================================================================
# ## FACEBOOK LIKES CALCULATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## FACEBOOK POST METADATA
# ##---------------------------------------------------------------
# facebook_posts = eval(input([{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]))
# ##---------------------------------------------------------------
# #================================================================
# # PROVIDE INTEGER STARTING VARIABLE
# ##---------------------------------------------------------------
# total_likes = 0
# #================================================================
# # LOOP THROUGH POSTS
# ##---------------------------------------------------------------
# for post in facebook_posts:
#     ##---------------------------------------------------------------
#     # SUMMARIZE TOTAL LIKES INTO EXISTING VARIABLE
#     ##---------------------------------------------------------------
#     total_likes = total_likes + post['Likes']
# #================================================================
# # PRINT RESULT
# ##---------------------------------------------------------------
# print(total_likes)
# #================================================================
# # CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: KEYERROR DUE TO NOT ALL DICTIONARIES CONTAINING LIKES
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
# PRACTICAL EXAMPLE VIA MAKING A PIE EXERCISE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM2_V1 = {
# #================================================================
# ## MAKING A PIE
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # FRUIT INPUT
# ##---------------------------------------------------------------
# fruits = eval(input(['Apple', 'Pear', 'Orange']))
# #================================================================
# # PIE FUNCTION
# ##---------------------------------------------------------------
# def make_pie(index):
#     ##---------------------------------------------------------------
#     # TRY TO CALL THE INDEX
#     ##---------------------------------------------------------------
#     try:
#         fruit = fruits[index]
#     ##---------------------------------------------------------------
#     # IF EXCEPTION IS EQUAL TO INDEXERROR
#     ##---------------------------------------------------------------
#     except IndexError:
#         print('Fruit Pie')
#     ##---------------------------------------------------------------
#     # ELSE PRINT
#     ##---------------------------------------------------------------
#     else:
#         print(fruit + 'Pie')
# #================================================================
# # CALL INDEX
# ##---------------------------------------------------------------
# make_pie(4)
# #================================================================
# # CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: INDEX OUT OF RANGE
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM2_V0 = {
# #================================================================
# ## SECTION NAME
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# # SECTION PART
# ##---------------------------------------------------------------
# fruits = eval(input())
# #================================================================
# # SECTION PART
# ##---------------------------------------------------------------
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + 'pie')
# ##---------------------------------------------------------------
# # SECTION PART
# ##---------------------------------------------------------------
# make_pie(4)
# #================================================================
# # CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: INDEX OUT OF RANGE
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
# PRACTICAL EXAMPLE VIA BMI EXERCISE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM2_V1 = {
# #================================================================
# ## BMI CALCULATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## BMI INPUTS
# ##---------------------------------------------------------------
# height = float(input('Height: '))
# weight = int(input('Weight: '))
# ##---------------------------------------------------------------
# # RAISE EXCEPTION: HUMAN HEIGHT VERIFY
# ##---------------------------------------------------------------
# if height > 3:
#     raise ValueError('Human height is typically three (3) meters or less.')
# #================================================================
# # BMI CALCULATION FUNCTION
# ##---------------------------------------------------------------
# bmi = weight / height ** 2
# ##---------------------------------------------------------------
# # BMI DISPLAY
# ##---------------------------------------------------------------
# print(bmi)
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V0 = {
# #================================================================
# ## BMI CALCULATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## BMI INPUTS
# ##---------------------------------------------------------------
# height = float(input('Height: '))
# weight = int(input('Weight: '))
# ##---------------------------------------------------------------
# #================================================================
# # BMI CALCULATION FUNCTION
# ##---------------------------------------------------------------
# bmi = weight / (height * height)
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
# COUNTERING ERRORS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V9 = {
# #================================================================
# ## ERROR COUNTER EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TRY TO OPEN THE SPECIFIED FILE
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     #---------------------------------------------------------------
#     # AFTER OPEN FILE, PRINT VALUE OF SPECIFIED KEY
#     #---------------------------------------------------------------
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# ##---------------------------------------------------------------
# ## EXCEPT IF NONEXISTENT FILE, CREATE FILE
# ##---------------------------------------------------------------
# except FileNotFoundError:
#   file = open('a_file.txt', 'w')
#   file.write('Something')
# ##---------------------------------------------------------------
# ## EXCEPT IF KEYERROR FROM DICTIONARY ACCESS, PRINT ERROR
# ##---------------------------------------------------------------
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# ##---------------------------------------------------------------
# ## ELSE IF NO ERROR
# ##---------------------------------------------------------------
# else:
#    content = file.read()
#    print(content)
# ##---------------------------------------------------------------
# ## FINALLY NO MATTER THE RESULTS OF ABOVE
# ##---------------------------------------------------------------
# finally:
#    raise TypeError('This is an error that I made up.')
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: FORCES AN EXCEPTION
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V8 = {
# #================================================================
# ## ERROR COUNTER EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TRY TO OPEN THE SPECIFIED FILE
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     #---------------------------------------------------------------
#     # AFTER OPEN FILE, PRINT VALUE OF SPECIFIED KEY
#     #---------------------------------------------------------------
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# ##---------------------------------------------------------------
# ## EXCEPT IF NONEXISTENT FILE, CREATE FILE
# ##---------------------------------------------------------------
# except FileNotFoundError:
#   file = open('a_file.txt', 'w')
#   file.write('Something')
# ##---------------------------------------------------------------
# ## EXCEPT IF KEYERROR FROM DICTIONARY ACCESS, PRINT ERROR
# ##---------------------------------------------------------------
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# ##---------------------------------------------------------------
# ## ELSE IF NO ERROR
# ##---------------------------------------------------------------
# else:
#    content = file.read()
#    print(content)
# ##---------------------------------------------------------------
# ## FINALLY NO MATTER THE RESULTS OF ABOVE
# ##---------------------------------------------------------------
# finally:
#    file.close()
#    print('File was closed.')
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: CURRENT STRUCTURE CLOSES FILE NO MATTER SUCCESS OR FAILURE OF CODE
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V7 = {
# #================================================================
# ## ERROR COUNTER EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TRY TO OPEN THE SPECIFIED FILE
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     #---------------------------------------------------------------
#     # AFTER OPEN FILE, PRINT VALUE OF SPECIFIED KEY
#     #---------------------------------------------------------------
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# ##---------------------------------------------------------------
# ## EXCEPT IF NONEXISTENT FILE, CREATE FILE
# ##---------------------------------------------------------------
# except FileNotFoundError:
#   file = open('a_file.txt', 'w')
#   file.write('Something')
# ##---------------------------------------------------------------
# ## EXCEPT IF KEYERROR FROM DICTIONARY ACCESS, PRINT ERROR
# ##---------------------------------------------------------------
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# ##---------------------------------------------------------------
# ## ELSE IF NO ERROR
# ##---------------------------------------------------------------
# else:
#    content = file.read()
#    print(content)
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: CURRENT STRUCTURE REQUIRES MULTIPLE RUNS TO DISPLAY END GOAL CORRECTLY
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V6 = {
# #================================================================
# ## ERROR COUNTER EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TRY TO OPEN THE SPECIFIED FILE
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     #---------------------------------------------------------------
#     # AFTER OPEN FILE, PRINT VALUE OF SPECIFIED KEY
#     #---------------------------------------------------------------
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['non_existent_key'])
# ##---------------------------------------------------------------
# ## EXCEPT IF NONEXISTENT FILE, CREATE FILE
# ##---------------------------------------------------------------
# except FileNotFoundError:
#   file = open('a_file.txt', 'w')
#   file.write('Something')
# ##---------------------------------------------------------------
# ## EXCEPT IF KEYERROR FROM DICTIONARY ACCESS, PRINT ERROR
# ##---------------------------------------------------------------
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# ##---------------------------------------------------------------
# ## ELSE IF NO ERROR
# ##---------------------------------------------------------------
# else:
#    content = file.read()
#    print(content)
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: IF FILE DOES NOT EXIST, NO ERROR IS PASSED BUT ELSE IS NEVER TRIGGERED
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V5 = {
# #================================================================
# ## ERROR COUNTER EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TRY TO OPEN THE SPECIFIED FILE
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     #---------------------------------------------------------------
#     # AFTER OPEN FILE, PRINT VALUE OF SPECIFIED KEY
#     #---------------------------------------------------------------
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['non_existent_key'])
# ##---------------------------------------------------------------
# ## IF NONEXISTENT FILE, CREATE FILE
# ##---------------------------------------------------------------
# except FileNotFoundError:
#   file = open('a_file.txt', 'w')
#   file.write('Something')
# ##---------------------------------------------------------------
# ## IF KEYERROR FROM DICTIONARY ACCESS, PRINT ERROR
# ##---------------------------------------------------------------
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: PURPOSEFUL ERROR RESULTS IN KEYERROR EXCEPTION BEING TRIGGERED
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V4 = {
# #================================================================
# ## ERROR COUNTER EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TRY TO OPEN THE SPECIFIED FILE
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     #---------------------------------------------------------------
#     # AFTER OPEN FILE, PRINT VALUE OF SPECIFIED KEY
#     #---------------------------------------------------------------
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['non_existent_key'])
# ##---------------------------------------------------------------
# ## IF NONEXISTENT FILE, CREATE FILE
# ##---------------------------------------------------------------
# except FileNotFoundError:
#   file = open('a_file.txt', 'w')
#   file.write('Something')
# ##---------------------------------------------------------------
# ## IF KEYERROR FROM DICTIONARY ACCESS, PRINT ERROR
# ##---------------------------------------------------------------
# except KeyError:
#     print('That key does not exist')
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: PURPOSEFUL ERROR RESULTS IN KEYERROR EXCEPTION BEING TRIGGERED
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V3 = {
# #================================================================
# ## ERROR EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## OPENING FILE THAT DOESNT EXIST WITH ERROR COUNTER
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['non_existent_key'])
# ##---------------------------------------------------------------
# ## IF TRY FAILS, CREATE FILE USING WRITE METHOD
# ##---------------------------------------------------------------
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('Something')
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: FILE COULD BE OPENED, BUT DICTIONARY VALUE DOES NOT EXIST
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V2 = {
# #================================================================
# ## ERROR EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## OPENING FILE THAT DOESNT EXIST WITH ERROR COUNTER
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['non_existent_key'])
# ##---------------------------------------------------------------
# ## IF TRY FAILS, CREATE FILE USING WRITE METHOD
# ##---------------------------------------------------------------
# except:
#     file = open('a_file.txt', 'w')
#     file.write('Something')
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: EXCEPT IS TOO BROAD, IF FILE EXISTS AND A_DICTIONARY WAS ACCESSED IMPROPERLY, THE EXCEPTION WOULD CREATE THE FILE ANYWAYS
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V1 = {
# #================================================================
# ## ERROR EXAMPLES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## OPENING FILE THAT DOESNT EXIST WITH ERROR COUNTER
# ##---------------------------------------------------------------
# try:
#     file = open('a_file.txt')
# ##---------------------------------------------------------------
# ## IF TRY FAILS, PRINT EXCEPTION
# ##---------------------------------------------------------------
# except:
#     print('There was an error.')
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V0 = {
#================================================================
## ERROR EXAMPLES
##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## OPENING FILE THAT DOESNT EXIST
##---------------------------------------------------------------
# with open('a_file.txt') as file:
#     file.read()
##---------------------------------------------------------------
## ACCESSING KEY THAT DOESNT EXIST
##---------------------------------------------------------------
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']
##---------------------------------------------------------------
## ACCESSING INDEX THAT DOESNT EXIST
##---------------------------------------------------------------
# fruit_list = ['apple', 'banana', 'pear']
# fruit = fruit_list[3]
##---------------------------------------------------------------
## VALID TYPE FAILURE
##---------------------------------------------------------------
# text = 'abc'
# print(text + 5)
#================================================================
## ERROR COUNTER EXAMPLES
##---------------------------------------------------------------
# try:
#     print('Something that might cause an exception')
# except:
#     if something == ignore:
#         print('Do this if there was an exception')
# else:
#     print('Do this if there were no exceptions')
# finally:
#     print('Do this no matter what error occurs')
##---------------------------------------------------------------
#================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################