import selenium
from selenium import webdriver
import time
def read():
    a=open("credential.txt","r")
    credentials_list=a.readlines()
    return credentials_list
def automator():
    driver = webdriver.Safari()
    a=driver.get("http://www.python.org")
    print(type(a),a)
automator()l
