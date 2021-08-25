import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, ".form-group [name='firstname']").send_keys("end")
    driver.find_element(By.CSS_SELECTOR, ".form-group [name='lastname']").send_keys("to")
    driver.find_element(By.CSS_SELECTOR, ".form-group [name='email']").send_keys("send")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = driver.find_element(By.ID, "file")
    element.send_keys(file_path)
    driver.find_element(By.TAG_NAME, "button").click()
finally:
    time.sleep(15)
    driver.quit()
