import pywhatkit
import time

# Wait a bit before running, just to make sure everything is ready
time.sleep(5)

# Sends message at 8:20 PM, waits 15 seconds before typing
pywhatkit.sendwhatmsg("+880xxxxxxxxx0", "Happy Birthday Sweet Heart", 20, 20, wait_time=15)
# Sends message at 8:21 PM, waits 15 seconds before typing
pywhatkit.sendwhatmsg("+8801xxxxxxxxx2", "Happy Birthday Sweet Heart", 20, 21, wait_time=15)

print("Message scheduled. Make sure not to touch your mouse or keyboard.")
