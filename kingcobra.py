#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

#Default wait time
defaultWait = 10

#Default path for chromedriver is '/usr/local/bin/';
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10);

driver.get('https://www.google.com/webhp?gws_rd=ssl');

search_box = wait.until(expected_conditions.presence_of_element_located((By.NAME, 'q')));
print(search_box)

# Web Element API:
# https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html

search_box.send_keys('Saju Sasidharan')
search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
