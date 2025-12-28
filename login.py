import time
from playwright.sync_api import sync_playwright, TimeoutError
import enc_dec

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
       
        print(f"Full page content: {all_text}")
        return False


def login_after_logout(page,username, password):
    page.goto("http://192.168.254.1:8090/httpclient.html")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click("#loginbutton")
    page.wait_for_timeout(5000)
    return page.text_content('body')

user_wants_to_stop=False
import threading
import time
from playwright.sync_api import sync_playwright
import sys
import select
from playwright.sync_api import sync_playwright


def sign_in_to_signout_ver2(page, username, password, browser):
    print("Session started. Auto-refreshing every 10 minutes.")
    print("Type 'LO' and press Enter to logout at any time")

    refresh_count = 0
    user_wants_to_stop = False

    def check_for_input():
        """Check if user input is available without blocking"""
        try:
            # Check if there's input ready (non-blocking)-->stackoverflow idea
            if select.select([sys.stdin], [], [], 0)[0]:
                user_input = sys.stdin.readline().strip().upper()
                return user_input == "LO"
        except:
            pass
        return False

    while not user_wants_to_stop:
        refresh_count += 1
        print(f"\n--- Refresh #{refresh_count} at {time.strftime('%H:%M:%S')} ---")

        # Check for user input
        if check_for_input():
            print("Logout requested!")
            user_wants_to_stop = True
            break

        # Performing refresh operation
        try:
            page.click("#loginbutton")
            page.wait_for_timeout(3000)
            page.goto("http://192.168.254.1:8090/httpclient.html")
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)
            page.click("#loginbutton")
            page.wait_for_timeout(5000)
            current_content = page.text_content('body')
            if username in current_content:
                print("Refresh successful!")
            else:
                print("Re-login failed!")
                break
        except Exception as e:
            print(f"Exception occurred: {e}")
            break

        # Wait period 
        print("Waiting... (type 'LO' to logout)")
        wait_time = 600  
        check_interval = 1  # Check every second

        for i in range(wait_time):
            if check_for_input():
                print("Logout requested!")
                user_wants_to_stop = True
                break
            time.sleep(check_interval)

    # logout sequence
    if user_wants_to_stop:
        print("Logging out...")
        try:
            page.click("#loginbutton")
            page.wait_for_timeout(2000)
        except Exception as e:
            print(f"Error during logout: {e}")
        finally:
            browser.close()


# control flow
x = read()
username = x[0].strip()
password = enc_dec.decrypt(x[1].strip())

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Initial login attempt
    all_text = login_attempt(page, username, password)
    true_or_false = validator(all_text, username)

    if true_or_false:
        print("Sign in successful! Starting auto-refresh sequence...")
        # Run everything in main thread - no threading needed
        sign_in_to_signout_ver2(page, username, password, browser)
    else:
        print("Initial login failed. Closing browser.")
        browser.close()
'''
Non Blocking input check

What select.select([sys.stdin], [], [], 0) Does:
select.select() - Monitors file descriptors for activity

[sys.stdin] - Watches the standard input (keyboard) for data

[] - No output streams to watch

[] - No error streams to watch

0 - Timeout of 0 seconds (non-blocking)
if the list is empty the user has not entered anything else the user has entered smth


Non-blocking: The script doesn't stop and wait for input

Responsive: Can detect "LO" at any time during the 10-minute cycle

Single-threaded: No threading complications with Playwright

Immediate response: User doesn't have to wait for current operation to finish

Credits similar to -https://stackoverflow.com/questions/2408560/non-blocking-console-input
https://stackoverflow.com/questions/6171132/non-blocking-console-input-c
'''
