#
# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# url = "http://www.adzjw.com/"
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(url)
# driver.implicitly_wait(5)
# # driver.find_element_by_id("login_link").clear()
# # driver.find_element_by_id("login_link").send_keys()
# # driver.find_element_by_id("login_link").click()
# # driver.find_element_by_id("login_link").submit()
# # right = driver.find_element_by_id("login_link")
# # ActionChains(driver).context_click(right).perform()
# # element = driver.find_element_by_id('login_link')
# # target = driver.find_element_by_id('sign_link')
# # ActionChains(driver).drag_and_drop(element, target).perform()
# left = driver.find_element_by_id('login_link')
# ActionChains(driver).click_and_hold(left).perform()
#
# time.sleep(2)
#
# driver.close()
#
# Keys

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()

driver.find_element_by_id("login_link").clear()
driver.find_element_by_id("login_link").send_keys()
driver.find_element_by_id("login_link").click()
driver.find_element_by_id("login_link").submit()
size = driver.find_element_by_id("id").size()
text = driver.find_element_by_id("id").text()
attribute = driver.find_element_by_id("id").get_attribute("type")
r = driver.find_element_by_id("id").is_displayed()
time.sleep(3)
driver.quit()



