import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    driver = webdriver.Chrome()
    driver.get(link)
    x_elem = driver.find_element_by_id("input_value")
    x = x_elem.text
    y = calc(x)
    button = driver.find_element_by_tag_name("button")
    driver.execute_script('window.scrollBy(0, 130);', button)
    driver.find_element_by_id("answer").send_keys(y)
    driver.find_element_by_id("robotCheckbox").click()
    driver.find_element_by_id("robotsRule").click()
    button.click()
finally:
    time.sleep(15)
    driver.quit()
