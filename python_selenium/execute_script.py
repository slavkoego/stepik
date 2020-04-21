from selenium import webdriver
import math
import time
try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_number = browser.find_element_by_id("input_value")
    x = x_number.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 130);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    print(y)
    time.sleep(10)
    browser.quit()

#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#browser.execute_script("window.scrollBy(0, 130);") #проскроллит на 130 пикселей вниз
#button.click()
#assert True