import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://automation.credence.in/")
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Credence")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credence@credence13.in")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence.credence10.in")
driver.find_element(By.XPATH, "//input[@id='password-confirm']").send_keys("Credence.credence10.in")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# if driver.title == "CredKart":
#     print("Registration is completed")
# else:
#     print("Registration is failed")
try:
    driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
    print("Registration is completed")
except:
    print("Registration is failed")

time.sleep(10)