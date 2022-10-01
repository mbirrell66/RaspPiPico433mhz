
import rfdevice
#import config
#import machine

sender = rfdevice.RFDevice()
sender.enable_tx()
test = ord("a")
test = test + ord("a")
sender.tx_code(int(test))