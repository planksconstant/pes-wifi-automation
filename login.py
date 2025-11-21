<<<<<<< HEAD
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
=======
import time
from playwright.sync_api import sync_playwright, TimeoutError
def read():#geting USN and pwd from text file
>>>>>>> 4b50be392aef9101f3fd7825edd31572d31c94a9
    a=open("credentials.txt","r")
    credentials_list=a.readlines()
    return credentials_list

def login_attempt(page,username,password):
    page.goto("http://192.168.254.1:8090/httpclient.html")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click("#loginbutton")
    page.wait_for_timeout(5000)  # without this the content is not geting captured :(
    all_text = page.text_content('body')
    return all_text

def validator(all_text,username):
    if 'Invalid' in all_text or 'failed' in all_text:
        print("Login Failed due to incorrect Username or password")
        return False
    elif username in all_text:
        print("Login Successful")
        return True
    elif "Maximum" in all_text:
        print("Your account has reached maximum Logins")
        print("Try after some time or log out from the other device")
        return False
    else:
        print("Unknown response from portal")
        # Print more content for debugging
        print(f"Full page content: {all_text}")
        return False


def login_after_logout(page,username, password):
    page.goto("http://192.168.254.1:8090/httpclient.html")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click("#loginbutton")
    page.wait_for_timeout(5000)
    return page.text_content('body')


def sign_in_to_signout_ver2(page, username, password, browser):
    #issue-so until u press enter or smth only then the refresh happens or else the refresh gets stuck cuz it never enters code post input block

    print("Session started. Auto-refreshing every 10 minutes.")

    refresh_count = 0
    user_wants_to_stop = False

    while not user_wants_to_stop:
        refresh_count += 1
        print(f"\n--- Refresh #{refresh_count} at {time.strftime('%H:%M:%S')} ---")

        # Ask user if they want to continue
        user_input = input("Type 'LO' to logout or press Enter to continue for 10 more minutes: ").strip().upper()
        if user_input == "LO":
            user_wants_to_stop = True
            break

        print("Continuing for 10 minutes...")
        time.sleep(10)  # 10 minutes

        print("Refreshing session...")
        try:
            # Logout and login again
            page.click("#loginbutton")
            page.wait_for_timeout(3000)
            page.goto("http://192.168.254.1:8090/httpclient.html")
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)
            page.click("#loginbutton")
            page.wait_for_timeout(5000)

            # Check if login was successful
            current_content = page.text_content('body')
            if username in current_content:
                print("Refresh successful!")
            else:
                print("Re-login failed!")
                break

        except Exception as e:
            print(f"Error during refresh: {e}")
            break

    print("Logging you out and closing browser...")
    try:
<<<<<<< HEAD
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
=======
        page.click("#loginbutton")
        page.wait_for_timeout(2000)
    except:
        pass
    browser.close()
>>>>>>> 4b50be392aef9101f3fd7825edd31572d31c94a9


x = read()
username = x[0].strip()
password = x[1].strip()

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    # Initial login attempt
    all_text = login_attempt(page, username, password)
    true_or_false = validator(all_text, username)  # Fixed: removed browser parameter

    if true_or_false==True:
        print("Sign in successful! Starting auto-refresh...")
        sign_in_to_signout_ver2(page, username, password, browser)
    else:
        print("Initial login failed. Closing browser.")
        browser.close()

