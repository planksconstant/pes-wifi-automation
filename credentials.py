#file for accepting SRN and password
import os
import platform
platform = platform.system()

class login():

    def config(self):
        a = open("credentials.txt", "r")
        if a.readlines() != []:
            a = open("credentials.txt", "a")
            if platform=="Darwin":#Darwin is mac
                print("Looks like you are on Mac OS ")
                print("Are you on an ARM processor? (Apple M Series Chip)")
                if input("[y/n]") == "y":
                    a.write("chromedriver_macos_arm")
                else:
                    a.write("chromedriver_macos_x64")
            elif platform=="Linux":
                print("Looks like you are on Linux")
                a.write("chromedriver_linux_64")
            elif platform=="Windows":
                print("Looks like you are on Windows")
                a.write("chromedriver_win64.exe")
            else:
                print("Looks like you are on an unsupported platform :( ")
        else:
            print("Configuration Issue Contact @planksconstant ")
            global login_issue




    def accept_name_password(self):

        a = open("credentials.txt", "w")
        srn=input("Enter SRN : ")
        pwd=input("Enter Password : ")
        a.write(srn+"\n")
        #a.write("\n")
        a.write(pwd+"\n")
        #a.write("\n")
    def change_password(self):
        file = open("credentials.txt", "r")
        l=file.readlines()
        srn=l[0]
        pwd=l[1]
        c=l[2]
        print(srn)
        print(l)
        a=input("Enter Your SRN ")
        if (a+'\n')!=srn:
            print("SRN entered is wrong")
        else:
            b=input("Enter your Password ")
            if (b+'\n')!=pwd:
                print("Password entered is wrong ")
            else:
                srn=input("Enter New SRN : ")
                pwd=input("Enter password : ")
                l=[srn,pwd,c]

        file.close()
        file=open("credentials.txt", "w")
        for j in l:
            file.write(j+"\n")



login().change_password()

