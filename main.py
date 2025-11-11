import credentials
credentials.accept_name_password()

import time
import login
import clear_stored_data
import connect_to_wifi
print("Running in review mode all stored data will be cleared :) ")
connect_to_wifi.connecting_wifi()
time.sleep(0.5)
login.automator()
clear_stored_data.clear()
