import time, datetime

import RPi.GPIO as GPIO

import telepot

from telepot.loop import MessageLoop


myled = 26

fan = 19

bulb = 13

tube = 6


now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

 

 

#MYLED

GPIO.setup(myled, GPIO.OUT)

GPIO.output(myled, 0) #Off initially

#fan

GPIO.setup(fan, GPIO.OUT)

GPIO.output(fan, 0) #Off initially

 #bulb

GPIO.setup(bulb, GPIO.OUT)

GPIO.output(bulb, 0) #Off initially

#tube

GPIO.setup(tube, GPIO.OUT)

GPIO.output(tube, 0) #Off initially



def action(msg):

    chat_id = msg['chat']['id']

    command = msg['text']


    print ('Received: %s' % command)


    if 'on' in command:

        message = "Turned on "

        if 'myled' in command:

            message = message + "myled"

            GPIO.output(myled, 1)

        if 'fan' in command:

            message = message + "fan "

            GPIO.output(fan, 1)

        if 'bulb' in command:

            message = message + "bulb "

            GPIO.output(bulb, 1)

        if 'tube' in command:

            message = message + "tube "

            GPIO.output(tube, 1)

        if 'all' in command:

            message = message + "all "

            GPIO.output(myled, 1)

            GPIO.output(fan, 1)

            GPIO.output(bulb, 1)

            GPIO.output(tube, 1)

        message = message + "light(s)"

        telegram_bot.sendMessage (chat_id, message)



    if 'off' in command:

        message = "Turned off "

        if 'myled' in command:

            message = message + "myled"

            GPIO.output(MYLED, 0)

        if 'fan' in command:

            message = message + "fan "

            GPIO.output(fan, 0)

        if 'bulb' in command:

            message = message + "bulb "

            GPIO.output(bulb, 0)

        if 'tube' in command:

            message = message + "tube "

            GPIO.output(tube, 0)

        if 'all' in command:

            message = message + "all "

            GPIO.output(myled, 0)

            GPIO.output(fan, 0)

            GPIO.output(bulb, 0)

            GPIO.output(tube, 0)

        message = message + "light(s)"

        telegram_bot.sendMessage (chat_id, message)


 


telegram_bot = telepot.Bot('5521025255:AAGFFPP_X_iJzi3VC34yIHoNuZw5FEUkElU')

print (telegram_bot.getMe())


MessageLoop(telegram_bot, action).run_as_thread()

print ('Code Unnati Home automation is Up and Running....')


while 1:

    time.sleep(10)

