from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(By.ID, "answer").send_keys(calc(driver.find_element(By.CSS_SELECTOR, "#treasure[valuex]").get_attribute("valuex")))
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    time.sleep(20)
    driver.quit()
