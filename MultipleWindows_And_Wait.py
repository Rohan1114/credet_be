import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=option)
driver.get("https://the-internet.herokuapp.com/windows")
# driver.implicitly_wait(2)
# this is applicable for all web elements
# if element is present in 2 sec then this will not wait to complete 5 sec
# if element not present after 5sec then error can be there
driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']").click()
time.sleep(4)
WindowsOpen = driver.window_handles
time.sleep(4)
driver.switch_to.window(WindowsOpen[1])  # To switch driver at 2nd window
time.sleep(2)  # fix time
wait = WebDriverWait(driver, 10)  # Explicit Wait # On specific element
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='New Window']")))
time.sleep(2)
print(driver.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text)
time.sleep(2)
driver.switch_to.window(WindowsOpen[0])
time.sleep(2)
print(driver.find_element(By.XPATH, "//h3[normalize-space()='Opening a new window']").text)
# driver.close() # To close existing window
# driver.quit()  # To quit your Driver(Browser)
