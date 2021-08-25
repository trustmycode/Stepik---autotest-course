from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("answer")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
finally:
    time.sleep(15)
    browser.quit()
