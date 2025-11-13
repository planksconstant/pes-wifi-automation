import os
from wireless import Wireless
import platform
def connecting_wifi():
    platform_system = platform.system()
    if platform_system == "Darwin":
        exit_status = os.system("./connect_to_wifi_mac.sh")
        if exit_status==0:
            print("Script executed successfully")
        else:
            print("Issue")
    if platform_system =="Windows":
        exit_status=os.system("powershell -ExecutionPolicy Bypass -File connect_to_wifi_win.ps1")

