from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name1 = browser.find_element_by_css_selector("input:nth-child(2)")
    name1.send_keys("Salavat")
    name2 = browser.find_element_by_css_selector("input:nth-child(4)")
    name2.send_keys("Anamov")
    email = browser.find_element_by_css_selector("input:nth-child(6)")
    email.send_keys("slavkoego@gmail.com")
    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)
    browser.find_element_by_css_selector("button").click()
finally:
    time.sleep(5)
