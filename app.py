from selenium import webdriver
from time import sleep
from secrets import phone, password
from keyboard import press


class Bumbot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://bumble.com/get-started')
        sleep(10)
        phone_login_button = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[3]/div')
        phone_login_button.click()

        phone_textbox = self.driver.find_element_by_xpath('//*[@id="phone"]')
        phone_textbox.send_keys(phone)
        sleep(2)

        ## continue_button = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[4]/button')
        ## continue_button.click()

        press('enter')

        sleep(2)

        password_textbox = self.driver.find_element_by_xpath('// *[ @ id = "pass"]')
        password_textbox.send_keys(password)

        login_button = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[2]/button')
        login_button.click()

        sleep(10)

    def like(self):
        like_button = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
        like_button.click()

    def autoLike(self):
        while True:
            sleep(2)
            self.like()


bot = Bumbot()
bot.login()
bot.autoLike()
