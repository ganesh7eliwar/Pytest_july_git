from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
# install selenium
# install pytest


class Test_Credence:

    def test_sum_001(self):
        a = 3
        b = 7
        sum = a + b
        print(sum)
        if sum == 10:
            assert True
        else:
            assert False

    def test_credence_url(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('https://automation.credence.in/login')
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys('7eliwar.ganesh@gmail.com')
        driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys('s@t07Ganesh')
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        try:
            driver.find_element(By.XPATH, '//h2[normalize-space()="CredKart"]')
            print('Login Successful')
            assert True

        except NoSuchElementException:
            print('Login Failed')
            assert False

        driver.quit()

    def test_sum_002(self):
        a = 3
        b = 7
        mul = a * b
        print(mul)
        if mul == 21:
            assert True
        else:
            assert False
