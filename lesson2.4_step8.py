from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    button = driver.find_element(By.ID, "book")
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()
    driver.find_element_by_id("answer").send_keys(
        str(math.log(abs(12 * math.sin(
            int(driver.find_element_by_id("input_value").text))))))
    driver.find_element(By.ID, "solve").click()
finally:
    time.sleep(15)
    driver.quit()
