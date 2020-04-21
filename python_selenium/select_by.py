from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    t = int(x) + int(y)
    t1 = str(t)
    DropDown = Select (browser.find_element_by_id("dropdown"))
    DropDown.select_by_value(t1)
    click1 = browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector("button").click()


#   select = Select(browser.find_element_by_css_selector("select"))
#   select.select_by_value() # ищем элемент с текстом "Python"
finally:
    print(t)
    time.sleep(5)
    browser.quit()