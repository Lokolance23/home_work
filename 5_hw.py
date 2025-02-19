from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

class Home_5:
    def __init__(self, url):
        self.url = url

    def finder(self):
        driver.get(self.url)
        print(self.url)
        password = driver.find_element(By.ID,"password")
        username = driver.find_element(By.ID, "user-name")
        login_button = driver.find_element(By.ID, "login-button")
        if password is not None and username is not None and login_button is not None:
            print("Элементы найдены")



demo = Home_5("https://www.saucedemo.com")
demo.finder()



