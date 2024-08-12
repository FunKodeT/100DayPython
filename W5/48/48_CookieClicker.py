################################################################>
#=========================================================>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <48_CookieClicker.py>
#=========================================================<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## IMPORTS
#-------------------------------------<
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## SELENIUM
#:::::::::::::::::::::::::::::::::::::<
# SELENIUM: DRIVER IMPORT
#---------------------------<
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
#-------------------------------------<
# SELENIUM: DRIVER ALLOCATION
#---------------------------<
driver = webdriver.Chrome(options=chrome_options)
#-------------------------------------<
# SELENIUM: TARGET URL
#---------------------------<
driver.get('http://orteil.dashnet.org/experiments/cookie/')
#---------------------------<
# URL: TARGET ELEMENT VIA ID
#---------------<
cookie = driver.find_element(By.ID, value='cookie')
#---------------------------<
# URL: TARGET ELEMENTs VIA CSS
#---------------<
items = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')
item_ids = [i.get_attribute('id') for i in items]
#---------------------------<
# TARGET: TIMED LAG
#---------------<
timeout = time.time() + 5
#---------------------------<
# TARGET: TIMED ACTIVATION
#---------------<
five_min = time.time() + 60*5
#---------------------------<
# BOT RUN PATH
#---------------<
while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value='#store b')
        item_prices = []
        for p in all_prices:
            element_text = p.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)
        cookie_upgrades = {}
        for ip in range(len(item_prices)):
            cookie_upgrades[item_prices[ip]] = item_ids[ip]
        money_element = driver.find_element(by=By.ID, value='money').text
        if ',' in money_element:
            money_element = money_element.replace(',', '')
        cookie_count = int(money_element)
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        highest_price_affordabe_upgrade = max(affordable_upgrades)
        print(highest_price_affordabe_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordabe_upgrade]
        driver.find_element(by=By.ID, value=to_purchase_id).click()
        timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value='cps').text
        print(cookie_per_s)
        break
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## CODE RESULTS
#-------------------------------------<
# SUCCESS: CODE RUNS CORRECTLY
#:::::::::::::::::::::::::::::::::::::::::::::::<
#=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# SELENIUM WEBDRIVER > PSEUDO_COOKIE_CLICKER
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM4_V1>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('http://orteil.dashnet.org/experiments/cookie/')
# #---------------------------<
# # URL: TARGET ELEMENT VIA ID
# #---------------<
# cookie = driver.find_element(By.ID, value='cookie')
# #---------------------------<
# # URL: TARGET ELEMENTs VIA CSS
# #---------------<
# items = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')
# item_ids = [i.get_attribute('id') for i in items]
# #---------------------------<
# # TARGET: TIMED LAG
# #---------------<
# timeout = time.time() + 5
# #---------------------------<
# # TARGET: TIMED ACTIVATION
# #---------------<
# five_min = time.time() + 60*5
# #---------------------------<
# # BOT RUN PATH
# #---------------<
# while True:
#     cookie.click()
#     if time.time() > timeout:
#         all_prices = driver.find_elements(by=By.CSS_SELECTOR, value='#store b')
#         item_prices = []
#         for p in all_prices:
#             element_text = p.text
#             if element_text != '':
#                 cost = int(element_text.split('-')[1].strip().replace(',', ''))
#                 item_prices.append(cost)
#         cookie_upgrades = {}
#         for ip in range(len(item_prices)):
#             cookie_upgrades[item_prices[ip]] = item_ids[ip]
#         money_element = driver.find_element(by=By.ID, value='money').text
#         if ',' in money_element:
#             money_element = money_element.replace(',', '')
#         cookie_count = int(money_element)
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#         highest_price_affordabe_upgrade = max(affordable_upgrades)
#         print(highest_price_affordabe_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordabe_upgrade]
#         driver.find_element(by=By.ID, value=to_purchase_id).click()
#         timeout = time.time() + 5
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(by=By.ID, value='cps').text
#         print(cookie_per_s)
#         break
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: CODE RUNS CORRECTLY
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM4_V0>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('http://orteil.dashnet.org/experiments/cookie/')
# #---------------------------<
# # URL: TARGET ELEMENT VIA ID
# #---------------<
# cookie = driver.find_element(By.ID, value='cookie')
# #---------------------------<
# # URL: TARGET ELEMENTs VIA CSS
# #---------------<
# items = driver.find_elements(by=By.CSS_SELECTOR, value='#store div')
# item_ids = [i.get_attribute('id') for i in items]
# #---------------------------<
# # TARGET: TIMED LAG
# #---------------<
# timeout = time.time() + 5
# #---------------------------<
# # TARGET: TIMED ACTIVATION
# #---------------<
# five_min = time.time() + 60*5
# #---------------------------<
# # BOT RUN PATH
# #---------------<
# while True:
#     cookie.click()
#     if time.time() > timeout:
#         all_prices = driver.find_elements(by=By.CSS_SELECTOR, value='#store b')
#         item_prices = []
#         for p in all_prices:
#             element_text = price.text
#             if element_text != '':
#                 cost = int(element_text.split('-')[1].strip().replace(',', ''))
#                 item_prices.append(cost)
#         cookie_upgrades = {}
#         for ip in range(len(item_prices)):
#             cookie_upgrades[item_prices[ip]] = item_ids[ip]
#         money_element = driver.find_element(by=By.ID, value='money').text
#         if ',' in money_element:
#             money_element = money_element.replace(',', '')
#         cookie_count = int(money_element)
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#         highest_price_affordabe_upgrade = max(affordable_upgrades)
#         print(highest_price_affordabe_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordabe_upgrade]
#         driver.find_element(by=By.ID, value=to_purchase_id).click()
#         timeout = time.time() + 5
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(by=By.ID, value='cps').text
#         print(cookie_per_s)
#         break
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # ERROR: RUNS AT FIRST, THAN ENCOUNTERS CRASH DUE TO NAMEERROR 'price' L171
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# SELENIUM WEBDRIVER > FAKE_REGISTRATION
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM3_V1>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://secure-retreat-92358.herokuapp.com')
# #---------------------------<
# # URL: TARGET ELEMENT VIA NAME
# #---------------<
# fName = driver.find_element(By.NAME, value='fName')
# lName = driver.find_element(By.NAME, value='lName')
# email = driver.find_element(By.NAME, value='email')
# #---------------------------<
# # URL: TARGET ELEMENT VIA CSS
# #---------------<
# submit = driver.find_element(By.CSS_SELECTOR, value='form button')
# #---------------------------<
# # URL: SEND INPUT KEY VALUES TO TARGET
# #---------------<
# fName.send_keys('Matthew')
# lName.send_keys('Cootey')
# email.send_keys('cooteybug@gmail.com')
# #---------------------------<
# # URL: SEND SUBMIT VALUE TO TARGET
# #---------------<
# submit.click()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: INPUT VALUES ARE SENT, SUBMISSION IS ACTIVATED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM3_V0>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://secure-retreat-92358.herokuapp.com')
# #---------------------------<
# # URL: TARGET ELEMENT VIA NAME
# #---------------<
# fName = driver.find_element(By.NAME, value='fName')
# lName = driver.find_element(By.NAME, value='lName')
# email = driver.find_element(By.NAME, value='email')
# #---------------------------<
# # URL: TARGET ELEMENT VIA CSS
# #---------------<
# submit = driver.find_element(By.CSS_SELECTOR, value='form button')
# #---------------------------<
# # URL: SEND INPUT KEY VALUES TO TARGET
# #---------------<
# fName.send_keys('Matthew')
# lName.send_keys('Cootey')
# email.send_keys('cooteybug@gmail.com')
# #---------------------------<
# # URL: SEND SUBMIT VALUE TO TARGET
# #---------------<
# submit.click()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: INPUT VALUES ARE SENT, SUBMISSION IS ACTIVATED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# SELENIUM WEBDRIVER > WIKIPEDIA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM2_V7>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# #---------------------------<
# # URL: TARGET ELEMENT VIA NAME
# #---------------<
# search = driver.find_element(By.NAME, value='search')
# #---------------------------<
# # URL: SEND INPUT KEY VALUE AND INPUT ENTER VALUE TO TARGET
# #---------------<
# search.send_keys('Python', Keys.ENTER)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: INPUT IS SENT AND ENTER IS PRESSED THROUGH AUTOMATION VIA SELENIUM WEBDRIVER
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM2_V6>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# #---------------------------<
# # URL: TARGET ELEMENT VIA NAME
# #---------------<
# search = driver.find_element(By.NAME, value='search')
# #---------------------------<
# # URL: SEND INPUT KEY VALUE TO TARGET
# #---------------<
# search.send_keys('Python')
# #---------------------------<
# # URL: SEND INPUT KEY ENTER TO TARGET
# #---------------<
# search.send_keys(Keys.ENTER)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # WARNING: FULL FUNCTIONALITY, JUST A LINE OR TWO OF UNNECESSARY CODE
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM2_V5>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# #---------------------------<
# # URL: TARGET ELEMENT VIA NAME
# #---------------<
# search = driver.find_element(By.NAME, value='search')
# #---------------------------<
# # URL: SEND KEYS TO TARGET
# #---------------<
# search.send_keys('Python')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: TYPES VALUE AS INTENDED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM2_V4 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# #---------------------------<
# # URL: TARGET ELEMENT VIA LINK_TEXT
# #---------------<
# all_portals = driver.find_element(By.LINK_TEXT, value='Content Portals')
# #---------------------------<
# # URL: CLICK TARGET
# #---------------<
# all_portals.click()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: CLICKS VALUE AS INTENDED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM2_V3 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# #---------------------------<
# # URL: TARGET ELEMENT
# #---------------<
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# #---------------------------<
# # URL: CLICK TARGET
# #---------------<
# article_count.click()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: CLICKS VALUE AS INTENDED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM2_V2 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# #---------------------------<
# # URL: TARGET ELEMENT
# #---------------<
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# #---------------------------<
# # URL: PRINT TARGET
# #---------------<
# print(article_count.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # SUCCESS: PRINTS VALUE AS INTENDED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM2_V1 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## SELENIUM
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM: DRIVER IMPORT
# #---------------------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #-------------------------------------<
# # SELENIUM: DRIVER ALLOCATION
# #---------------------------<
# driver = webdriver.Chrome(options=chrome_options)
# #-------------------------------------<
# # SELENIUM: TARGET URL
# #---------------------------<
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# #---------------------------<
# # URL: TARGET ELEMENT
# #---------------<
# article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# #---------------------------<
# # URL: PRINT TARGET
# #---------------<
# print(article_count.text)
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## CODE RESULTS
# #-------------------------------------<
# # ERROR: SELENIUM COULD NOT RETRIEVE TARGET VALUE, 'By' IS NOT DEFINED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM2_V0 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# SELENIUM WEBDRIVER > PYTHON.ORG
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V11 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: BROWSER SETTINGS
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER TYPE
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# #---------------------------<
# # WEBDRIVER: USE URL
# #---------------<
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT BY CLASS
# #---------------------------<
# tier_1 = driver.find_elements(By.CLASS_NAME, value='tier-1')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT 1 BY CSS
# #---------------------------<
# event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT 2 BY CSS
# #---------------------------<
# event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# #:::::::::::::::::::::::::::::::::::::<
# ## RESPONSE DICTIONARY
# #:::::::::::::::::::::::::::<
# # DICTIONARY: EMPTY OBJECT
# #---------------<
# events = {}
# #---------------------------<
# # DICTIONARY: ALLOCATE RESPONSE TO OBJECT
# #---------------<
# for i in range(len(event_times)):
#     events[i] = {
#         'time': event_times[i].text,
#         'name': event_names[i].text
#     }
# #---------------------------<
# # DICTIONARY: PRINT ALLOCATION
# #---------------<
# print(events)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # NOTE: FULL FUNCTIONALITY ACHIEVED
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V10 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: BROWSER SETTINGS
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER TYPE
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# #---------------------------<
# # WEBDRIVER: USE URL
# #---------------<
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT BY CLASS
# #---------------------------<
# tier_1 = driver.find_elements(By.CLASS_NAME, value='tier-1')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT 1 BY CSS
# #---------------------------<
# event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# #---------------------------<
# # ELEMENT: PRINT CSS VALUE 1
# #---------------<
# for time in event_times:
#     print(time.text)
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT 2 BY CSS
# #---------------------------<
# event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# #---------------------------<
# # ELEMENT: PRINT CSS VALUE 2
# #---------------<
# for name in event_names:
#     print(name.text)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # NOTE: SPECIFYING FURTHER ALLOWED FOR INTENDED RESPONSE
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V9 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: BROWSER SETTINGS
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER TYPE
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# #---------------------------<
# # WEBDRIVER: USE URL
# #---------------<
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT BY CLASS
# #---------------------------<
# tier_1 = driver.find_elements(By.CLASS_NAME, value='tier-1')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT 1 BY CSS
# #---------------------------<
# event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# #---------------------------<
# # ELEMENT: PRINT CSS VALUE 1
# #---------------<
# for time in event_times:
#     print(time.text)
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT 2 BY CSS
# #---------------------------<
# event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget a')
# #---------------------------<
# # ELEMENT: PRINT CSS VALUE 2
# #---------------<
# for name in event_names:
#     print(name.text)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: RESPONSE IS ACCURACTE, HOWEVER THE FIRST DIV PROVIDES ADDITIONAL UNWANTED INFORMATION DUE TO LACK OF ACCURACY IN SPECIFICATION
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V8 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: BROWSER SETTINGS
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER TYPE
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# #---------------------------<
# # WEBDRIVER: USE URL
# #---------------<
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT BY CLASS
# #---------------------------<
# tier_1 = driver.find_elements(By.CLASS_NAME, value='tier-1')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT BY CSS
# #---------------------------<
# event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# #---------------------------<
# # ELEMENT: PRINT CSS VALUE
# #---------------<
# print(event_times)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: RESPONSE IS RECEIVED IN SELENIUM FORMATTING
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V7 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: SPECIFY BROWSER PATH
# #---------------<
# chrome_driver_path = '/Users/angela/Development/chromedriver'

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# # #---------------------------<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT BY XPATH
# #---------------------------<
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# #---------------------------<
# # ELEMENT: PRINT XPATH VALUE
# #---------------<
# print(bug_link.text)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<

# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V6 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE ELEMENT BY XPATH
# #---------------------------<
# driver.find_element(By.XPATH, value="//*[@id="site-map"]/div[2]/div/ul/li[3]/a")
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # ERROR: CANNOT FIND XPATH DUE TO QUOTATION ERRORS
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V5 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE NAME ELEMENT
# #---------------------------<
# search_bar = driver.find_element(By.NAME, value='q')
# #---------------------------<
# # ELEMENT: PRINT NAME VALUE
# #---------------<
# print(search_bar.get_attribute('placeholder'))
# #-------------------------------------<
# # SELENIUM: RETRIEVE ID ELEMENT
# #---------------------------<
# button = driver.find_element(By.ID, value='submit')
# #---------------------------<
# # ELEMENT: PRINT ID VALUE
# #---------------<
# print(button.size)
# #-------------------------------------<
# # SELENIUM: RETRIEVE CSS_SELECTOR ELEMENT
# #---------------------------<
# documentation_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# #---------------------------<
# # ELEMENT: PRINT CSS_SELECTOR VALUE
# #---------------<
# print(documentation_link.text)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # NOTE: RETURNS THE VALUE OF THE ANCHOR ELEMENT VIA CSS_SELECTORS
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V4 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE NAME ELEMENT
# #---------------------------<
# search_bar = driver.find_element(By.NAME, value='q')
# #---------------------------<
# # ELEMENT: PRINT RESULT
# #---------------<
# print(search_bar.get_attribute('placeholder'))
# #-------------------------------------<
# # SELENIUM: RETRIEVE ID ELEMENT
# #---------------------------<
# button = driver.find_element(By.ID, value='submit')
# #---------------------------<
# # ELEMENT: PRINT RESULT
# #---------------<
# print(button.size)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # NOTE: RETURNS THE VALUE OF THE BUTTON ID>CSS BUTTON SIZE
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V3 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE NAME ELEMENT
# #---------------------------<
# search_bar = driver.find_element(By.NAME, value='q')
# #---------------------------<
# # ELEMENT: PRINT RESULT
# #---------------<
# print(search_bar.get_attribute('placeholder'))
# #-------------------------------------<
# # SELENIUM: RETRIEVE ID ELEMENT
# #---------------------------<
# button = driver.find_element(By.ID, value='submit')
# #---------------------------<
# # ELEMENT: PRINT RESULT
# #---------------<
# print(button)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: RETURNS THE VALUE OF THE BUTTON ID SPECIFIED IN SELENIUM ELEMENT FORMAT
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V2 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE Q ELEMENTS
# #---------------------------<
# search_bar = driver.find_element(By.NAME, value='q')
# #-------------------------------------<
# # ELEMENT: PRINT RESULT
# #---------------------------<
# print(search_bar.get_attribute('placeholder'))
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: RETURNS TO USER THE VALUE OF 'Search' AS THAT IS THE VALUE OF THE TARGETED CLASS>TARGETED ELEMENT>TARGETED ATTRIBUTE>ATTRIBUTE VALUE
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V1 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE Q ELEMENTS
# #---------------------------<
# search_bar = driver.find_element(By.NAME, value='q')
# #-------------------------------------<
# # ELEMENT: PRINT RESULT
# #---------------------------<
# print(search_bar.tag_name)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: RETURNS TO USER THE VALUE OF 'input' AS THAT IS THE VALUE OF THE TARGETED ELEMENT WITHIN THE SPECIFIED WEBPAGE
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM1_V0 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.python.org/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE Q ELEMENTS
# #---------------------------<
# search_bar = driver.find_element(By.NAME, value='q')
# #-------------------------------------<
# # ELEMENT: PRINT RESULT
# #---------------------------<
# print(search_bar)
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# # driver.close()
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: RESULTS IN SELENIUM ELEMENT RETURN, FUNCTIONAL BUT NOT MEANT TO BE READ BY HUMANS
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>
#=========================================================>
# SELENIUM WEBDRIVER > AMAZON
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V5 = {
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://appbrewery.github.io/instant_pot/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE SPECIFIED ELEMENTS
# #---------------------------<
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# #---------------------------<
# # ELEMENTS: PRINT VALUES
# #---------------<
# print(f'The price is {price_dollar.text}.{price_cents.text}')
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# # driver.close()
# driver.quit()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # SUCCESS: CURRENT FUNCTIONALITY ALMOST ENTIRELY DOES THE SAME THING AS PREVIOUS PROJECT: 47_Amazon_PriceChange_Notify.py
# # NOTE: THE BENEFIT OF USING SELENIUM VS BEAUTIFULSOUP IS TWOFOLD. ONE SIDE OF THE COIN IS SIMPLER, FASTER, EASIER, AND MORE EFFICIENT CODE. THE SECOND SIDE OF THE COIN IS THE REQUEST IS BEING SENT IN A FASHION THAT REPRESENTS AN ACTUAL USER, RESULTING IN NO CAPTCHA ISSUES AND THE RESPONDING URL BELIEVING THE PROGRAM TO FUNCTIONALLY ACTUALLY BE A USER INSTEAD OF A BOT.
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
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://appbrewery.github.io/instant_pot/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE SPECIFIED ELEMENTS
# #---------------------------<
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# #---------------------------<
# # ELEMENTS: PRINT VALUES
# #---------------<
# print(f'The price is {price_dollar.text}.{price_cents.text}')
# #-------------------------------------<
# # SELENIUM: WEBDRIVER END STATE
# #---------------------------<
# driver.close()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: FUNCTIONALITY ACCOMPLISHED, HOWEVER A NEW INSTANCE OF CHROME WILL BE LAUNCHED WITH EVERY PROGRAM START DUE TO driver.close() FUNCTION
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
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://appbrewery.github.io/instant_pot/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE SPECIFIED ELEMENTS
# #---------------------------<
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# #---------------------------<
# # ELEMENTS: PRINT VALUES
# #---------------<
# print(f'The price is {price_dollar}.{price_cents}')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: RETURNS VALUE, HOWEVER RETURNS VALUE OF ENTIRE HTML CODE RATHER THAN HTML TEXT VALUE
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
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: KEEP BROWSER OPEN
# #---------------<
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('detach', True)
# #:::::::::::::::::::::::::::<
# # SELENIUM: WEBDRIVER SETTINGS
# #---------------<
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://appbrewery.github.io/instant_pot/')
# #-------------------------------------<
# # SELENIUM: RETRIEVE SPECIFIED ELEMENTS
# #---------------------------<
# price_dollar = driver.find_element(By.CLASS_NAME, value='aok-offscreen')
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # WARNING: NOT INSTRUCTOR INTENDED METHOD
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
# from selenium import webdriver
# #:::::::::::::::::::::::::::::::::::::<
# # SELENIUM
# #:::::::::::::::::::::::::::<
# # SELENIUM: DRIVER BROWSER SPECIFICATION
# #---------------<
# driver = webdriver.Chrome()
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# # CODE RESULTS
# #-------------------------------------<
# # ERROR: Chrome() DOES NOT EXIST.
# # NOTE: THE SOLUTION WAS RESTARTING VSCODE, IT HADN'T FULLY INTEGRATED THE NEW MODULE INSTALLATION
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
PROGRAM0_V0 = {
#=========================================================<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## IMPORTS
#-------------------------------------<
# import selenium
#:::::::::::::::::::::::::::::::::::::::::::::::<
#=========================================================<
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
#################################################################