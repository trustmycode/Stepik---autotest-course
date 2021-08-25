from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element_by_tag_name("button").click()
    new_wind = driver.window_handles[1]
    driver.switch_to.window(new_wind)
    driver.find_element_by_id("answer").send_keys(
        str(math.log(abs(12*math.sin(
            int(driver.find_element_by_id("input_value").text))))))
    driver.find_element_by_tag_name("button").click()
finally:
    time.sleep(15)
    driver.quit()
