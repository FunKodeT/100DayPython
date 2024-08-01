################################################################>
#=========================================================>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# EXERCISE_TRACKER = {
#=========================================================<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## IMPORTS
#-------------------------------------<
import os
from dotenv import load_dotenv
import requests
from datetime import datetime
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## ENVIRONMENT VARIABLES
#-------------------------------------<
load_dotenv('./W4/38/.env')
USERNAME = os.getenv('SHEETY_USERNAME')
PASSWORD = os.getenv('SHEETY_PASSWORD')
USER_ID = os.getenv('SHEETY_USER_ID')
PROJECT_ID = os.getenv('SHEETY_PROJECT_ID')
SHEET_ID = os.getenv('SHEETY_SHEET_ID')
API_KEY = os.getenv('NUTRITIONIX_API_KEY')
API_ID = os.getenv('NUTRITIONIX_API_ID')
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## GLOBAL VARIABLE
#-------------------------------------<
is_running = True
date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%X')
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## FUNCTIONS
#:::::::::::::::::::::::::::::::::::::<
# FUNCTION: CLEAR TERMINAL
#---------------------------<
def clear_terminal_window():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')

def shutdown_program():
    is_running = False
    return is_running
#:::::::::::::::::::::::::::::::::::::<
# FUNCTION: QUERY INPUT
#---------------------------<
def query_fn():
    query = input('What exercise did you do today?')
    return query
#:::::::::::::::::::::::::::::::::::::<
# FUNCTION: WEIGHT INPUT AND CONVERSION
#---------------------------<
def imperial_metric_weight():
    weight = input("How much do you weigh today?\n")
    unit = input('Pounds or Kilograms?\n')
    if unit.title() == 'Pounds' or unit.title() == 'Lbs':
        weight = round(float(weight) / 2.205)
        return weight
    elif unit.title() == 'Kilograms' or unit.title() == 'Kilos' or unit.title() == 'Kg' or unit.title() == 'Kgs':
        return weight
    else:
        continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
        if continue_or_nah.title() != 'Y':
            clear_terminal_window()
            imperial_metric_weight()
        elif continue_or_nah.title() == 'N':
            is_running = False
        else:
            is_running = False
#:::::::::::::::::::::::::::::::::::::<
# FUNCTION: HEIGHT INPUT AND CONVERSION
#---------------------------<
def imperial_metric_height():
    height = input("How tall are you?\n")
    unit = input('Feet, Inches, or Meters, or Centimeters?\n')
    if unit.title() == 'Inches' or unit.title() == 'In':
        height = round(float(height) * 2.54)
        return height
    elif unit.title() == 'Feet' or unit.title() == 'Ft':
            feet = int(height[:1])
            inch = int(height[2:])
            total = (feet * 12) + inch
            height = round(float(total) * 2.54)
            return height
    elif unit.title() == 'Meters' or unit.title() == 'M':
        height = round(float(height) / .01)
    elif unit.title() == 'Centimeters' or unit.title() == 'Cm':
        return height
    else:
        continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
        if continue_or_nah.title() != 'Y':
            clear_terminal_window()
            imperial_metric_height()
        elif continue_or_nah.title() == 'N':
            is_running = False
        else:
            is_running = False
#:::::::::::::::::::::::::::::::::::::<
# FUNCTION: AGE
#---------------------------<
def user_age():
    age = input('How old are you?\n')
    return age
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## NUTRITIONIX
#:::::::::::::::::::::::::::::::::::::<
# NUTRITIONIX: URLS
#---------------------------<
nutritionix_end = 'https://trackapi.nutritionix.com/v2/natural/exercise'
#:::::::::::::::::::::::::::::::::::::::::::::::<
# NUTRITIONIX: HEADERS
#---------------------------<
headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# SHEETY
#:::::::::::::::::::::::::::::::::::::<
# SHEETY: URLS
#---------------------------<
sheety_end = f'https://api.sheety.co/{USER_ID}/{PROJECT_ID}/{SHEET_ID}'
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# PROGRAM: FUNCTION
#-------------------------------------<
def exercise_tracker():
    while is_running == True:
        query = query_fn()
        weight = imperial_metric_weight()
        height = imperial_metric_height()
        age = user_age()
        #---------------------------<
        # POST: JSON PAYLOAD
        #---------------<
        exercise_data = {
            'query': query,
            'weight_kg': weight,
            'height_cm': height,
            'age': age
        }
        #---------------------------<
        # POST: JSON TO NUTRITIONIX
        #---------------<
        response = requests.post(url=nutritionix_end, json=exercise_data, headers=headers)
        print(response.text)
        nutritionix_result = response.json()
        # #---------------------------<
        # # SHEETY: NUTRTITIONIX_RESPONSE.JSON TO SHEETY_DATA.JSON
        # #---------------<
        for i in nutritionix_result['exercises']:
            sheet_data = {
                'workout': {
                    'date': date,
                    'time': time,
                    'exercise': i['name'].title(),
                    'duration': i['duration_min'],
                    'calories': i['nf_calories']
                }
            }
        # #---------------------------<
        # # POST: SHEETY_DATA TO SHEETY
        # #---------------<
        sheety_response = requests.post(sheety_end, json=sheet_data, auth=(USERNAME, PASSWORD))
        print(sheety_response.text)
        quit()
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# RUN PROGRAM
#-------------------------------------<
exercise_tracker()
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
#=========================================================<
# }
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# PROJECT: EXERCISE TRACKER USING NUTRITIONIX, SHEETY, AND GOOGLE DOCS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V2 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import os
# from dotenv import load_dotenv
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## ENVIRONMENT VARIABLES
# #-------------------------------------<
# load_dotenv('./W4/38/.env')
# USERNAME = os.getenv('SHEETY_USERNAME')
# PASSWORD = os.getenv('SHEETY_PASSWORD')
# USER_ID = os.getenv('SHEETY_USER_ID')
# PROJECT_ID = os.getenv('SHEETY_PROJECT_ID')
# SHEET_ID = os.getenv('SHEETY_SHEET_ID')
# API_KEY = os.getenv('NUTRITIONIX_API_KEY')
# API_ID = os.getenv('NUTRITIONIX_API_ID')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## GLOBAL VARIABLE
# #-------------------------------------<
# is_running = True
# date = datetime.now().strftime('%d/%m/%Y')
# time = datetime.now().strftime('%X')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: CLEAR TERMINAL
# #---------------------------<
# def clear_terminal_window():
#     if os.name =='nt':
#         os.system('cls')
#     else:
#         os.system('clear')

# def shutdown_program():
#     is_running = False
#     return is_running
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: QUERY INPUT
# #---------------------------<
# def query_fn():
#     query = input('What exercise did you do today?')
#     return query
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: WEIGHT INPUT AND CONVERSION
# #---------------------------<
# def imperial_metric_weight():
#     weight = input("How much do you weigh today?\n")
#     unit = input('Pounds or Kilograms?\n')
#     if unit.title() == 'Pounds' or unit.title() == 'Lbs':
#         weight = round(float(weight) / 2.205)
#         return weight
#     elif unit.title() == 'Kilograms' or unit.title() == 'Kilos' or unit.title() == 'Kg' or unit.title() == 'Kgs':
#         return weight
#     else:
#         continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
#         if continue_or_nah.title() != 'Y':
#             clear_terminal_window()
#             imperial_metric_weight()
#         elif continue_or_nah.title() == 'N':
#             is_running = False
#         else:
#             is_running = False
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: HEIGHT INPUT AND CONVERSION
# #---------------------------<
# def imperial_metric_height():
#     height = input("How tall are you?\n")
#     unit = input('Feet, Inches, or Meters, or Centimeters?\n')
#     if unit.title() == 'Inches' or unit.title() == 'In':
#         height = round(float(height) * 2.54)
#         return height
#     elif unit.title() == 'Feet' or unit.title() == 'Ft':
#             feet = int(height[:1])
#             inch = int(height[2:])
#             total = (feet * 12) + inch
#             height = round(float(total) * 2.54)
#             return height
#     elif unit.title() == 'Meters' or unit.title() == 'M':
#         height = round(float(height) / .01)
#     elif unit.title() == 'Centimeters' or unit.title() == 'Cm':
#         return height
#     else:
#         continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
#         if continue_or_nah.title() != 'Y':
#             clear_terminal_window()
#             imperial_metric_height()
#         elif continue_or_nah.title() == 'N':
#             is_running = False
#         else:
#             is_running = False
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: AGE
# #---------------------------<
# def user_age():
#     age = input('How old are you?\n')
#     return age
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## NUTRITIONIX
# #:::::::::::::::::::::::::::::::::::::<
# # NUTRITIONIX: URLS
# #---------------------------<
# nutritionix_end = 'https://trackapi.nutritionix.com/v2/natural/exercise'
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # NUTRITIONIX: HEADERS
# #---------------------------<
# headers = {
#     'x-app-id': API_ID,
#     'x-app-key': API_KEY
# }
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # SHEETY
# #:::::::::::::::::::::::::::::::::::::<
# # SHEETY: URLS
# #---------------------------<
# sheety_end = f'https://api.sheety.co/{USER_ID}/{PROJECT_ID}/{SHEET_ID}'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PROGRAM: FUNCTION
# #-------------------------------------<
# def exercise_tracker():
#     while is_running == True:
#         query = query_fn()
#         weight = imperial_metric_weight()
#         height = imperial_metric_height()
#         age = user_age()
#         #---------------------------<
#         # POST: JSON PAYLOAD
#         #---------------<
#         exercise_data = {
#             'query': query,
#             'weight_kg': weight,
#             'height_cm': height,
#             'age': age
#         }
#         #---------------------------<
#         # POST: JSON TO NUTRITIONIX
#         #---------------<
#         response = requests.post(url=nutritionix_end, json=exercise_data, headers=headers)
#         print(response.text)
#         nutritionix_result = response.json()
#         # #---------------------------<
#         # # SHEETY: NUTRTITIONIX_RESPONSE.JSON TO SHEETY_DATA.JSON
#         # #---------------<
#         for i in nutritionix_result['exercises']:
#             sheet_data = {
#                 'workout': {
#                     'date': date,
#                     'time': time,
#                     'exercise': i['name'].title(),
#                     'duration': i['duration_min'],
#                     'calories': i['nf_calories']
#                 }
#             }
#         # #---------------------------<
#         # # POST: SHEETY_DATA TO SHEETY
#         # #---------------<
#         sheety_response = requests.post(sheety_end, json=sheet_data, auth=(USERNAME, PASSWORD))
#         print(sheety_response.text)
#         quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # RUN PROGRAM
# #-------------------------------------<
# exercise_tracker()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V1 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import os
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# # USERNAME = 'FunKodeT'
# # TOKEN = 'Gr3nd3lk@nD0!t@77'
# SHEETY_USER = 'd681b7c7f339553787243ddb5d66c1d7'
# SHEETY_PROJECT = 'myWorkouts'
# SHEEY_SHEET = 'workouts'
# APP_ID = '77ac89a5'
# API_KEY = '65429873b882ca4651de0d8549bd0994'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## GLOBAL VARIABLE
# #-------------------------------------<
# is_running = True
# date = datetime.now().strftime('%d/%m/%Y')
# time = datetime.now().strftime('%X')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: CLEAR TERMINAL
# #---------------------------<
# def clear_terminal_window():
#     if os.name =='nt':
#         os.system('cls')
#     else:
#         os.system('clear')

# def shutdown_program():
#     is_running = False
#     return is_running
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: QUERY INPUT
# #---------------------------<
# def query_fn():
#     query = input('What exercise did you do today?')
#     return query
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: WEIGHT INPUT AND CONVERSION
# #---------------------------<
# def imperial_metric_weight():
#     weight = input("How much do you weigh today?\n")
#     unit = input('Pounds or Kilograms?\n')
#     if unit.title() == 'Pounds' or unit.title() == 'Lbs':
#         weight = round(float(weight) / 2.205)
#         return weight
#     elif unit.title() == 'Kilograms' or unit.title() == 'Kilos' or unit.title() == 'Kg' or unit.title() == 'Kgs':
#         return weight
#     else:
#         continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
#         if continue_or_nah.title() != 'Y':
#             clear_terminal_window()
#             imperial_metric_weight()
#         elif continue_or_nah.title() == 'N':
#             is_running = False
#         else:
#             is_running = False
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: HEIGHT INPUT AND CONVERSION
# #---------------------------<
# def imperial_metric_height():
#     height = input("How tall are you?\n")
#     unit = input('Feet, Inches, or Meters, or Centimeters?\n')
#     if unit.title() == 'Inches' or unit.title() == 'In':
#         height = round(float(height) * 2.54)
#         return height
#     elif unit.title() == 'Feet' or unit.title() == 'Ft':
#             feet = int(height[:1])
#             inch = int(height[2:])
#             total = (feet * 12) + inch
#             height = round(float(total) * 2.54)
#             return height
#     elif unit.title() == 'Meters' or unit.title() == 'M':
#         height = round(float(height) / .01)
#     elif unit.title() == 'Centimeters' or unit.title() == 'Cm':
#         return height
#     else:
#         continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
#         if continue_or_nah.title() != 'Y':
#             clear_terminal_window()
#             imperial_metric_height()
#         elif continue_or_nah.title() == 'N':
#             is_running = False
#         else:
#             is_running = False
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: AGE
# #---------------------------<
# def user_age():
#     age = input('How old are you?\n')
#     return age
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## NUTRITIONIX
# #:::::::::::::::::::::::::::::::::::::<
# # NUTRITIONIX: URLS
# #---------------------------<
# nutritionix_end = 'https://trackapi.nutritionix.com/v2/natural/exercise'
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # NUTRITIONIX: HEADERS
# #---------------------------<
# headers = {
#     'x-app-id': APP_ID,
#     'x-app-key': API_KEY
# }
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # SHEETY
# #:::::::::::::::::::::::::::::::::::::<
# # SHEETY: URLS
# #---------------------------<
# sheety_end = 'https://api.sheety.co/d681b7c7f339553787243ddb5d66c1d7/myWorkouts/workouts'
# # sheety_end = f'https://api.sheety.co/{SHEETY_USER}/{SHEETY_PROJECT}/{SHEEY_SHEET}'
# # GEThttps://api.sheety.co/d681b7c7f339553787243ddb5d66c1d7/myWorkouts/workouts
# # POSThttps://api.sheety.co/d681b7c7f339553787243ddb5d66c1d7/myWorkouts/workouts
# # PUThttps://api.sheety.co/d681b7c7f339553787243ddb5d66c1d7/myWorkouts/workouts/[Object ID]
# # DELETEhttps://api.sheety.co/d681b7c7f339553787243ddb5d66c1d7/myWorkouts/workouts/[Object ID]


# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PROGRAM: FUNCTION
# #-------------------------------------<
# def exercise_tracker():
#     while is_running == True:
#         query = query_fn()
#         weight = imperial_metric_weight()
#         height = imperial_metric_height()
#         age = user_age()
#         #---------------------------<
#         # POST: JSON PAYLOAD
#         #---------------<
#         exercise_data = {
#             'query': query,
#             'weight_kg': weight,
#             'height_cm': height,
#             'age': age
#         }
#         #---------------------------<
#         # POST: JSON TO NUTRITIONIX
#         #---------------<
#         response = requests.post(url=nutritionix_end, json=exercise_data, headers=headers)
#         print(response.text)
#         nutritionix_result = response.json()
#         # #---------------------------<
#         # # SHEETY: NUTRTITIONIX_RESPONSE.JSON TO SHEETY_DATA.JSON
#         # #---------------<
#         for i in nutritionix_result['exercises']:
#             sheet_data = {
#                 'workout': {
#                     'date': date,
#                     'time': time,
#                     'exercise': i['name'].title(),
#                     'duration': i['duration_min'],
#                     'calories': i['nf_calories']
#                 }
#             }
#         # #---------------------------<
#         # # POST: SHEETY_DATA TO SHEETY
#         # #---------------<
#         sheety_response = requests.post(sheety_end, json=sheet_data)
#         print(sheety_response.text)
#         quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # RUN PROGRAM
# #-------------------------------------<
# exercise_tracker()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import os
# import sys
# import itertools
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# # USERNAME = 'FunKodeT'
# # TOKEN = 'Gr3nd3lk@nD0!t@77'
# APP_ID = '77ac89a5'
# API_KEY = '65429873b882ca4651de0d8549bd0994'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## GLOBAL VARIABLE
# #-------------------------------------<
# is_running = True
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## FUNCTIONS
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: CLEAR TERMINAL
# #---------------------------<
# def clear_terminal_window():
#     if os.name =='nt':
#         os.system('cls')
#     else:
#         os.system('clear')
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: QUERY INPUT
# #---------------------------<
# def query_fn():
#     query = input('What exercise did you do today?')
#     return query
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: WEIGHT INPUT AND CONVERSION
# #---------------------------<
# def imperial_metric_weight():
#     weight = input("How much do you weigh today?\n")
#     unit = input('Pounds or Kilograms?\n')
#     if unit.title() == 'Pounds' or unit.title() == 'Lbs':
#         weight = round(float(weight) / 2.205)
#         return weight
#     elif unit.title() == 'Kilograms' or unit.title() == 'Kilos' or unit.title() == 'Kg' or unit.title() == 'Kgs':
#         return weight
#     else:
#         continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
#         if continue_or_nah.title() != 'Y':
#             clear_terminal_window()
#             imperial_metric_weight()
#         elif continue_or_nah.title() == 'N':
#             is_running = False
#         else:
#             is_running = False
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: HEIGHT INPUT AND CONVERSION
# #---------------------------<
# def imperial_metric_height():
#     height = input("How tall are you?\n")
#     unit = input('Feet, Inches, or Meters, or Centimeters?\n')
#     if unit.title() == 'Inches' or unit.title() == 'In':
#         height = round(float(height) * 2.54)
#         return height
#     elif unit.title() == 'Feet' or unit.title() == 'Ft':
#             feet = int(height[:1])
#             inch = int(height[2:])
#             total = (feet * 12) + inch
#             height = round(float(total) * 2.54)
#             return height
#     elif unit.title() == 'Meters' or unit.title() == 'M':
#         height = round(float(height) / .01)
#     elif unit.title() == 'Centimeters' or unit.title() == 'Cm':
#         return height
#     else:
#         continue_or_nah = input("Only Imperial or Metric systems are available at this time. Would you like to retry? Type 'y' to continue, 'n' to quit:\n")
#         if continue_or_nah.title() != 'Y':
#             clear_terminal_window()
#             imperial_metric_height()
#         elif continue_or_nah.title() == 'N':
#             is_running = False
#         else:
#             is_running = False
# #:::::::::::::::::::::::::::::::::::::<
# # FUNCTION: AGE
# #---------------------------<
# def user_age():
#     age = input('How old are you?\n')
#     return age
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## NUTRITIONIX
# #:::::::::::::::::::::::::::::::::::::<
# # NUTRITIONIX: URLS
# #---------------------------<
# nutritionix_end = 'https://trackapi.nutritionix.com/v2/natural'
# nutritionix_post_end = f'{nutritionix_end}/exercise/{APP_ID}/{API_KEY}'
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# # NUTRITIONIX: HEADERS
# #---------------------------<
# headers = {
#     'x-app-id': APP_ID,
#     'x-app-key': API_KEY
# }
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # FUNCTION: PROGRAM CODE
# #-------------------------------------<
# def exercise_tracker():
#     while is_running == True:
#         query = query_fn()
#         weight = imperial_metric_weight()
#         height = imperial_metric_height()
#         age = user_age()
#         #---------------------------<
#         # POST: JSON PAYLOAD
#         #---------------<
#         exercise_data = {
#             'query': query,
#             'weight_kg': weight,
#             'height_cm': height,
#             'age': age
#         }
#         #---------------------------<
#         # POST: SEND JSON
#         #---------------<
#         response = requests.post(url=nutritionix_post_end, json=exercise_data, headers=headers)
#         print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # RUN PROGRAM
# #-------------------------------------<
# exercise_tracker()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
#################################################################