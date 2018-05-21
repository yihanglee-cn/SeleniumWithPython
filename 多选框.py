from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('1.html')
driver.get(file_path)

inputs = driver.find_elements_by_tag_name('input')

for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()

time.sleep(2)

driver.quit()