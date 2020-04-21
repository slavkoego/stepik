from selenium import webdriver
from selenium.webdriver.common.by import By
import time

    #обращаю внимание, тест должен упасть с ошибкой NoSuchElementException
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration1.html")

input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
input1.send_keys("Slava")
input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
input2.send_keys("Ego")
input3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
input3.send_keys("slavkoego@gmail.com")
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
time.sleep(1)

    # находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(3)
    # закрываем браузер после всех манипуляций
browser.quit()

