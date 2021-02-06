from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def login(email, password):
    driver = webdriver.Chrome("../ChromeDriver/chromedriver.exe")

    driver.get("https://discord.com/login")
    username_input = driver.find_element_by_name('email')
    username_input.send_keys(email)
    password_input = driver.find_element_by_name('password')
    password_input.send_keys(password)
    element_string = '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]'
    login_button = driver.find_element_by_xpath(element_string)
    login_button.click()

print("Your Discord account's E-mail >>")
email = input()
print("Your Discord account's Password >>")
password = input()
login(email, password)