from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)
    x_elem = driver.find_element(By.ID, "input_value")
    x = x_elem.text
    y = calc(x)
    input0 = driver.find_element(By.ID, "answer")
    input0.send_keys(y)
    chkbx = driver.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']")
    chkbx.click()
    radiobx = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobx.click()
    button = driver.find_element(By.CSS_SELECTOR, "[type='submit'].btn")
    button.click()
finally:
    time.sleep(20)
    driver.quit()
