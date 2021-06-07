from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os

driver = webdriver.Firefox()
driver.get("https://lms.hackeru.pro/login/index.php")


login = "ascanders@gmail.com"
username = driver.find_element_by_id("username")
for c in login:
    username.send_keys(c)
    time.sleep(0.01)


my_password = open('pass.txt', 'r').read()

password = driver.find_element_by_id("password")
for c in my_password:
    password.send_keys(c)
    time.sleep(0.01)


submit = driver.find_element_by_id("loginbtn")
submit.click()


#module = WebDriverWait(driver,20).until(expected_conditions.element_to_be_clickable((By.XPATH,"//a/span[contains(text(),'CSR-23_ 12.05.2021_ Python Programming For Penetration Testing')]")))
#module.click()

id = "12012"
driver.get("https://lms.hackeru.pro/mod/attendance/view.php?id=" + id)


mark = driver.find_element_by_link_text("Отправить посещаемость")
WebDriverWait(driver,20).until(expected_conditions.element_to_be_clickable(mark)).click


