from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        a = "Congratulations! You have successfully registered!"
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
        input1.send_keys("Slava")
        input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Ego")
        input3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
        input3.send_keys("slavkoego@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(a, welcome, "Ошибка в тесте 1")

    def test_registration2(self):
        a = "Congratulations! You have successfully registered!"
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
        input1.send_keys("Slava")
        input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Ego")
        input3 = browser.find_element_by_css_selector("div.first_block > div.form-group.third_class > input")
        input3.send_keys("slavkoego@gmail.com")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(a, welcome, "Ошибка в тесте 2")


if __name__ == '__main__':
    unittest.main()
