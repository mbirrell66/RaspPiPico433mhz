import rfdevice
import time
from time import sleep
from machine import WDT
#import config
#import machine


sender = rfdevice.RFDevice()
sender.enable_tx()

while True:

    test = ord("a")
    test = test + ord("a")
    sender.tx_code(int(test))
    time.sleep(5)