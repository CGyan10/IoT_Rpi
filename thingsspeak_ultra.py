from grovepi import *
import sys
import os
import time
import urllib #pip install urllib
from urllib import request

myAPI = "RYCTR7KP7WG48L8Z"  # API Key from thingSpeak.com channel
myDelay = 15 #how many seconds between posting data

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

ultrasonic_ranger = 4

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

while True:
    try:
           # Read distance value from Ultrasonic
            distant = ultrasonicRead(ultrasonic_ranger)
            time.sleep(0.5)
                        
            distant=str(distant)
            f = urllib.request.urlopen(baseURL + "&field1=%s" %distant)
            f.close()

            print(distant)

            time.sleep(int(myDelay))

        

    except TypeError:
        print("Error")
    except IOError:
        print("Error")
