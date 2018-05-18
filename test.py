
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = "http://www.adzjw.com/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(5)
# driver.find_element_by_id("login_link").clear()
# driver.find_element_by_id("login_link").send_keys()
# driver.find_element_by_id("login_link").click()
# driver.find_element_by_id("login_link").submit()
right = driver.find_element_by_id("login_link")
ActionChains(driver).context_click(right).perform()

time.sleep(2)

driver.close()


