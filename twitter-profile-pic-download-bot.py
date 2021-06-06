#!/usr/bin/env python
# coding: utf-8



import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import requests 


binary = FirefoxBinary(r'C:\Users\NDH00596\AppData\Local\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\Users\NDH00596\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe')


driver.get("https://twitter.com/")


loginButton =driver.find_element_by_xpath("//a[@data-testid='loginButton']")

loginButton.click()


userNameBox = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
passwordBox = driver.find_element_by_xpath("//input[@name='session[password]']")
userNameBox.send_keys('__username_')
passwordBox.send_keys('__password__')
validateLoginButton =driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']")
validateLoginButton.click()



count=1
i = 1
timeLine = driver.find_element_by_xpath("//div[@aria-label='Timeline: Your Home Timeline']")
urlList = []




while 1:
    timeLine = driver.find_element_by_xpath("//div[@aria-label='Timeline: Your Home Timeline']")
    profilePicList = timeLine.find_elements_by_xpath("//img[@class='css-9pa8cd']")
    save_path = r"C:\Users\NDH00596\Documents\Python\twitter-profiles"
    for pic in profilePicList:
        try:
            file_name = str(count)+'.jpg'
            completeName = os.path.join(save_path, file_name)
            url = pic.get_attribute("src")
            if urlList.count(url)==0:
                urlList.append(url)
                response = requests.get(url)
                file = open(completeName, "wb")
                file.write(response.content)
                file.close()
                count=count+1
        except:
            continue
    height = 100
    while(height):
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        height=height-1
 





