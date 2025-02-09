from selenium import webdriver
from  selenium.webdriver.common.by import By 
from dotenv import load_dotenv
import os, time

load_dotenv()
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:
    def __init__(self):
        driver_options = webdriver.ChromeOptions()
        driver_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=driver_options)
        self.login()
        time.sleep(4.2)
        self.find_followers("chefsteps")
        # pass

    def login(self):
        self.driver.get('https://instagram.com')
        username_input = self.driver.find_element(by=By.NAME, value='username')
        username_input.send_keys(USER)

        password_input = self.driver.find_element(by=By.NAME, value="password")
        password_input.send_keys(PASSWORD)

        login_button  = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
        login_button.click()

    def find_followers(self, username) -> None:
        url = f'https://instagram.com/{username}/followers'
        self.driver.get(url)
        self.driver.execute_script("window.scrollTo(0, document.boy.scrollHeight)")

    def follow():
        buttons = self.driver.find_elements(by=By.TAG_NAME, value='button')
        print(buttons)
        pass