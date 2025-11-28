import credentials
import clear_stored_data
import connect_to_wifi
import enc_dec

import time
import platform
import stdiomask
print("===Enter 1 proceed to Login/Signup :: Enter 2 to change Password")
change_pwd=int(input())
if change_pwd==1:
    credentials.accept_name_password()

elif change_pwd==2:
    credentials.change_password()
else:
    credentials.accept_name_password()
if platform.system()=="Darwin":
    print("Looks Like You are on a MAC ")
    print("Soon You would see a pop up which comes when we connect to WIFI")
    print("Please press the cancel button as soon as it pops up ")
    time.sleep(2)
    connect_to_wifi.connecting_wifi()

elif platform.system()=="Windows":
    print("Looks like You are on Windows")
    print("Make sure the WIFI is turned on in the computer/settings")
    time.sleep(2)
    connect_to_wifi.connecting_wifi()
elif platform.system()=="Linux":
    print("Looks Like you are on Linux ")
    time.sleep(2)
    connect_to_wifi.connecting_wifi()
else:
    print("The OS used is not Known :(")
time.sleep(3)#stabelise post connecting to wifi
import login
print("Enter 1 -To quit execution :: 2 -Signout")
signout=int(input())
if signout==1:
    print("Stoping Execution")
elif signout==2:
    print("Signing out would clear Stored data (SRN/Password)")
    print("1-to confirm signout;2-to quit signout")
    decision=int(input())
    if decision==1:
        b= stdiomask.getpass("Password: ", mask='*')
        x=open("credentials.txt","r")
        content=x.readlines()
        if content[1].strip()==enc_dec.encrypt(b):
            clear_stored_data.clear()
            print("All stored data has been erased")

        else:
            print("Entered Password is Incorrect")
    elif decision==2:
        print("Stoping Execution")
    else:
        print("Stoping Execution")
else:
    print("Stoping Execution")