import os
from wireless import Wireless
def connecting_wifi(name,pwd):
    wireless = Wireless()
    wireless.connect(ssid=name, password=pwd)
connecting_wifi()
