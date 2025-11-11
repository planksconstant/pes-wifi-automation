import credentials

import time
import login
import clear_stored_data
#import connect_to_wifi
print("Running in review mode all stored data will be cleared :) ")
credentials.accept_name_password()
#connect_to_wifi.connecting_wifi()
#time.sleep(0.5)
login.automator()
clear_stored_data.clear()
