# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
from datetime import datetime

## importing socket module
import socket

from threading import Thread

from requests import get

# buat callback on_publish untuk publish data
########################################
def on_publish(client, userdata, result):
    now = datetime.now()
    date_time = now.strftime("%d %m %Y, %H:%M:%S")
    print(f"Published at {date_time} \n")
    pass
########################################

def getIpPublisher():
    ip_address = get('https://api.ipify.org').text

    now = datetime.now()
    date_time = now.strftime("%d %m %Y, %H:%M:%S")

    return client.publish("log_ripki", "Publisher : "+str(ip_address)+" at "+date_time)

def exoPhoto():
    f = open("exo.jpg", "rb")
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    # client melakukan publish data dengan topik "waktu"
    return client.publish("ripki", byteArr, 1)

# definisikan nama broker yang akan digunakan
broker_address = "broker.hivemq.com"

# buat client baru bernama P2
print("Creating New Instance")
client = mqtt.Client("P1")

# kaitkan callback on_publish ke client
client.on_publish=on_publish

# lakukan koneksi ke broker
print("Connecting to Broker")
client.connect(broker_address, port=1883)

def publishTopic():
    Thread(target = getIpPublisher).start()
    Thread(target = exoPhoto).start()

# mulai loop client
client.loop_start()

# lakukan 20x publish waktu dengan topik "waktu"
for i in range (5):
    # sleep 1 detik
    time.sleep(1)

    publishTopic()
    
#stop loop
client.loop_stop()