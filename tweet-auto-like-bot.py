#!/usr/bin/env python
# coding: utf-8

# In[39]:


import webbrowser
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

binary = FirefoxBinary(r'C:\Users\NDH00596\AppData\Local\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\Users\NDH00596\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe')


driver.get("https://twitter.com/")



content = driver.page_source
soup = BeautifulSoup(content)


loginButton =driver.find_element_by_xpath("//a[@data-testid='loginButton']")

loginButton.click()


userNameBox = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
passwordBox = driver.find_element_by_xpath("//input[@name='session[password]']")
userNameBox.send_keys('__username__')
passwordBox.send_keys('__password__')
validateLoginButton =driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']")
validateLoginButton.click()


while 1:
    tweetsList = driver.find_elements_by_xpath("//div[@data-testid='tweet']")
    tweetsListToLike = driver.find_elements_by_xpath("//div[@data-testid='like']")
    for tweet in tweetsListToLike:
        tweet.click()
    driver.execute_script("window.scrollY + 200") 
    

