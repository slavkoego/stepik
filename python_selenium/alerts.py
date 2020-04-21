from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("btn-primary").click()
    alert = browser.switch_to.alert
    alert.accept()
    x_number = browser.find_element_by_id("input_value")
    x = x_number.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    button = browser.find_element_by_css_selector("button")
    button.click()
finally:
    print(y)
    time.sleep(5)
    browser.quit()
