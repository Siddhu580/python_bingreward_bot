from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json 
from random import randint
import random
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
time.sleep(randint(1,3))

#Login to the bing account by making a function
def sign_in(browser, email, password):
    time.sleep(randint(6,7))
    browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=15&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d12FC900BAC776E2521478345ADC56F47%26nopa%3d2&wp=MBI_SSL&lc=1033&CSRFToken=bc5b735a-1699-40d9-b575-f793d95b8a54&aadredir=1&nopa=2')
    time.sleep(randint(6,7))
    email_login = browser.find_element(By.XPATH, '//*[@id="i0116"]')
    time.sleep(randint(6,7))
    email_login.send_keys(email)
    time.sleep(randint(6,7))
    email_login.send_keys(Keys.RETURN)
    time.sleep(randint(6,7))
    email_pass = browser.find_element(By.XPATH, '//*[@id="i0118"]')
    time.sleep(randint(6,7))
    email_pass.send_keys(password)
    time.sleep(randint(6,7))
    email_pass.send_keys(Keys.RETURN)
    time.sleep(randint(6,7))
    no = browser.find_element(By.XPATH, '//*[@id="idBtn_Back"]')
    no.click()

def sign_out(browser):
    browser.get('https://rewards.bing.com/')
    time.sleep(randint(6,7))
    image = browser.find_element(By.XPATH, '//*[@id="img_sec_default"]')
    time.sleep(randint(6,7))
    image.click()
    out = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div/div[2]/div[2]/div/div[1]/div[2]/a')
    time.sleep(3)
    out.click()
    time.sleep(5)


def search(browser,words):
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #Start searching
    for i in range(0,30):
        time.sleep(randint(3,4))
        Search_box = browser.find_element(By.XPATH, '//*[@id="sb_form_q"]')
        Search_box.clear()
        Search_box = browser.find_element(By.XPATH, '//*[@id="sb_form_q"]')
        time.sleep(randint(1,3))
        Search_box.send_keys(random.choice(words))
        time.sleep(randint(1,3))
        Search_box.send_keys(Keys.RETURN)
        time.sleep(randint(1,3))
        Search_box = browser.find_element(By.XPATH, '//*[@id="sb_form_q"]')
        Search_box.clear()
        time.sleep(randint(2,4))
 
#Code starts running from here
#calling the function
logins = open('logins.txt', 'r').read().split('\n')
with open("words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
for login in logins:
    info = login.split(':')
    sign_in(browser, info[0], info[1])
    search(browser,words)
    sign_out(browser)










