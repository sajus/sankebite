#
from selenium import webdriver
import time

#Default path for chromedriver is '/usr/local/bin/';
driver = webdriver.Chrome()

driver.get('https://www.google.com/webhp?gws_rd=ssl');
time.sleep(5)

# Web Element API:
# https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html
search_box = driver.find_element_by_name('q')

search_box.send_keys('Saju Sasidharan')
search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()
