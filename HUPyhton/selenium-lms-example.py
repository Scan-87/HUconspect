from selenium import webdriver
import selenium
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import datetime
from pswd import PASSWORD
LMS_LOGIN ="https://lms.hackeru.pro/login/index.php"
LOGIN = "i.krivonos@hackeru.com"


def lms_login(driver:webdriver.Firefox, url=LMS_LOGIN):
    driver.get(url)
    login_input = driver.find_element_by_id("username")
    for c in LOGIN:
        login_input.send_keys(c)
        time.sleep(0.1)
    pass_input = driver.find_element_by_id("password")
    for c in PASSWORD:
        pass_input.send_keys(c)
        time.sleep(0.1)
    login_btn = driver.find_element_by_id("loginbtn")
    login_btn.click()
    time.sleep(1)
    # card = driver.find_element_by_link_text("CSR-1. 12.01.2021_Python Programming For Penetration Testing")
    # card = driver.find_element_by_link_text("CSR-23_ 12.05.2021_ Python Programming For Penetration Testing")
    # card = driver.find_element_by_xpath(xpath="//a/span[contains(text(),'CSR-23_ 12.05.2021_ Python Programming For Penetration Testing')]")
    # card = driver.find_element_by_xpath(xpath="//a/span[@class='foo']")
    # card = card.find_element_by_xpath("..")


    WebDriverWait(driver,20).until(expected_conditions.element_to_be_clickable((By.XPATH,"//a/span[contains(text(),'CSR-23_ 12.05.2021_ Python Programming For Penetration Testing')]"))).click()

    # time.sleep(1)
    # card.click()

    # print(card.text)
    # a = card.parent
    # print("a", a.tag_name)
    # print("a", a.text)

    time.sleep(1)
    module = driver.find_element_by_id("module-11224")
    # tasks = module.find_element_by_tag_name("a")
    tasks = module.find_element_by_xpath(".//a[1]")
    # tasks.click()
    url = tasks.get_attribute("href")
    print("task url:",url)
    driver.get(url)

    time.sleep(1)
    table = driver.find_element_by_class_name("generaltable")

    # row = driver.find_element_by_partial_link_text(datetime.datetime.today().strftime("%d.%m.%y"))
    row = table.find_element_by_xpath(".//*[contains(text(),'{}')]".format(datetime.datetime.today().strftime('%-d.%m.%y')))
    parent_tr = row.find_element_by_xpath('..').find_element_by_xpath("..")
    # x,y = row.location_once_scrolled_into_view
    print(parent_tr.tag_name)
    a = parent_tr.find_element_by_xpath(".//*[@title='Пароль']")
    # a = row.find_element_by_class_name("helptooltip")
    url = a.get_attribute("href")
    driver.get(url)
    # a.click()
    time.sleep(2)
    driver.execute_script("alert('end')")

# options = webdriver.FirefoxOptions()
# options.add_argument("--start-maximized")
driver = webdriver.Firefox()
driver.maximize_window()
lms_login(driver)