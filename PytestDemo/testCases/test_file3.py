import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Pytest:

    def test_OrangeHRM_007(self):
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

    def test_Registeration_008(self):
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

