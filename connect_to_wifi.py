import os
from wireless import Wireless
def connecting_wifi():
    wireless = Wireless()
    wireless.connect(ssid="PESU-EC-Campus", password="PESU-EC-Campus")
connecting_wifi()
