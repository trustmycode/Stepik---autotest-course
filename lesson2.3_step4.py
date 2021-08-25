from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element_by_tag_name("button").click()
    driver.switch_to.alert.accept()
    driver.find_element_by_id("answer").send_keys(
        str(math.log(abs(12*math.sin(
            int(driver.find_element_by_id("input_value").text))))))
    driver.find_element_by_tag_name("button").click()
finally:
    time.sleep(15)
    driver.quit()
