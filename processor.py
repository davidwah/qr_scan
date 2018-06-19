from sys import argv
import zbar
import paho.mqtt.client as mqtt
import datetime
import time

mqtt = mqtt.Client("python_pub")
mqtt.connect("192.168.1.111", 1883)

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

# setup a callback
#def my_handler(proc, image, closure):
    # extract results
for symbol in proc.results:
        # do something useful with results
    print 'DATA', symbol.type, '=', '"%s"' % symbol.data, st

#proc.set_data_handler(my_handler)
mqtt.publish("yuhu",'%s' % symbol.data)
mqtt.loop(2)

# enable the preview window
proc.visible = True

# initiate scanning
proc.active = True
try:
    # keep scanning until user provides key/mouse input
    proc.user_wait()
except zbar.WindowClosed, e:
    pass


mqtt.loop(2)