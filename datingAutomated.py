from selenium import webdriver
from time import sleep
import pyautogui as pag
# Using Firefox to access web 

driver = webdriver.Firefox()
driver.get('https://www.okcupid.com/login')

# Wait for login prompt to generate.
sleep(2)

emailBox = driver.find_element_by_id('username')

#Enter your email
emailBox.send_keys('example@gmail.com')

passBox = driver.find_element_by_id('password')

#Enter your password
passBox.send_keys('examplePassword')

loginButton = driver.find_element_by_class_name('login-actions-button')
loginButton.click()

sleep(3)

pag.moveTo(1147, 520)

while True:
    print('like!')
    pag.press('1')
    sleep(2)
#likeButton = driver.find_element_by_class_name('likes-pill-button-inner')
#likeButton.click() 
