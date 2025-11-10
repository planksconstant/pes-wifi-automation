import credentials
import login
import clear_stored_data
import connect_to_wifi
print("Running in review mode all stored data will be cleared :) ")
a=open("credentials.txt","r")
l=a.readlines()
wifiname=l[2]
wifipwd=l[3]
connect_to_wifi.connecting_wifi(wifiname,wifipwd)
if a.readlines()==[]:
    credentials.accept_name_password()
login.automator()
clear_stored_data.clear()
