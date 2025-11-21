'''
#learning how selenium works
from selenium import webdriver
from selenium.webdriver.common.by import By


def read():#geting USN and pwd from text file
    a=open("credentials.txt","r")
    credentials_list=a.readlines()
    return credentials_list

x=read()
srn=x[0]
pwd=x[1]
driver=webdriver.Safari()
driver.implicitly_wait(10)
driver.get("http://192.168.254.1:8090/httpclient.html")
driver.find_element(By.ID, "username").send_keys(srn)
driver.find_element(By.ID, "password").send_keys(pwd)
driver.find_element(By.ID, "loginbutton").click()

msg=["You are signed in as","maximum","incorrect"]
#functionality to be addde

scrape data from login page and check conection status 
Ie=signed in/maximum users,incorrect credentials
have a live signout button in the code when told logout the code should log out from the captive


breakpoint()
'''
#issues=safari dosent support headless==>in mac force install firefox,in windows
import time
from playwright.sync_api import sync_playwright, TimeoutError
def read():#geting USN and pwd from text file
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
        page.click("#loginbutton")
        page.wait_for_timeout(2000)
    except:
        pass
    browser.close()


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





'''x=read()
username=x[0].strip()
password=x[1].strip()
with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    # Initial login attempt
    browser_feedback = login_attempt(page, username, password)
    login_success = validator(browser_feedback, username, browser)

    if login_success:
        signin_to_signout(page, username, password, browser)
    else:
        browser.close()


#testing logout feature
with sync_playwright() as p:



    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("http://192.168.254.1:8090/httpclient.html")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]',password)

    page.click("#loginbutton")
    page.wait_for_timeout(5000)#without this the content is not geting captured :(
    time.sleep(10)
    print("Clicking on logout")
    page.click("#loginbutton")#logout feature is working
    print("Clicked")
    a=input()
    browser.close()



'''



'''
with sync_playwright() as p:



    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("http://192.168.254.1:8090/httpclient.html")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]',password)

    page.click("#loginbutton")
    page.wait_for_timeout(5000)#without this the content is not geting captured :(
    #current_url = page.url
    #print(f"Current URL: {current_url}")

    # Get all text content
    all_text = page.text_content('body')
    #print("=== PAGE CONTENT ===")
    #print(all_text.split())
    if 'Invalid' in all_text.split() or 'failed.' in all_text.split():
        print("Login Failed due to incorrect Username or password")
    elif username in all_text.split() :
        print("Login Successful")
    elif "Maximum" in all_text.split() :
        print("Your account has reached maximum Logins ")
        print("Try after  some time or log out from the other device")
    a=input()
    browser.close()

'''
'''
for j in all_text.split():
    if j=="failed":
        print("Login failed ,incorrect SRN/Password")
    if j=="Maximum":
        print("Maximum logins consider signing out of other device or Try Later")
    if j=="close":
        print("Login Successfull")
a=input("Enter LO to log out")
if a=="LO":
     page.click("#logoutbutton")
else:
    browser.close()
'''

    
        

    

