#################################################################
#================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FINAL PROGRAM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
## IMPORTS
##---------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
##---------------------------------------------------------------
##===============================================================
## PASSWORD GENERATOR
##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## CHARACTER LISTS
##---------------------------------------------------------------
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
    ##===============================================================
    ## LIST COMPREHENSION
    ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    ## COMPREHENSION: LETTERS
    ##---------------------------------------------------------------
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    ##---------------------------------------------------------------
    ## COMPREHENSION: NUMBERS
    ##---------------------------------------------------------------
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    ##---------------------------------------------------------------
    ## COMPREHENSION: SYMBOLS
    ##---------------------------------------------------------------
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    ##===============================================================
    ## LIST ASSIGNMENT FROM COMPREHENSION
    ##---------------------------------------------------------------
    password_list = password_letters + password_numbers + password_symbols
    ##===============================================================
    ## RANDOM SHUFFLE OF LIST ASSIGNMENT
    ##---------------------------------------------------------------
    shuffle(password_list)
    ##---------------------------------------------------------------
    ## ASSIGNMENT TO STRING VARIABLE
    ##---------------------------------------------------------------
    password = ''.join(password_list)
    ##---------------------------------------------------------------
    ## STRING TO ENTRY INSERTION
    ##---------------------------------------------------------------
    password_entry.insert(0, password)
    pyperclip.copy(password)
    ##---------------------------------------------------------------
##===============================================================
## SAVE PASSWORD
##---------------------------------------------------------------
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    ##---------------------------------------------------------------
    ## VALIDATE INPUTS
    ##---------------------------------------------------------------
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title='Oops', message='All fields required, please try again.')
    else:
        ##---------------------------------------------------------------
        ## USER VERIFY
        ##---------------------------------------------------------------
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nDo you approve?')
        if is_ok:
            ##---------------------------------------------------------------
            ## SAVE TO FILE
            ##---------------------------------------------------------------
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
##---------------------------------------------------------------
##===============================================================
## UI SETUP
##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## TKINTER WINDOW SETTINGS
##---------------------------------------------------------------
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
##---------------------------------------------------------------
## TKINTER CANVAS SETTINGS
##---------------------------------------------------------------
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='W3/29/Resources/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
##===============================================================
## CANVAS LABELS
##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## LABELS: WEBSITE
##---------------------------------------------------------------
website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)
##---------------------------------------------------------------
## LABELS: EMAIL || USERNAME
##---------------------------------------------------------------
email_label = Label(text='Email/Username: ')
email_label.grid(row=2, column=0)
##---------------------------------------------------------------
## LABELS: PASSWORD
##---------------------------------------------------------------
password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)
##===============================================================
## CANVAS ENTRIES
##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## ENTRIES: WEBSITE
##---------------------------------------------------------------
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
##---------------------------------------------------------------
## ENTRIES: EMAIL || USERNAME
##---------------------------------------------------------------
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, 'cooteybug@gmail.com')
##---------------------------------------------------------------
## ENTRIES: PASSWORD
##---------------------------------------------------------------
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
##===============================================================
## CANVAS BUTTONS
##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
## BUTTONS: GENERATE RANDOM PASSWORD
##---------------------------------------------------------------
generate_password_button = Button(text='Generate Password', command=gen_password)
generate_password_button.grid(row=3, column=3)
##---------------------------------------------------------------
## BUTTONS: SAVE INFORMATION TO FILE
##---------------------------------------------------------------
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
##---------------------------------------------------------------
##===============================================================
## WINDOW INITIALIZATION
##---------------------------------------------------------------
window.mainloop()
##---------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
# PROJECT: PASSWORD MANAGER
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V13 = {
# #================================================================
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# import pyperclip
# ##---------------------------------------------------------------
# ##===============================================================
# ## PASSWORD GENERATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## CHARACTER LISTS
# ##---------------------------------------------------------------
# def gen_password():
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
#     ##===============================================================
#     ## LIST COMPREHENSION
#     ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#     ## COMPREHENSION: LETTERS
#     ##---------------------------------------------------------------
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     ##---------------------------------------------------------------
#     ## COMPREHENSION: NUMBERS
#     ##---------------------------------------------------------------
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
#     ##---------------------------------------------------------------
#     ## COMPREHENSION: SYMBOLS
#     ##---------------------------------------------------------------
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     ##===============================================================
#     ## LIST ASSIGNMENT FROM COMPREHENSION
#     ##---------------------------------------------------------------
#     password_list = password_letters + password_numbers + password_symbols
#     ##===============================================================
#     ## RANDOM SHUFFLE OF LIST ASSIGNMENT
#     ##---------------------------------------------------------------
#     shuffle(password_list)
#     ##---------------------------------------------------------------
#     ## ASSIGNMENT TO STRING VARIABLE
#     ##---------------------------------------------------------------
#     password = ''.join(password_list)
#     ##---------------------------------------------------------------
#     ## STRING TO ENTRY INSERTION
#     ##---------------------------------------------------------------
#     password_entry.insert(0, password)
#     pyperclip.copy(password)
#     ##---------------------------------------------------------------
# ##===============================================================
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     ##---------------------------------------------------------------
#     ## VALIDATE INPUTS
#     ##---------------------------------------------------------------
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     else:
#         ##---------------------------------------------------------------
#         ## USER VERIFY
#         ##---------------------------------------------------------------
#         is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nDo you approve?')
#         if is_ok:
#             ##---------------------------------------------------------------
#             ## SAVE TO FILE
#             ##---------------------------------------------------------------
#             with open('data.txt', 'a') as data_file:
#                 data_file.write(f'{website} | {email} | {password}\n')
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
# ##---------------------------------------------------------------
# ##===============================================================
# ## UI SETUP
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##===============================================================
# ## CANVAS LABELS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## LABELS: WEBSITE
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# ##---------------------------------------------------------------
# ## LABELS: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# ##---------------------------------------------------------------
# ## LABELS: PASSWORD
# ##---------------------------------------------------------------
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##===============================================================
# ## CANVAS ENTRIES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## ENTRIES: WEBSITE
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# ##---------------------------------------------------------------
# ## ENTRIES: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# ##---------------------------------------------------------------
# ## ENTRIES: PASSWORD
# ##---------------------------------------------------------------
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##===============================================================
# ## CANVAS BUTTONS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## BUTTONS: GENERATE RANDOM PASSWORD
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password', command=gen_password)
# generate_password_button.grid(row=3, column=3)
# ##---------------------------------------------------------------
# ## BUTTONS: SAVE INFORMATION TO FILE
# ##---------------------------------------------------------------
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ##===============================================================
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V12 = {
# #================================================================
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# from tkinter import messagebox
# from random import choice, randint, shuffle
# ##---------------------------------------------------------------
# ##===============================================================
# ## PASSWORD GENERATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## CHARACTER LISTS
# ##---------------------------------------------------------------
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
# ##===============================================================
# ## LIST COMPREHENSION
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## COMPREHENSION: LETTERS
# ##---------------------------------------------------------------
# password_letters = [choice(letters) for _ in range(randint(8, 10))]
# ##---------------------------------------------------------------
# ## COMPREHENSION: NUMBERS
# ##---------------------------------------------------------------
# password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
# ##---------------------------------------------------------------
# ## COMPREHENSION: SYMBOLS
# ##---------------------------------------------------------------
# password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
# ##===============================================================
# ## LIST ASSIGNMENT FROM COMPREHENSION
# ##---------------------------------------------------------------
# password_list = password_letters + password_numbers + password_symbols
# ##===============================================================
# ## RANDOM SHUFFLE OF LIST ASSIGNMENT
# ##---------------------------------------------------------------
# shuffle(password_list)
# ##---------------------------------------------------------------
# ## ASSIGNMENT TO STRING VARIABLE
# ##---------------------------------------------------------------
# password = ''
# for char in password_list:
#     password += char
# ##---------------------------------------------------------------
# ## STRING TO PRINT
# ##---------------------------------------------------------------
# print(f'Your password is: {password}')
# ##---------------------------------------------------------------
# ##===============================================================
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     ##---------------------------------------------------------------
#     ## VALIDATE INPUTS
#     ##---------------------------------------------------------------
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     else:
#         ##---------------------------------------------------------------
#         ## USER VERIFY
#         ##---------------------------------------------------------------
#         is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nDo you approve?')
#         if is_ok:
#             ##---------------------------------------------------------------
#             ## SAVE TO FILE
#             ##---------------------------------------------------------------
#             with open('data.txt', 'a') as data_file:
#                 data_file.write(f'{website} | {email} | {password}\n')
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
# ##---------------------------------------------------------------
# ##===============================================================
# ## UI SETUP
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##===============================================================
# ## CANVAS LABELS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## LABELS: WEBSITE
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# ##---------------------------------------------------------------
# ## LABELS: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# ##---------------------------------------------------------------
# ## LABELS: PASSWORD
# ##---------------------------------------------------------------
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##===============================================================
# ## CANVAS ENTRIES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## ENTRIES: WEBSITE
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# ##---------------------------------------------------------------
# ## ENTRIES: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# ##---------------------------------------------------------------
# ## ENTRIES: PASSWORD
# ##---------------------------------------------------------------
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##===============================================================
# ## CANVAS BUTTONS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## BUTTONS: GENERATE RANDOM PASSWORD
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)
# ##---------------------------------------------------------------
# ## BUTTONS: SAVE INFORMATION TO FILE
# ##---------------------------------------------------------------
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ##===============================================================
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V11 = {
# #================================================================
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# from tkinter import messagebox
# import random
# ##---------------------------------------------------------------
# ##===============================================================
# ## PASSWORD GENERATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## CHARACTER LISTS
# ##---------------------------------------------------------------
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
# ##---------------------------------------------------------------
# ## RANDOM SELECTIONS FROM CHARACTERS
# ##---------------------------------------------------------------
# nr_letters = random.randint(8, 10)
# nr_numbers = random.randint(2, 4)
# nr_symbols = random.randint(2, 4)
# ##===============================================================
# ## LIST COMPREHENSION
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## COMPREHENSION: LETTERS
# ##---------------------------------------------------------------
# password_letters = [random.choice(letters) for _ in range(nr_letters)]
# ##---------------------------------------------------------------
# ## COMPREHENSION: NUMBERS
# ##---------------------------------------------------------------
# password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
# ##---------------------------------------------------------------
# ## COMPREHENSION: SYMBOLS
# ##---------------------------------------------------------------
# password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
# ##===============================================================
# ## LIST ASSIGNMENT FROM COMPREHENSION
# ##---------------------------------------------------------------
# password_list = password_letters + password_numbers + password_symbols
# ##===============================================================
# ## RANDOM SHUFFLE OF LIST ASSIGNMENT
# ##---------------------------------------------------------------
# random.shuffle(password_list)
# ##---------------------------------------------------------------
# ## ASSIGNMENT TO STRING VARIABLE
# ##---------------------------------------------------------------
# password = ''
# for char in password_list:
#     password += char
# ##---------------------------------------------------------------
# ## STRING TO PRINT
# ##---------------------------------------------------------------
# print(f'Your password is: {password}')
# ##---------------------------------------------------------------
# ##===============================================================
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     ##---------------------------------------------------------------
#     ## VALIDATE INPUTS
#     ##---------------------------------------------------------------
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     else:
#         ##---------------------------------------------------------------
#         ## USER VERIFY
#         ##---------------------------------------------------------------
#         is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nDo you approve?')
#         if is_ok:
#             ##---------------------------------------------------------------
#             ## SAVE TO FILE
#             ##---------------------------------------------------------------
#             with open('data.txt', 'a') as data_file:
#                 data_file.write(f'{website} | {email} | {password}\n')
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
# ##---------------------------------------------------------------
# ##===============================================================
# ## UI SETUP
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##===============================================================
# ## CANVAS LABELS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## LABELS: WEBSITE
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# ##---------------------------------------------------------------
# ## LABELS: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# ##---------------------------------------------------------------
# ## LABELS: PASSWORD
# ##---------------------------------------------------------------
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##===============================================================
# ## CANVAS ENTRIES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## ENTRIES: WEBSITE
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# ##---------------------------------------------------------------
# ## ENTRIES: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# ##---------------------------------------------------------------
# ## ENTRIES: PASSWORD
# ##---------------------------------------------------------------
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##===============================================================
# ## CANVAS BUTTONS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## BUTTONS: GENERATE RANDOM PASSWORD
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)
# ##---------------------------------------------------------------
# ## BUTTONS: SAVE INFORMATION TO FILE
# ##---------------------------------------------------------------
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ##===============================================================
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V10 = {
# #================================================================
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# from tkinter import messagebox
# import random
# ##---------------------------------------------------------------
# ##===============================================================
# ## PASSWORD GENERATOR
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## CHARACTER LISTS
# ##---------------------------------------------------------------
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '-', '=']
# ##---------------------------------------------------------------
# ## RANDOM SELECTIONS FROM CHARACTERS
# ##---------------------------------------------------------------
# nr_letters = random.randint(8, 10)
# nr_numbers = random.randint(2, 4)
# nr_symbols = random.randint(2, 4)
# ##---------------------------------------------------------------
# ## EMPTY LIST VARIABLE
# ##---------------------------------------------------------------
# password_list = []
# ##===============================================================
# ## RANDOM ASSIGNEMENT TO EMPTY LIST
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## RANDOM ASSIGNMENT: LETTERS
# ##---------------------------------------------------------------
# for char in range(nr_letters):
#     password_list.append(random.choice(letters))
# ##---------------------------------------------------------------
# ## RANDOM ASSIGNMENT: NUMBERS
# ##---------------------------------------------------------------
# for char in range(nr_numbers):
#     password_list += random.choice(numbers)
# ##---------------------------------------------------------------
# ## RANDOM ASSIGNMENT: SYMBOLS
# ##---------------------------------------------------------------
# for char in range(nr_symbols):
#     password_list += random.choice(symbols)
# ##===============================================================
# ## RANDOM SHUFFLE OF RANDOM ASSIGNMENT
# ##---------------------------------------------------------------
# random.shuffle(password_list)
# ##---------------------------------------------------------------
# ## ASSIGNMENT TO STRING VARIABLE
# ##---------------------------------------------------------------
# password = ''
# for char in password_list:
#     password += char
# ##---------------------------------------------------------------
# ## STRING TO PRINT
# ##---------------------------------------------------------------
# print(f'Your password is: {password}')
# ##---------------------------------------------------------------
# ##===============================================================
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     ##---------------------------------------------------------------
#     ## VALIDATE INPUTS
#     ##---------------------------------------------------------------
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     else:
#         ##---------------------------------------------------------------
#         ## USER VERIFY
#         ##---------------------------------------------------------------
#         is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nDo you approve?')
#         if is_ok:
#             ##---------------------------------------------------------------
#             ## SAVE TO FILE
#             ##---------------------------------------------------------------
#             with open('data.txt', 'a') as data_file:
#                 data_file.write(f'{website} | {email} | {password}\n')
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)
# ##---------------------------------------------------------------
# ##===============================================================
# ## UI SETUP
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##===============================================================
# ## CANVAS LABELS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## LABELS: WEBSITE
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# ##---------------------------------------------------------------
# ## LABELS: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# ##---------------------------------------------------------------
# ## LABELS: PASSWORD
# ##---------------------------------------------------------------
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##===============================================================
# ## CANVAS ENTRIES
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## ENTRIES: WEBSITE
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# ##---------------------------------------------------------------
# ## ENTRIES: EMAIL || USERNAME
# ##---------------------------------------------------------------
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')
# ##---------------------------------------------------------------
# ## ENTRIES: PASSWORD
# ##---------------------------------------------------------------
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##===============================================================
# ## CANVAS BUTTONS
# ##vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# ## BUTTONS: GENERATE RANDOM PASSWORD
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)
# ##---------------------------------------------------------------
# ## BUTTONS: SAVE INFORMATION TO FILE
# ##---------------------------------------------------------------
# add_button = Button(text='Add', width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ##===============================================================
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V9 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# from tkinter import messagebox
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     ##---------------------------------------------------------------
#     ## VALIDATE INPUTS
#     ##---------------------------------------------------------------
#     if len(website) == 0 or len(password) == 0 or len(email) == 0:
#         messagebox.showinfo(title='Oops', message='All fields required, please try again.')
#     else:
#         ##---------------------------------------------------------------
#         ## USER VERIFY
#         ##---------------------------------------------------------------
#         is_ok = messagebox.askokcancel(title=website, message=f'These are the details enter:\nEmail: {email}\nPassword: {password}\nDo you approve?')
#         if is_ok:
#             ##---------------------------------------------------------------
#             ## SAVE TO FILE
#             ##---------------------------------------------------------------
#             with open('data.txt', 'a') as data_file:
#                 data_file.write(f'{website} | {email} | {password}\n')
#                 website_entry.delete(0, END)
#                 password_entry.delete(0, END)

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## CANVAS LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)

# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)

# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##---------------------------------------------------------------
# ## CANVAS ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')

# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##---------------------------------------------------------------
# ## CANVAS BUTTONS
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)

# add_button = Button(text='Add', width=36)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: WINDOW DOES NOT POP UP, FUNCTION CALL DOES NOT EXIST
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V8 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# from tkinter import messagebox
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     ##---------------------------------------------------------------
#     ## USER VERIFY
#     ##---------------------------------------------------------------
#     messagebox.showinfo(title='Title', message='Message')
#     ##---------------------------------------------------------------
#     ## SAVE TO FILE
#     ##---------------------------------------------------------------
#     with open('data.txt', 'a') as data_file:
#         data_file.write(f'{website} | {email} | {password}\n')
#         website_entry.delete(0, END)
#         password_entry.delete(0, END)

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## CANVAS LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)

# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)

# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##---------------------------------------------------------------
# ## CANVAS ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')

# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##---------------------------------------------------------------
# ## CANVAS BUTTONS
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)

# add_button = Button(text='Add', width=36)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: WORKS, BUT ONLY SHOWS A TEMPORARY EXAMPLE WINDOW ON PRESS
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V7 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     website = website_entry.get()
#     email = email_entry.get()
#     password = password_entry.get()
#     with open('data.txt', 'a') as data_file:
#         data_file.write(f'{website} | {email} | {password}')
#         website_entry.delete(0, END)
#         password_entry.delete(0, END)

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## CANVAS LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)

# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)

# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##---------------------------------------------------------------
# ## CANVAS ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')

# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##---------------------------------------------------------------
# ## CANVAS BUTTONS
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)

# add_button = Button(text='Add', width=36)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: WORKS, HOWEVER APPENDS ADDED DATA TO END OF PREVIOUS LINE, CAUSING COMBINED, CONVOLUTED, AND UNREADABLE LINES OF INFORMATION
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V6 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# def save():
#     data_file = open('data.txt', 'a')
# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## CANVAS LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)

# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)

# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##---------------------------------------------------------------
# ## CANVAS ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(END, 'cooteybug@gmail.com')

# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##---------------------------------------------------------------
# ## CANVAS BUTTONS
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)

# add_button = Button(text='Add', width=36)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: CAN SAVE OPEN TO VARIABLE, BUT ALTERNATIVE PREFERRED
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V5 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=50, pady=50)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file='W3/29/logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## CANVAS LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)

# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)

# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##---------------------------------------------------------------
# ## CANVAS ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()

# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, 'cooteybug@gmail.com')

# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##---------------------------------------------------------------
# ## CANVAS BUTTONS
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)

# add_button = Button(text='Add', width=36)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # WARNING: FILE PATH IS DETERMINED BY PYTHON TERMINAL ADDRESS, NOT BY PYTHON FILE RELEVANT LOCATION; WARNING: FUNCTIONS, 0 IS AN ALTERNATIVE OF END
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V4 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=20, pady=20)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# log_img = PhotoImage(file='logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## CANVAS LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##---------------------------------------------------------------
# ## CANVAS ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##---------------------------------------------------------------
# ## CANVAS BUTTONS
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)
# add_button = Button(text='Add', width=36)
# add_button.grid(row=4, column=1, columnspan=2)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: PADDING IS INSUFFICIENT, LOGO IS NOT BEING FOUND IN DIRECTORY
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V3 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=20, pady=20)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# log_img = PhotoImage(file='logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## CANVAS LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website: ')
# website_label.grid(row=1, column=0)
# email_label = Label(text='Email/Username: ')
# email_label.grid(row=2, column=0)
# password_label = Label(text='Password: ')
# password_label.grid(row=3, column=0)
# ##---------------------------------------------------------------
# ## CANVAS ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1)
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1)
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
# ##---------------------------------------------------------------
# ## CANVAS BUTTONS
# ##---------------------------------------------------------------
# generate_password_button = Button(text='Generate Password')
# generate_password_button.grid(row=3, column=3)
# add_button = Button(text='Add')
# add_button.grid(row=4, column=1)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: USER INTERFACE IS NOT AS DESIRED, 'ADD' BUTTON IS TOO SMALL, PASSWORD BUTTON IS NOT CORRECTLY ALIGNED
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V2 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=20, pady=20)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# log_img = PhotoImage(file='logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
# ##---------------------------------------------------------------
# ## GRID LABELS
# ##---------------------------------------------------------------
# website_label = Label(text='Website')
# website_label.grid(row=1, column=0)
# email_label = Label(text='Email/Username')
# email_label.grid(row=2, column=0)
# password_label = Label(text='Password')
# password_label.grid(row=3, column=0, width=35)
# ##---------------------------------------------------------------
# ## ENTRIES
# ##---------------------------------------------------------------
# website_entry = Entry(width=35)
# email_entry = Entry(width=35)
# password_entry = Entry(width=21)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: WIDTH IS NOT A VALID GRID COMMAND
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V1 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------

# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# window.config(padx=20, pady=20)
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# log_img = PhotoImage(file='logo.png')
# canvas.create_image(100, 100, image=logo_img)
# canvas.pack()
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM1_V0 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## PASSWORD GENERATOR
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## SAVE PASSWORD
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## UI SETUP
# ##---------------------------------------------------------------
# ##---------------------------------------------------------------
# ## TKINTER WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# window.title('Password Manager')
# ##---------------------------------------------------------------
# ## TKINTER CANVAS SETTINGS
# ##---------------------------------------------------------------
# canvas = Canvas(height=200, width=200)
# log_img = PhotoImage(file='logo.png')
# canvas.create_image(image=logo_img)
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################
#================================================================
# TKINTER INTRODUCTION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V1 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# ##---------------------------------------------------------------
# ## GRID SETTINGS
# ##---------------------------------------------------------------
# r = Label(bg='red', width=20, height=5)
# r.grid(row=0, column=0)
# g = Label(bg='green', width=20, height=5)
# g.grid(row=1, column=1)
# b = Label(bg='blue', width=20, height=5)
# b.grid(row=2, column=0, columnspan=2)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROGRAM0_V0 = {
# #================================================================
# ##---------------------------------------------------------------
# ## IMPORTS
# ##---------------------------------------------------------------
# from tkinter import *
# ##---------------------------------------------------------------
# ## WINDOW SETTINGS
# ##---------------------------------------------------------------
# window = Tk()
# ##---------------------------------------------------------------
# ## GRID SETTINGS
# ##---------------------------------------------------------------
# r = Label(bg='red', width=20, height=5)
# r.grid(row=0, column=0)
# g = Label(bg='green', width=20, height=5)
# g.grid(row=1, column=1)
# b = Label(bg='blue', width=40, height=5)
# b.grid(row=2, column=0)
# ##---------------------------------------------------------------
# ## WINDOW INITIALIZATION
# ##---------------------------------------------------------------
# window.mainloop()
# ##---------------------------------------------------------------
# ## CODE RESULTS
# ##---------------------------------------------------------------
# # ERROR: UNDESIRED COLUMN EXTENSION
# ##---------------------------------------------------------------
# #================================================================
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================
#################################################################