import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


EMAIL = 'elhaelha@yandex.ru'
PASSWORD = 'Franella123!'
PHONE = '+7 963 134-84-16'

WRONG_LOGIN = ['', 'elhaelha@mail.ru', '89631348416']
WRONG_LOGIN_IDS = ['empty email', 'wrong email', 'wrong phone number']
WRONG_PASSWORDS = ['', '123456', PASSWORD.upper(), PASSWORD.lower()]
WRONG_PASSWORD_IDS = ['empty password', 'wrong password', 'register upper', 'register lower']


def login(name, password):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(name)

    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(password)

    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, 'kc-login')))
    pytest.driver.find_element(By.ID, 'kc-login').click()