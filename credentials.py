#file for accepting SRN and password
import os
import platform
import stdiomask
platform = platform.system()


def accept_name_password():
    x=""
    if os.path.exists('credentials.txt'):
        a = open("credentials.txt", "r")

        if a.readlines()!=[]:
            print("Credentials are stored :)")
        else:
            a = open("credentials.txt", "w")
            srn = input("Enter SRN : ")
            pwd = stdiomask.getpass("Password: ", mask='*')
            a.write(srn + "\n")
            # a.write("\n")
            a.write(pwd + "\n")
    else:
        a = open("credentials.txt", "w")
        srn=input("Enter SRN : ")
        pwd=input("Enter Password : ")
        a.write(srn+"\n")
        #a.write("\n")
        a.write(pwd+"\n")
    #a.write("\n")
    return x
def change_password():
    file = open("credentials.txt", "r")
    l=file.readlines()
    srn=l[0]
    pwd=l[1]
    #c=l[2]-->driver name
    a=input("Enter Your SRN ")
    print(srn)
    if (a)!=srn:
        print("SRN entered is wrong")
    else:
        b= stdiomask.getpass("Password: ", mask='*')
        if (b)!=pwd:
            print("Password entered is wrong ")
        else:
            srn=input("Enter New SRN : ")
            pwd= stdiomask.getpass("Password: ", mask='*')
            l=[srn,pwd]
    file.close()
    file=open("credentials.txt", "w")
    for j in l:
        file.write(j+"\n")
