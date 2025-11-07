#file for accepting SRN and password
import os
import platform
import getpass

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
        if os.path.exists('credentials.txt'):
            a = open("credentials.txt", "r")

            if a.readlines()!=[]:
                print("Credentials are stored :)")
            else:
                a = open("credentials.txt", "w")
                srn = input("Enter SRN : ")
                pwd = getpass.getpass(prompt='Enter your password: ')
                a.write(srn + "\n")
                # a.write("\n")
                a.write(pwd + "\n")

        else:
            a = open("credentials.txt", "w")
            srn=input("Enter SRN : ")
            pwd = getpass.getpass(prompt='Enter your password: ')
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



n=0
while n<3:
    print("Enter the numbers for the following operations")
    print("1=Creating credentials")
    print("2=Change SRN/Password")
    print("3=Exit the menu")
    n=int(input(""))
    if n==1:
        login().accept_name_password()
        login().config()
    elif n==2:
        login().change_password()
    elif n==3:
        break
    else:
        break



