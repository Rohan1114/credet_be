import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 Open Browser/ Driver
driver = webdriver.Chrome()

driver.maximize_window()

# 2 Opening Url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
# 3 Enter Username
driver.find_element(By.NAME, "username").send_keys("Admin")

# 4 Enter Password
driver.find_element(By.NAME, "password").send_keys("admin123")

# 5 Click on login button
driver.find_element(By.CLASS_NAME, "oxd-button").click()

time.sleep(2)

# 6 Click on Menu button
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()

# 7 Click on logout button
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()




time.sleep(5)