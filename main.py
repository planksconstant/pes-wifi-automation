import credentials
import login


a=open("credentials.txt","r")
if a.readlines()==[]:
    credentials.accept_name_password()
login.automator()
