import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = "C:/chromedriver/chromedriver.exe"

service = Service(executable_path=driver_path)
link = "https://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser,13).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
)
button2 = browser.find_element(By.ID, 'book')
button2.click()

x = browser.find_element(By.ID, 'input_value').text
res = str(math.log(abs(12 * math.sin(int(x)))))
input2 = browser.find_element(By.CSS_SELECTOR,'#answer')
input2.send_keys(res)
button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button.click()
input()