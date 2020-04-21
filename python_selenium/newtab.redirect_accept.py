from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_class_name("trollface").click()
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
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
    time.sleep(5)
    browser.quit()