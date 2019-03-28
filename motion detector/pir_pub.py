import RPi.GPIO as gpio
import time
#import paho.mqtt.client as mqtt
import paho.mqtt.publish as pub

#mqtt_client=mqtt.client()
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(13,gpio.IN)

while True:
	pirSig=gpio.input(13)
	if pirSig==1:
		print("Motion detected")
		pub.single("pir_channel","Motion Detected!!",hostname="localhost")
		time.sleep(1)
	else:
		print("No motion detected")
		pub.single("pir_channel","No motion detection.",hostname="localhost")
		time.sleep(0.3)
