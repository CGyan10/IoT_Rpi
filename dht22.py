from grovepi import *
import math
# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 7  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

while True:
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = dht(sensor,blue)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            #print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
            print("temp = {:.2f}C\thumidity = {:.2f}%".format(temp, humidity))

    except IOError:
        print ("Error")