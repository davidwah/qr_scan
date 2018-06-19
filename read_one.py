#!/usr/bin/python
from sys import argv
import zbar
import paho.mqtt.client as mqtt
import datetime
import time

mqtt = mqtt.Client("python_pub")
mqtt.connect("192.168.1.111", 1883)
#mqtt.publish("yuhu", "yuhuu")
#mqtt.loop(2)

#def alert():
#    client.connect("192.168.1.116", 1833, 60)
#    if data['qr'] == 'decode':
#        client.publish(topic="face", payload="1", retain=True)
#    elif data['qr'] == 'ok':
#        client.publish(topic="face", payload="0", retain=True)

#    client.disconnect()
#    return"ok"

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

    # create a Processor
proc = zbar.Processor()
    # configure the Processor
proc.parse_config('enable')
    # initialize the Processor
device = '/dev/video0'
if len(argv) > 1:
    device = argv[1]
proc.init(device)
    # enable the preview window
proc.visible = True
    # read at least one barcode (or until window closed)
proc.process_one()
    # hide the preview window
proc.visible = False
    # extract results
for symbol in proc.results:
        # do something useful with results
    print symbol.type, 'symbol', '%s' % symbol.data, st

mqtt.publish("yuhu",'%s' %symbol.data)
#	topic = yuhu
#	pesan = "%s"
mqtt.loop(2)
