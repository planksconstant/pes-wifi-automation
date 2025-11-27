#file for accepting SRN and password
import os
import platform
import stdiomask
from enc_dec import decrypt, encrypt
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
            pwd2=stdiomask.getpass("Confirm Password: ", mask='*')
            if pwd==pwd2:
                a.write(srn + "\n")
                # a.write("\n")
                a.write(encrypt(pwd) + "\n")
            else:
                print("The entered passwords do not match.")



    else:

        a = open("credentials.txt", "w")
        srn=input("Enter SRN : ")
        pwd=stdiomask.getpass("Enter Password : ")
        pwd2 = stdiomask.getpass("Confirm Password: ", mask='*')
        if pwd == pwd2:
            a.write(srn + "\n")
            # a.write("\n")
            a.write(encrypt(pwd) + "\n")
        else:
            print("The entered passwords do not match.")
    return x

def change_password():
    file = open("credentials.txt", "r")
    l=file.readlines()
    srn=l[0].strip()
    pwd=decrypt(l[1].strip())
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
            pwd= stdiomask.getpass("Enter New Password: ", mask='*')
            l=[srn,encrypt(pwd)]
    file.close()
    file=open("credentials.txt", "w")
    for j in l:
        file.write(j+"\n")
