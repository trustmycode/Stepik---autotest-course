from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your first name']")#"div.first_block .form-control
    input1.send_keys("asd")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your last name']")#"div.first_block .form-control
    input2.send_keys("asddsa")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder = 'Input your email']")#"div.first_block .form-control
    input3.send_keys("qwezxc")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(8)
    browser.quit()
