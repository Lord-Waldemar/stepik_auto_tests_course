import unittest
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

driver_path = "C:/chromedriver/chromedriver.exe"  # Пример: "C:/drivers/chromedriver.exe"

service = Service(executable_path=driver_path)


class TestAbs(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')
        x_element = browser.find_element(By.ID, 'treasure')
        x = x_element.get_attribute('valuex')
        y = str(math.log(abs(12 * math.sin(int(x)))))
        input = browser.find_element(By.CSS_SELECTOR, '#answer')
        input.send_keys(y)
        input2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
        input2.click()
        input3 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
        input3.click()
        button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_2(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')
        x_element = browser.find_element(By.ID, 'treasure')
        x = x_element.get_attribute('valuex')
        y = str(math.log(abs(12 * math.sin(int(x)))))
        input = browser.find_element(By.CSS_SELECTOR, '#answer')
        input.send_keys(y)
        input2 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
        input2.click()
        input3 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
        input3.click()
        button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
