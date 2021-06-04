from selenium import webdriver

import time
import datetime
from selenium.webdriver.common.keys import Keys
""""
doc & examples: https://selenium-python.readthedocs.io/installation.html#introduction
location elements: https://selenium-python.readthedocs.io/locating-elements.html
Chrome:   https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:   https://github.com/mozilla/geckodriver/releases
Safari:   https://webkit.org/blog/6900/webdriver-support-in-safari-10/
1. add +x rights
2. place to venv/bin directory


selenium antidetect: https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
"""



driver = webdriver.Firefox()
driver.get("http://hackeru.com")

burger = driver.find_element_by_id("mega-toggle-block-2")
if burger:
    time.sleep(2)
    burger.click()
    contact_link = driver.find_element_by_id("mega-menu-item-1530")
    time.sleep(2)
    contact_link.click()
    time.sleep(2)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    fullname = driver.find_element_by_id("fullName")
    x,y = fullname.location_once_scrolled_into_view
    print(x,y)
    s = ""
    for c in "Mamkin Hacker":
        fullname.send_keys(c)
        time.sleep(0.4)
    # time.sleep(2)
    # burger.click()
    # driver.execute_script("alert('hello, little fella!')")
    # time.sleep(2)
    # driver.switch_to.alert.accept()

    # driver.save_screenshot(f"screen_{datetime.datetime.now().strftime('%H.%M')}.png")

    driver.save_screenshot(f"screen_{datetime.datetime.now().strftime('%H_%M')}.png")
# driver.close()