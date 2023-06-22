import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

driver = webdriver.Chrome()
# Open website
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(2)
# Enter "Admin" into "Username"
#time.sleep(2)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# Enter "******" into "Password"
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# Click on "Login"
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
# Click on Menu Button
time.sleep(2)
driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
# Click on "Logout"
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()

