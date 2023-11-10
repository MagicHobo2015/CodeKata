import bluetooth
import threading
from alive_progress import alive_bar
from time import sleep

def progressBar():
    with alive_bar(100, spinner = 'radioactive') as bar:
        for i in range(100):
            sleep(.3)
            bar()
            
def discover():
    

print("Searching for Devices...")
# create a separate thread for the progress bar.
progressBarThread = threading.Thread(target=progressBar())
progressBarThread.start()

progressBarThread.join()

for addr, name in nearby_devices:
    print(" {} - {}".format(addr, name))