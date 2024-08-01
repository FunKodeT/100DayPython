################################################################>
#=========================================================>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# 37_HabitTracker = {
#=========================================================<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## IMPORTS
#-------------------------------------<
import requests
from datetime import datetime
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## CONSTANTS
#-------------------------------------<
USERNAME = 'funkodet'
TOKEN = 'ItsAMeFunKodeT'
GRAPH_ID = 'graph1'
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# PIXELA
#:::::::::::::::::::::::::::::::::::::<
# PIXELA: URL
#---------------------------<
pixela_end = 'https://pixe.la/v1/users'
#-------------------------------------<
# PIXELA: ACCOUNT INFORMATIOIN
#---------------------------<
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
#-------------------------------------<
# PIXELA: POST ACCOUNT INFORMATION REQUEST
#---------------------------<
# response = requests.post(url=pixela_end, json=user_params)
#-------------------------------------<
# PIXELA: PRINT RESPONSE
#---------------------------<
# print(response.text)
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# GRAPH
#:::::::::::::::::::::::::::::::::::::<
# GRAPH: URL
#---------------------------<
graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
#-------------------------------------<
# GRAPH: SETTINGS
#---------------------------<
graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Miles',
    'type': 'int',
    'color': 'shibafu'
}
#-------------------------------------<
# GRAPH: HEADERS VARIABLE
#---------------------------<
headers = {
    'X-USER-TOKEN': TOKEN
}
#-------------------------------------<
# GRAPH: CREATE GRAPH
#---------------------------<
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#:::::::::::::::::::::::::::::::::::::<
# METHOD: POST
#---------------------------<
# POST: URL
#---------------<
pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
#---------------------------<
# POST: SPECIFY DATE AND TIME
#---------------<
today = datetime.now()
#---------------------------<
# POST: ALLOCATE DATA
#---------------<
pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many miles did you ride? '),
}
#---------------------------<
# POST: SEND REQUEST
#---------------<
# response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# print(response.text)
#:::::::::::::::::::::::::::::::::::::<
# METHOD: PUT
#---------------------------<
# PUT: URL
#---------------<
update_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#---------------------------<
# PUT: ALLOCATE DATA
#---------------<
new_data = {
    'quantity': '2',
}
#---------------------------<
# PUT: SEND REQUEST
#---------------<
# response = requests.put(url=update_end, json=new_data, headers=headers)
# print(response.text)
#:::::::::::::::::::::::::::::::::::::<
# METHOD: DELETE
#---------------------------<
# DELETE: URL
#---------------<
delete_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#---------------------------<
# DELETE: SEND REQUEST
#---------------<
response = requests.delete(url=delete_end, headers=headers)
print(response.text)
#:::::::::::::::::::::::::::::::::::::::::::::::<
#=========================================================<
# }
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# PROJECT: HABIT TRACKER
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V10 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# GRAPH_ID = 'graph1'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'int',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: POST
# #---------------------------<
# # POST: URL
# #---------------<
# pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
# #---------------------------<
# # POST: SPECIFY DATE AND TIME
# #---------------<
# today = datetime.now()
# #---------------------------<
# # POST: ALLOCATE DATA
# #---------------<
# pixel_data = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': input('How many miles did you ride? '),
# }
# #---------------------------<
# # POST: SEND REQUEST
# #---------------<
# # response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: PUT
# #---------------------------<
# # PUT: URL
# #---------------<
# update_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# #---------------------------<
# # PUT: ALLOCATE DATA
# #---------------<
# new_data = {
#     'quantity': '2',
# }
# #---------------------------<
# # PUT: SEND REQUEST
# #---------------<
# # response = requests.put(url=update_end, json=new_data, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: DELETE
# #---------------------------<
# # DELETE: URL
# #---------------<
# delete_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# #---------------------------<
# # DELETE: SEND REQUEST
# #---------------<
# response = requests.delete(url=delete_end, headers=headers)
# print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V9 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# GRAPH_ID = 'graph1'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'int',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: POST
# #---------------------------<
# # POST: URL
# #---------------<
# pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
# #---------------------------<
# # POST: SPECIFY DATE AND TIME
# #---------------<
# today = datetime(year=2024, month=7, day=23)
# #---------------------------<
# # POST: ALLOCATE DATA
# #---------------<
# pixel_data = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '5',
# }
# #---------------------------<
# # POST: SEND REQUEST
# #---------------<
# # response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: PUT
# #---------------------------<
# # PUT: URL
# #---------------<
# update_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# #---------------------------<
# # PUT: ALLOCATE DATA
# #---------------<
# new_data = {
#     'quantity': '2',
# }
# #---------------------------<
# # PUT: SEND REQUEST
# #---------------<
# # response = requests.put(url=update_end, json=new_data, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: DELETE
# #---------------------------<
# # DELETE: URL
# #---------------<
# delete_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# #---------------------------<
# # DELETE: SEND REQUEST
# #---------------<
# response = requests.delete(url=delete_end, headers=headers)
# print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V8 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# GRAPH_ID = 'graph1'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'int',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: POST
# #---------------------------<
# # POST: URL
# #---------------<
# pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
# #---------------------------<
# # POST: SPECIFY DATE AND TIME
# #---------------<
# today = datetime(year=2024, month=7, day=23)
# #---------------------------<
# # POST: ALLOCATE DATA
# #---------------<
# pixel_data = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '5',
# }
# #---------------------------<
# # POST: SEND REQUEST
# #---------------<
# # response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # METHOD: PUT
# #---------------------------<
# # PUT: URL
# #---------------<
# update_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# #---------------------------<
# # PUT: ALLOCATE DATA
# #---------------<
# new_data = {
#     'quantity': '2',
# }
# #---------------------------<
# # PUT: SEND REQUEST
# #---------------<
# response = requests.put(url=update_end, json=new_data, headers=headers)
# print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V7 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# GRAPH_ID = 'graph1'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'int',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH METHOD: POST
# #---------------------------<
# # POST: URL
# #---------------<
# pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
# #---------------------------<
# # POST: SPECIFY DATE AND TIME
# #---------------<
# today = datetime(year=2024, month=7, day=23)
# #---------------------------<
# # POST: ALLOCATE DATA
# #---------------<
# pixel_data = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '5',
# }
# #---------------------------<
# # POST: POST REQUEST
# #---------------<
# response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V6 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# GRAPH_ID = 'graph1'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'int',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH DATA ALLOCATION
# #---------------------------<
# # ALLOCATE: URL VARIABLE
# #---------------<
# pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
# #---------------------------<
# # ALLOCATE: DATE AND TIME
# #---------------<
# today = datetime.now()
# print(today.strftime('%Y%m%d'))
# #---------------------------<
# # ALLOCATE: PIXEL DATA
# #---------------<
# pixel_data = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '5',
# }
# #---------------------------<
# # ALLOCATE: POST PIXEL REQUEST
# #---------------<
# # response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V5 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# from datetime import datetime
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# GRAPH_ID = 'graph1'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'int',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH DATA ALLOCATION
# #---------------------------<
# # ALLOCATE: URL VARIABLE
# #---------------<
# pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
# #---------------------------<
# # ALLOCATE: DATE AND TIME
# #---------------<
# today = datetime.now()
# print(today)
# #---------------------------<
# # ALLOCATE: PIXEL DATA
# #---------------<
# pixel_data = {
#     'date': today.strftime('%Y%m%d'),
#     'quantity': '5',
# }
# #---------------------------<
# # ALLOCATE: POST PIXEL REQUEST
# #---------------<
# # response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V4 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# GRAPH_ID = 'graph1'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'int',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text)
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH DATA ALLOCATION
# #---------------------------<
# # ALLOCATE: URL VARIABLE
# #---------------<
# pixel_create_end = f'{pixela_end}/{USERNAME}/graphs/{GRAPH_ID}'
# #---------------------------<
# # ALLOCATE: PIXEL DATA
# #---------------<
# pixel_data = {
#     'date': '20240731',
#     'quantity': '5',
# }
# #---------------------------<
# # ALLOCATE: POST PIXEL REQUEST
# #---------------<
# response = requests.post(url=pixel_create_end, json=pixel_data, headers=headers)
# print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V3 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': 'graph1',
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'float',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: HEADERS VARIABLE
# #---------------------------<
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
# #-------------------------------------<
# # GRAPH: CREATE GRAPH
# #---------------------------<
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V2 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CONSTANTS
# #-------------------------------------<
# USERNAME = 'funkodet'
# TOKEN = 'ItsAMeFunKodeT'
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: POST ACCOUNT INFORMATION REQUEST
# #---------------------------<
# # response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# # print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # GRAPH
# #:::::::::::::::::::::::::::::::::::::<
# # GRAPH: URL
# #---------------------------<
# graph_endpoint = f'{pixela_end}/{USERNAME}/graphs'
# #-------------------------------------<
# # GRAPH: SETTINGS
# #---------------------------<
# graph_config = {
#     'id': 'graph1',
#     'name': 'Cycling Graph',
#     'unit': 'Miles',
#     'type': 'float',
#     'color': 'shibafu'
# }
# #-------------------------------------<
# # GRAPH: POST REQUEST
# #---------------------------<
# response = requests.post(url=graph_endpoint, json=graph_config)
# print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # ERROR: TOKEN HAS NOT BEEN PROVIDED FOR AUTHENTICATION WITH THE SERVER
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V1 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': 'ItsAMeFunKodeT',
#     'username': 'funkodet',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: REQUEST RESPONSE
# #---------------------------<
# response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# print(response.text)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# import requests
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # PIXELA
# #:::::::::::::::::::::::::::::::::::::<
# # PIXELA: URL
# #---------------------------<
# pixela_end = 'https://pixe.la/v1/users'
# #-------------------------------------<
# # PIXELA: ACCOUNT INFORMATIOIN
# #---------------------------<
# user_params = {
#     'token': 'ItsAMeFunKodeT',
#     'username': 'FunKodeT',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# #-------------------------------------<
# # PIXELA: REQUEST RESPONSE
# #---------------------------<
# response = requests.post(url=pixela_end, json=user_params)
# #-------------------------------------<
# # PIXELA: PRINT RESPONSE
# #---------------------------<
# print(response.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #---------------------------<
# # ERROR: INCORRECT USERNAME SYNTAX
# #:::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
#################################################################