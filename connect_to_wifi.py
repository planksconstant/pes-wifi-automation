import os
import platform
def connecting_wifi():
    platform_system = platform.system()
    if platform_system == "Darwin":
        exit_status = os.system("./connect_to_wifi_mac.sh")
        if exit_status==0:
            print("Script executed successfully")
        else:
            print("Issue,try connecting to WI-FI manually")
    if platform_system =="Windows":
        exit_status=os.system("connect_wifi.cmd")

