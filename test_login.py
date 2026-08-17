from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(r"C:\Users\arath\OneDrive\Desktop\software engineering\login.html")

driver.maximize_window()

driver.find_element(By.ID,"username").send_keys("admin")

driver.find_element(By.ID,"password").send_keys("12345")

driver.find_element(By.ID,"login").click()

time.sleep(2)

result = driver.find_element(By.ID,"result").text

print(result)

assert result=="Login Successful"

print("✅ TEST PASSED")

driver.quit()