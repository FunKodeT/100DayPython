################################################################>
#=========================================================>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# AMAZON_PRICECHANGE_NOTIFY = {
#=========================================================/
#:::::::::::::::::::::::::::::::::::::::::::::::/
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## IMPORTS
#-------------------------------------<
from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
#:::::::::::::::::::::::::::::::::::::<
# IMPORTS: LOAD ENV
#:::::::::::::::::::::::::::<
load_dotenv()
#:::::::::::::::::::::::::::::::::::::<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## URL
#:::::::::::::::::::::::::::::::::::::<
# URL: PAGES
#:::::::::::::::::::::::::::<
fake_url = 'https://appbrewery.github.io/instant_pot/'
real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
#:::::::::::::::::::::::::::<
## CONVERTER
#:::::::::::::::<
# CONVERTER: VARIABLES
#----------<
fake = True
# fake = False
#---------------<
# CONVERTER: FUNCTION
#----------<
def url_convert():
    if fake == True:
        url = fake_url
        return url
    else:
        url = real_url
        return url
#---------------<
# CONVERTER: FUNCTION VALUE
#----------<
# print(url_convert())
#:::::::::::::::::::::::::::::::::::::<
# URL: HEADERS DICTIONARY
#---------------<
headers = {
    'Accept-Language':'en-US,en;q=0.9',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}
#:::::::::::::::::::::::::::::::::::::<
# URL: RESPONSE ALLOCATION
#---------------<
response = requests.get(url_convert(), headers=headers)
#:::::::::::::::::::::::::::<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## BEAUTIFUL SOUP
#:::::::::::::::::::::::::::::::::::::<
# SOUP: GET REQUEST
#---------------------------<
soup = BeautifulSoup(response.content, 'html.parser')
#-------------------------------------<
# SOUP: PRINT RESPONSE
#---------------------------<
print(soup.prettify())
#-------------------------------------<
# SOUP: GET REQUEST PRICE
#---------------------------<
symbol_price = soup.find(class_='aok-offscreen').get_text()
#-------------------------------------<
# SOUP: CLEAN PRICE RESULT
#---------------------------<
int_price = symbol_price.split('$')[1]
dec_price = float(int_price)
#-------------------------------------<
# SOUP: PRINT CLEAN RESULT
#---------------------------<
print(dec_price)
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## EMAIL
#:::::::::::::::::::::::::::::::::::::<
# EMAIL: VARIABLE
#---------------------------<
title = soup.find(id='productTitle').get_text().strip()
#-------------------------------------<
# VARIABLE: PRINT
#---------------------------<
print(title)
#-------------------------------------<
# EMAIL: SET NOTIFICATION VALUE
#---------------------------<
BUY_PRICE = 100
#-------------------------------------<
# EMAIL: NOTIFICATION LOGIC
#---------------------------<
if dec_price < BUY_PRICE:
    message = f"{title} is on sale for {symbol_price}!"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PYTHON_PASSKEY'])
        connection.sendmail(
            from_addr=os.environ['EMAIL_ADDRESS'],
            to_addrs=os.environ['EMAIL_ADDRESS'],
            msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
        )
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: SOME REQUESTS RECEIVE CAPTCHA (INVALIDATING REQUEST) OR SUCCEED BUT DO NOT SEND EMAIL
#:::::::::::::::::::::::::::::::::::::::::::::::\
# =========================================================\
# }
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# SECTION DESCRIPTION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import os
# from dotenv import load_dotenv
# #:::::::::::::::::::::::::::::::::::::<
# # IMPORTS: LOAD ENV
# #:::::::::::::::::::::::::::<
# load_dotenv()
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::<
# ## CONVERTER
# #:::::::::::::::<
# # CONVERTER: VARIABLES
# #----------<
# # fake = True
# fake = False
# #---------------<
# # CONVERTER: FUNCTION
# #----------<
# def url_convert():
#     if fake == True:
#         url = fake_url
#         return url
#     else:
#         url = real_url
#         return url
# #---------------<
# # CONVERTER: FUNCTION VALUE
# #----------<
# # print(url_convert())
# #:::::::::::::::::::::::::::::::::::::<
# # URL: HEADERS DICTIONARY
# #---------------<
# headers = {
#     'Accept-Language':'en-US',
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
# #:::::::::::::::::::::::::::::::::::::<
# # URL: RESPONSE ALLOCATION
# #---------------<
# response = requests.get(url_convert(), headers=headers)
# #:::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: PRINT RESPONSE
# #---------------------------<
# print(soup.prettify())
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='aok-offscreen').get_text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## EMAIL
# #:::::::::::::::::::::::::::::::::::::<
# # EMAIL: VARIABLE
# #---------------------------<
# title = soup.find(id='productTitle').get_text().strip()
# #-------------------------------------<
# # VARIABLE: PRINT
# #---------------------------<
# print(title)
# #-------------------------------------<
# # EMAIL: SET NOTIFICATION VALUE
# #---------------------------<
# BUY_PRICE = 98
# #-------------------------------------<
# # EMAIL: NOTIFICATION LOGIC
# #---------------------------<
# if dec_price < BUY_PRICE:
#     message = f"{title} is on sale for {symbol_price}!"
#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PYTHON_PASSKEY'])
#         connection.sendmail(
#             from_addr=os.environ['EMAIL_ADDRESS'],
#             to_addrs=os.environ['EMAIL_ADDRESS'],
#             msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
#         )
# # #_______________________________________________/
# # #:::::::::::::::::::::::::::::::::::::::::::::::\
# # ## CODE RESULTS
# # #-------------------------------------<
# # # ERROR: AMAZON SENT A CAPTCHA REQUEST, INVALIDATING REQUEST
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # =========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import os
# from dotenv import load_dotenv
# #:::::::::::::::::::::::::::::::::::::<
# # IMPORTS: LOAD ENV
# #:::::::::::::::::::::::::::<
# load_dotenv()
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::<
# ## CONVERTER
# #:::::::::::::::<
# # CONVERTER: VARIABLES
# #----------<
# # fake = True
# fake = False
# #---------------<
# # CONVERTER: FUNCTION
# #----------<
# def url_convert():
#     if fake == True:
#         url = fake_url
#         return url
#     else:
#         url = real_url
#         return url
# #---------------<
# # CONVERTER: FUNCTION VALUE
# #----------<
# # print(url_convert())
# #:::::::::::::::::::::::::::::::::::::<
# # URL: HEADERS DICTIONARY
# #---------------<
# headers = {
#     'Accept-Language':'en-US',
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
# #:::::::::::::::::::::::::::::::::::::<
# # URL: RESPONSE ALLOCATION
# #---------------<
# response = requests.get(url_convert(), headers=headers)
# #:::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='aok-offscreen').get_text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## EMAIL
# #:::::::::::::::::::::::::::::::::::::<
# # EMAIL: VARIABLE
# #---------------------------<
# title = soup.find(id='productTitle').get_text().strip()
# #-------------------------------------<
# # VARIABLE: PRINT
# #---------------------------<
# print(title)
# #-------------------------------------<
# # EMAIL: SET NOTIFICATION VALUE
# #---------------------------<
# BUY_PRICE = 98
# #-------------------------------------<
# # EMAIL: NOTIFICATION LOGIC
# #---------------------------<
# if dec_price < BUY_PRICE:
#     message = f"{title} is on sale for {symbol_price}!"
#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PYTHON_PASSKEY'])
#         connection.sendmail(
#             from_addr=os.environ['EMAIL_ADDRESS'],
#             to_addrs=os.environ['EMAIL_ADDRESS'],
#             msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
#         )
# # #_______________________________________________/
# # #:::::::::::::::::::::::::::::::::::::::::::::::\
# # ## CODE RESULTS
# # #-------------------------------------<
# # # WARNING: NO ERROR, BUT NO EMAIL IS SENT TO NOTIFY
# # # NOTE: I BELIEVE THIS ISSUE IS BEING CAUSED BY SCHOOL INTERNET CONNECTION VIA WIFI
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # =========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import os
# from dotenv import load_dotenv
# #:::::::::::::::::::::::::::::::::::::<
# # IMPORTS: LOAD ENV
# #:::::::::::::::::::::::::::<
# load_dotenv()
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::<
# ## CONVERTER
# #:::::::::::::::<
# # CONVERTER: VARIABLES
# #----------<
# fake = True
# # fake = False
# #---------------<
# # CONVERTER: FUNCTION
# #----------<
# def url_convert():
#     if fake == True:
#         url = fake_url
#         return url
#     else:
#         url = real_url
#         return url
# #---------------<
# # CONVERTER: FUNCTION VALUE
# #----------<
# # print(url_convert())
# #:::::::::::::::::::::::::::::::::::::<
# # URL: HEADERS DICTIONARY
# #---------------<
# headers = {
#     'Accept-Language':'en-US',
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
# #:::::::::::::::::::::::::::::::::::::<
# # URL: RESPONSE ALLOCATION
# #---------------<
# response = requests.get(url_convert(), headers=headers)
# #:::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='a-offscreen').get_text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## EMAIL
# #:::::::::::::::::::::::::::::::::::::<
# # EMAIL: VARIABLE
# #---------------------------<
# title = soup.find(id='productTitle').get_text().strip()
# #-------------------------------------<
# # VARIABLE: PRINT
# #---------------------------<
# print(title)
# #-------------------------------------<
# # EMAIL: SET NOTIFICATION VALUE
# #---------------------------<
# BUY_PRICE = 70
# #-------------------------------------<
# # EMAIL: NOTIFICATION LOGIC
# #---------------------------<
# if dec_price < BUY_PRICE:
#     message = f"{title} is on sale for {symbol_price}!"
#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PYTHON_PASSKEY'])
#         connection.sendmail(
#             from_addr=os.environ['EMAIL_ADDRESS'],
#             to_addrs=os.environ['EMAIL_ADDRESS'],
#             msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
#         )
# # #_______________________________________________/
# # #:::::::::::::::::::::::::::::::::::::::::::::::\
# # ## CODE RESULTS
# # #-------------------------------------<
# # # WARNING: NO ERROR, HOWEVER NO RESULTS ARE POPULATED EITHER
# # # ERROR: IF BUY_PRICE IS MODIFED TO 100, CONNECTION IS REFUSED
# # # NOTE: I BELIEVE THIS ISSUE IS BEING CAUSED BY SCHOOL INTERNET CONNECTION VIA WIFI
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # =========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import os
# from dotenv import load_dotenv
# #:::::::::::::::::::::::::::::::::::::<
# # IMPORTS: LOAD ENV
# #:::::::::::::::::::::::::::<
# load_dotenv()
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::<
# ## CONVERTER
# #:::::::::::::::<
# # CONVERTER: VARIABLES
# #----------<
# fake = True
# # fake = False
# #---------------<
# # CONVERTER: FUNCTION
# #----------<
# def url_convert():
#     if fake == True:
#         url = fake_url
#         return url
#     else:
#         url = real_url
#         return url
# #---------------<
# # CONVERTER: FUNCTION VALUE
# #----------<
# # print(url_convert())
# #:::::::::::::::::::::::::::::::::::::<
# # URL: HEADERS DICTIONARY
# #---------------<
# headers = {
#     'Accept-Language':'en-US',
#     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
# }
# #:::::::::::::::::::::::::::::::::::::<
# # URL: RESPONSE ALLOCATION
# #---------------<
# response = requests.get(url_convert(), headers='{Accept-Language':'en-US', 'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"})
# #:::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='a-offscreen').get_text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## EMAIL
# #:::::::::::::::::::::::::::::::::::::<
# # EMAIL: VARIABLE
# #---------------------------<
# title = soup.find(id='productTitle').get_text().strip()
# #-------------------------------------<
# # VARIABLE: PRINT
# #---------------------------<
# print(title)
# #-------------------------------------<
# # EMAIL: SET NOTIFICATION VALUE
# #---------------------------<
# BUY_PRICE = 100
# #-------------------------------------<
# # EMAIL: NOTIFICATION LOGIC
# #---------------------------<
# if dec_price < BUY_PRICE:
#     message = f"{title} is on sale for {symbol_price}!"
#     with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#         connection.starttls()
#         result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PYTHON_PASSKEY'])
#         connection.sendmail(
#             from_addr=os.environ['EMAIL_ADDRESS'],
#             to_addrs=os.environ['EMAIL_ADDRESS'],
#             msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
#         )
# # #_______________________________________________/
# # #:::::::::::::::::::::::::::::::::::::::::::::::\
# # ## CODE RESULTS
# # #-------------------------------------<
# # # ERROR: CONNECTION REFUSED BY TARGET MACHINE (WinError 10061)
# # # NOTE: I BELIEVE THIS ISSUE IS BEING CAUSED BY SCHOOL INTERNET CONNECTION VIA WIFI
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # =========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import os
# from dotenv import load_dotenv
# #:::::::::::::::::::::::::::::::::::::<
# # IMPORTS: LOAD ENV
# #:::::::::::::::::::::::::::<
# load_dotenv()
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::<
# ## CONVERTER
# #:::::::::::::::<
# # CONVERTER: VARIABLES
# #----------<
# fake = True
# # fake = False
# #---------------<
# # CONVERTER: FUNCTION
# #----------<
# def url_convert():
#     if fake == True:
#         url = fake_url
#         return url
#     else:
#         url = real_url
#         return url
# #---------------<
# # CONVERTER: FUNCTION VALUE
# #----------<
# # print(url_convert())
# #:::::::::::::::::::::::::::::::::::::<
# # URL: RESPONSE ALLOCATION
# #---------------<
# response = requests.get(url_convert())
# #:::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='a-offscreen').get_text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## EMAIL
# #:::::::::::::::::::::::::::::::::::::<
# # EMAIL: VARIABLE
# #---------------------------<
# title = soup.find(id='productTitle').get_text().strip()
# #-------------------------------------<
# # VARIABLE: PRINT
# #---------------------------<
# print(title)
# #-------------------------------------<
# # EMAIL: SET NOTIFICATION VALUE
# #---------------------------<
# BUY_PRICE = 100
# #-------------------------------------<
# # EMAIL: NOTIFICATION LOGIC
# #---------------------------<
# if dec_price < BUY_PRICE:
#     message = f"{title} is on sale for {symbol_price}!"
#     with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
#         connection.starttls()
#         result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PYTHON_PASSKEY'])
#         connection.sendmail(
#             from_addr=os.environ['EMAIL_ADDRESS'],
#             to_addrs=os.environ['EMAIL_ADDRESS'],
#             msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
#         )
# # #_______________________________________________/
# # #:::::::::::::::::::::::::::::::::::::::::::::::\
# # ## CODE RESULTS
# # #-------------------------------------<
# # # ERROR: CONNECTION REFUSED BY TARGET MACHINE
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# #=========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# import os
# from dotenv import load_dotenv
# #:::::::::::::::::::::::::::::::::::::<
# # IMPORTS: LOAD ENV
# #:::::::::::::::::::::::::::<
# load_dotenv()
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::<
# ## CONVERTER
# #:::::::::::::::<
# # CONVERTER: VARIABLES
# #----------<
# fake = True
# # fake = False
# #---------------<
# # CONVERTER: FUNCTION
# #----------<
# def url_convert():
#     if fake == True:
#         url = fake_url
#         return url
#     else:
#         url = real_url
#         return url
# #---------------<
# # CONVERTER: FUNCTION VALUE
# #----------<
# # print(url_convert())
# #:::::::::::::::::::::::::::::::::::::<
# # URL: RESPONSE ALLOCATION
# #---------------<
# response = requests.get(url_convert())
# #:::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='a-offscreen').get_text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## EMAIL
# #:::::::::::::::::::::::::::::::::::::<
# # EMAIL: VARIABLE
# #---------------------------<
# title = soup.find(id='productTitle').get_text().strip()
# #-------------------------------------<
# # VARIABLE: PRINT
# #---------------------------<
# print(title)
# #-------------------------------------<
# # EMAIL: SET NOTIFICATION VALUE
# #---------------------------<
# BUY_PRICE = 100
# #-------------------------------------<
# # EMAIL: NOTIFICATION LOGIC
# #---------------------------<
# if dec_price < BUY_PRICE:
#     message = f"{title} is on sale for {symbol_price}!"
#     with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
#         connection.starttls()
#         result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
#         connection.sendmail(
#             from_addr=os.environ['EMAIL_ADDRESS'],
#             to_addrs=os.environ['EMAIL_ADDRESS'],
#             msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
#         )
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # ERROR: KEYERROR RELATED TO SMTP_ADDRESS
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# #=========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# import smtplib
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::<
# ## CONVERTER
# #:::::::::::::::<
# # CONVERTER: VARIABLES
# #----------<
# fake = True
# # fake = False
# #---------------<
# # CONVERTER: FUNCTION
# #----------<
# def url_convert():
#     if fake == True:
#         url = fake_url
#         return url
#     else:
#         url = real_url
#         return url
# #---------------<
# # CONVERTER: FUNCTION VALUE
# #----------<
# # print(url_convert())
# #:::::::::::::::::::::::::::::::::::::<
# # URL: RESPONSE ALLOCATION
# #---------------<
# response = requests.get(url_convert())
# #:::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='a-offscreen').get_text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## EMAIL
# #:::::::::::::::::::::::::::::::::::::<
# # EMAIL: VARIABLE
# #---------------------------<
# title = soup.find(id='productTitle').get_text().strip()
# #-------------------------------------<
# # VARIABLE: PRINT
# #---------------------------<
# print(title)
# #-------------------------------------<
# # EMAIL: SET NOTIFICATION VALUE
# #---------------------------<
# BUY_PRICE = 100
# #-------------------------------------<
# # EMAIL: NOTIFICATION LOGIC
# #---------------------------<
# if dec_price < BUY_PRICE:
#     message = f"{title} is on sale for {symbol_price}!"
#     with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
#         connection.starttls()
#         result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
#         connection.sendmail(
#             from_addr=YOUR_EMAIL,
#             to_addrs=YOUR_EMAIL,
#             msg=f"Subject: Amazon Price Alert\n\n{message}\n{url_convert()}".encode('utf-8')
#         )
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# #=========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
# #=========================================================/
# #:::::::::::::::::::::::::::::::::::::::::::::::/
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from bs4 import BeautifulSoup
# import requests
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## URL
# #:::::::::::::::::::::::::::::::::::::<
# # URL: PAGES
# #:::::::::::::::::::::::::::<
# fake_url = 'https://appbrewery.github.io/instant_pot/'
# real_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# #:::::::::::::::::::::::::::::::::::::<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BEAUTIFUL SOUP
# #:::::::::::::::::::::::::::::::::::::<
# # SOUP: GET REQUEST
# #---------------------------<
# soup = BeautifulSoup(response.content, 'html.parser')
# #-------------------------------------<
# # SOUP: GET REQUEST PRICE
# #---------------------------<
# symbol_price = soup.find(class_='a-offscreen').get.text()
# #-------------------------------------<
# # SOUP: CLEAN PRICE RESULT
# #---------------------------<
# int_price = symbol_price.split('$')[1]
# dec_price = float(int_price)
# #-------------------------------------<
# # SOUP: PRINT CLEAN RESULT
# #---------------------------<
# print(dec_price)
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# #=========================================================\
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
#################################################################











