import selenium
import platform
from selenium import webdriver
from enc_dec import decrypt
from selenium.webdriver.common.by import By  # Add this import
import time
def setup_drive():
    platform_system = platform.system()
    if platform_system == "Darwin":  # Darwin is mac
        print("Looks like you are on Mac OS ")
        return webdriver.Safari()
    elif platform_system == "Linux":
        print("Looks like you are on Linux")
        return webdriver.Chrome()
    elif platform_system=="Windows":
        print("Looks like you are on windows")
        return webdriver.Chrome()
    else:
        print("Unsuported OS :(")
def read():
    a=open("credentials.txt","r")
    credentials_list=a.readlines()
    return credentials_list
def automator():
    try:
        x=read()
        driver = setup_drive()
        username = x[0]
        password = decrypt(x[1].strip())
        driver.get("http://192.168.254.1:8090/httpclient.html")
        time.sleep(0.5)#required to make sure the fields do not get bad text
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.ID, "loginbutton").click()
        time.sleep(0.5)
    except:
        print("*")
    #finally:
        #driver.quit()




#login failed ==> <selenium.webdriver.remote.webelement.WebElement (session="9F63AA64-D1DE-45AA-B979-E37440C374B3", element="node-7AF1754A-1D40-44D0-B696-DA020798E7DF")>
#login success==> <selenium.webdriver.remote.webelement.WebElement (session="F821B13F-A9BC-4EDC-A196-2D2D8370E7DF", element="node-CCEE84C6-F0E9-417E-97E6-91615926F273")>
