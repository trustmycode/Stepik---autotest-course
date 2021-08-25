import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def sum(x, y):
    return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    x_1 = driver.find_element_by_id("num1")
    x = x_1.text
    y_2 = driver.find_element_by_id("num2")
    y = y_2.text
    xy = (sum(x, y))
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_visible_text(xy)
    driver.find_element_by_tag_name("button").click()
finally:
    time.sleep(15)
    driver.quit()
