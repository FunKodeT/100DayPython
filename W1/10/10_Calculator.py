#################################################################
#================================================================
# CALCULATOR PROGRAM
#----------------------------------------------------------------
from TextArt import logo

## FUNCTIONS
# ADD
def add(n1, n2):
    return n1 + n2
# SUBTRACT
def subtract(n1, n2):
    return n1 - n2
# MULTIPLY
def multiply(n1, n2):
    return n1 * n2
# DIVIDE
def divide(n1, n2):
    return n1 / n2

## DICTIONARY
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)

    num1 = float(input('What is the first number?:\n'))
    for index in operations:
        print(index)

    should_continue = True

    while should_continue:
        operation_symbol = input('Choose an operation from above:\n')
        num2 = float(input('What is the second number?:\n'))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM3_V7 = {
#================================================================

# from TextArt import logo

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2
# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2
# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2
# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# def calculator():
#     print(logo)

#     num1 = float(input('What is the first number?:\n'))
#     for index in operations:
#         print(index)

#     should_continue = True

#     while should_continue:
#         operation_symbol = input('Choose an operation from above:\n')
#         num2 = float(input('What is the second number?:\n'))

#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)

#         print(f'{num1} {operation_symbol} {num2} = {answer}')

#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n") == 'y':
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()

# calculator()

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V6 = {
#================================================================

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2
# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2
# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2
# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# def calculator():
#     num1 = int(input('What is the first number?:\n'))
#     for index in operations:
#         print(index)

#     should_continue = True

#     while should_continue:
#         operation_symbol = input('Choose an operation from above:\n')
#         num2 = int(input('What is the second number?:\n'))

#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)

#         print(f'{num1} {operation_symbol} {num2} = {first_answer}')

#         num3 = int(input('What is the next number?:\n'))

#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(calculation_function(num1, num2), num3)

#         print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')

#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n") == 'y':
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()

# calculator()

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V5 = {
#================================================================

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2
# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2
# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2
# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# ## INPUTS
# num1 = int(input('What is the first number?:\n'))
# # LOOP => OPERATIONS DICTIONARY
# for index in operations:
#     print(index)

# should_continue = True

# while should_continue:
#     operation_symbol = input('Choose an operation from above:\n')
#     num2 = int(input('What is the second number?:\n'))

#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)

#     print(f'{num1} {operation_symbol} {num2} = {first_answer}')

#     num3 = int(input('What is the next number?:\n'))

#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(calculation_function(num1, num2), num3)

#     print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:\n") == 'y':
#         num1 = answer
#     else:
#         should_continue = False

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V4 = {
#================================================================

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2
# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2
# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2
# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# ## INPUTS
# num1 = int(input('What is the first number?:\n'))
# num2 = int(input('What is the second number?:\n'))
# # LOOP => OPERATIONS DICTIONARY
# for index in operations:
#     print(index)
# operation_symbol = input('Choose an operation from above:\n')
# # CALCULATION FUNCTION
# calculation_function = operations[operation_symbol]
# first_answer = calculation_function(num1, num2)

# print(f'{num1} {operation_symbol} {num2} = {first_answer}')

# operation_symbol = input('Pick another operation:\n')
# num3 = int(input('What is the next number?:\n'))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(calculation_function(num1, num2), num3)

# print(f'{first_answer} {operation_symbol} {num3} = {second_answer}')

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V3 = {
#================================================================

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2
# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2
# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2
# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# ## INPUTS
# num1 = int(input('What is the first number?:\n'))
# num2 = int(input('What is the second number?:\n'))
# # LOOP => OPERATIONS DICTIONARY
# for index in operations:
#     print(index)
# operation_symbol = input('Choose an operation from above:\n')
# # CALCULATION FUNCTION
# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)

# print(f'{num1} {operation_symbol} {num2} = {answer}')

# operation_symbol = input('Pick another operation:\n')
# num3 = int(input('What is the next number?:\n'))
# calculation_function = operations[operation_symbol]
# answer = calculation_function(answer, num3)

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V2 = {
#================================================================

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2
# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2
# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2
# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# ## INPUTS
# num1 = int(input('What is the first number?:\n'))
# num2 = int(input('What is the second number?:\n'))
# # LOOP => OPERATIONS DICTIONARY
# for index in operations:
#     print(index)
# operation_symbol = input('Choose an operation from above:\n')

# def calculation (num1, num2):
#     if operation_symbol == '+':
#         answer = add(num1, num2)
#         return answer
#     elif operation_symbol == '-':
#         answer = subtract(num1, num2)
#         return answer
#     elif operation_symbol == '*':
#         answer = multiply(num1, num2)
#         return answer
#     else:
#         answer = divide(num1, num2)
#         return answer
    
# answer = calculation(num1, num2)

# print(f'{num1} {operation_symbol} {num2} = {answer}')

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V1 = {
#================================================================

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2

# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2

# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2

# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# operations = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

# ## INPUTS
# num1 = int(input('What is the first number?:\n'))
# num2 = int(input('What is the second number?:\n'))

# ## LOOP
# for index in operations:
#     print(operations[index])

# ## INTENT
# # function = operations['*']
# # function(2, 3)

#================================================================
}
#----------------------------------------------------------------
PROGRAM3_V0 = {
#================================================================

# ## FUNCTIONS
# # ADD
# def add(n1, n2):
#     return n1 + n2

# # SUBTRACT
# def subtract(n1, n2):
#     return n1 - n2

# # MULTIPLY
# def multiply(n1, n2):
#     return n1 * n2

# # DIVIDE
# def divide(n1, n2):
#     return n1 / n2

# ## DICTIONARY
# calcDictionary = {
#     '+': add(n1, n2),
#     '-': subtract(n1, n2),
#     '*': multiply(n1, n2),
#     '/': divide(n1, n2)
# }

#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM2_V8 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month == 2 and is_leap(year):
#     return 29
#   else:
#     return month_days[month - 1]

# year = int(input('What year do you want to check?\n'))
# month = int(input('What month in that year do you want to check?\n'))

# days = days_in_month(year, month)
# print(days)

# # What year do you want to check?; 2024; What month in that year do you want to check?; 2; True; 29;

#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V7 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   print(is_leap(year))
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != False and month != 2 or year == False:
#     conversion = month_days[int(month - 1)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# year = int(input('What year do you want to check?\n'))
# month = int(input('What month in that year do you want to check?\n'))

# days = days_in_month(year, month)
# print(days)

# # What year do you want to check?; 2024; What month in that year do you want to check?; 2; True; 29;

#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V6 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   print(is_leap(year))
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != False and month != 2 or year == False:
#     conversion = month_days[int(month)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# year = int(input('What year do you want to check?\n'))
# month = int(input('What month in that year do you want to check?\n'))

# days = days_in_month(year, month)
# print(days)

# # What year do you want to check?; 2024; What month in that year do you want to check?; 2; True; 29;

#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V5 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != False and month != 2 or year == False:
#     conversion = month_days[int(month)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# year = int(input('What year do you want to check?\n'))
# month = int(input('What month in that year do you want to check?\n'))

# print(is_leap(year))

# days = days_in_month(year, month)
# print(days)

# # What year do you want to check?; 2024; What month in that year do you want to check?; 2; True; 29;
# ## print(is_leap(year)) is in untouchable area

#----------------------------------------------------------------
}
#----------------------------------------------------------------
PROGRAM2_V4 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != False and month != 2:
#     conversion = month_days[int(month)]
#     return conversion
#   elif year == False:
#     conversion = month_days[int(month)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# year = int(input('What year do you want to check?\n'))
# month = int(input('What month in that year do you want to check?\n'))

# print(is_leap(year))

# days = days_in_month(year, month)
# print(days)

# # What year do you want to check?; 2024; What month in that year do you want to check?; 2; True; 29;

#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V3 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != False and month != 2:
#     conversion = month_days[int(month)]
#     return conversion
#   elif year == False:
#     conversion = month_days[int(month)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# print(is_leap(year))

# year = int(input('What year do you want to check?\n'))
# month = int(input('What month in that year do you want to check?\n'))

# days = days_in_month(year, month)
# print(days)

# # ERROR

#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V2 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != False and month != 2:
#     conversion = month_days[int(month)]
#     return conversion
#   elif year == False:
#     conversion = month_days[int(month)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# print(is_leap())

# year = int(input('What year do you want to check?\n'))
# month = int(input('What month in that year do you want to check?\n'))

# days = days_in_month(year, month)
# print(days)

# # ERROR

#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V1 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(iYear, iMonth):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != false and month != 2:
#     conversion = month_days[int(month)]
#     return conversion
#   elif year == false:
#     conversion = month_days[int(month)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# print(is_leap(year))

# # Your code above

# # Enter a year
# year = int(input('What year do you want to check?\n'))
# # Enter a month
# month = int(input('What month in that year do you want to check?\n'))

# days = days_in_month(year, month)
# print(days)

# # ERROR

#================================================================
}
#----------------------------------------------------------------
PROGRAM2_V0 = {
#================================================================
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(iYear, iMonth):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if year != false and month != 2:
#     conversion = month_days[int(month)]
#     return conversion
#   elif year == false:
#     conversion = month_days[int(month)]
#     return conversion
#   else:
#     conversion = 29
#     return conversion

# print(is_leap())

# # Your code above

# # Enter a year
# year = int(input('What year do you want to check?\n'))
# # Enter a month
# month = int(input('What month in that year do you want to check?\n'))

# days = days_in_month(year, month)
# print(days)

# # ERROR

#----------------------------------------------------------------

# instructions = {
# Convert the is_leap() functtion
# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# Create a new function called days_in_month()
# You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.

# days_in_month(year=2022, month=2)
# And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:

# 28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

# Hint
# Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

# Feel free to choose your own parameter names.

# Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

# Be careful with indentation.
# }

#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
PROGRAM1_V8 = {
#================================================================

# # RETURN AS AN EARLY EXIT
# def format_name(f_name, l_name):
#     """ Take a first and last name, format it to return the title case version of the name. """
#     if f_name == '' or l_name == '':
#         return "You didn't provide valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f'{formatted_f_name} {formatted_l_name}'

# print(format_name(input('What is your first name?\n'), input('What is your last name?\n')))

# # ALREADY USED FUNCTIONS WITH OUTPUTS
# length = len(formatted_name)

# # What is your first name?; matthew; What is your last name?; COOTEY; Matthew Cootey;

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V7 = {
#================================================================

# def format_name(f_name, l_name):
#     if f_name == '' or l_name == '':
#         return "You didn't provide valid inputs."
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f'{formatted_f_name} {formatted_l_name}'

# print(format_name(input('What is your first name?\n'), input('What is your last name?\n')))

# # What is your first name?; matthew; What is your last name?; COOTEY; Matthew Cootey;

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V6 = {
#================================================================

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f'{formatted_f_name} {formatted_l_name}'
#     print('This got printed')

# print(format_name('matthew', 'COOTEY'))

# # Matthew Cootey;

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V5 = {
#================================================================

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f'{formatted_f_name} {formatted_l_name}'

# print(format_name('matthew', 'COOTEY'))

# # Matthew Cootey;

# output = len('Matthew')
# # ^ Variable
# ##        ^ Function
# ###              ^ Input
# ####     ^------------^ Return

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V4 = {
#================================================================

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f'{formatted_f_name} {formatted_l_name}'

# print(format_name('matthew', 'COOTEY'))

# # Matthew Cootey;

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V3 = {
#================================================================

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f'{formatted_f_name} {formatted_l_name}'
#     ## f'{formatted_f_name} {formatted_l_name}' WILL REPLACE F_NAME, L_NAME IN THE FUNCTION CODE WHEN RETURNED

# formatted_name = format_name('matthew', 'COOTEY')
# ## f_name AND l_name WILL BE REPLACED WITH THE FORMATTED NAME IN THE FUNCTION, AND THAN THAT VALUE CAN BE SAVED IN A VARIABLE

# print(formatted_name)

# # Matthew Cootey;

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V2 = {
#================================================================

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     print(f'{formatted_f_name} {formatted_l_name}')


# format_name('matthew', 'COOTEY')

# # Matthew Cootey;

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V1 = {
#================================================================

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format_name('matthew', 'COOTEY')

# # Matthew; Cootey;

#================================================================
}
#----------------------------------------------------------------
PROGRAM1_V0 = {
#================================================================

# FUNCTIONS WITH OUTPUTS
# first = input('What is your first name?\n')
# last = input('What is your last name?\n')

# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()

# print(format_name(first, last))

# None

#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################
#================================================================
#----------------------------------------------------------------
TEMP1_V3 = {
#================================================================

# def my_function():
#     return 3 * 2

# output = my_function()

# print(output)

# # 6

#================================================================
}
#----------------------------------------------------------------
TEMP1_V2 = {
#================================================================
## WHEN RUNNING A FUNCTION, IF THE FUNCTION HAS A RETURN OUTPUT, THE CODE WILL REPLACE FUNCTION() WITH THE VALUE OF THE OUTPUT

# def my_function():
#     result = 3 * 2
#     return result

# trigger = True

# if trigger == True:
#     print(my_function())

# # 6

#================================================================
}
#----------------------------------------------------------------
TEMP1_V1 = {
#================================================================
# def my_function(something):
#     #Do this with something
#     #Then do this
#     #Finally do this

# my_function(123)
#================================================================
}
#----------------------------------------------------------------
TEMP1_V0 = {
#================================================================
# def my_function():
#     #Do this
#     #Then do this
#     #Finally do this

# my_function()
#================================================================
}
#----------------------------------------------------------------
#================================================================
#################################################################