#!/usr/bin/python


from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

lcd.begin(16,1)

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

try:
    while 1:
        lcd.clear()
#        lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        lcd.message('Ofus')
        lcd.scrollDisplayRight()
        sleep(2)
except KeyboardInterrupt:
    print "BYE"
    lcd.clear()
