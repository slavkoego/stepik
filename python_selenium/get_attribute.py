from selenium import webdriver

import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#ищем значение под картинкой
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
#вызываем функцию и  объявляем её y
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
#input1.send_keys(str(calc(x)) - другой вариант
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("body > div > form > div > div > button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()