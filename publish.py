# import paho mqtt
import paho.mqtt.client as mqtt

# import time untuk sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
from datetime import datetime

# import thread untuk memakai sistem threading parallel
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

# fungsi untuk publish IP Publisher dengan topik "exo/log"
def pubIpPublisher():
    ip_address = get('https://api.ipify.org').text

    now = datetime.now()
    date_time = now.strftime("%d %m %Y, %H:%M:%S")
    # client melakukan publish data dengan topik "exo/log"
    return client.publish("exo/log", "Publisher : "+str(ip_address)+" at "+date_time)

# fungsi untuk publish photo dengan topik "exo/photo"
def exoPhoto():
    f = open("exo.jpg", "rb")
    fileContent = f.read()
    byteArr = bytearray(fileContent)
    # client melakukan publish data dengan topik "exo/photo"
    return client.publish("exo/photo", byteArr, 1)

# definisikan nama broker yang akan digunakan
broker_address = "broker.hivemq.com"

# buat client baru bernama P1
print("Creating New Instance")
client = mqtt.Client("P1")

# kaitkan callback on_publish ke client
client.on_publish=on_publish

# lakukan koneksi ke broker
print("Connecting to Broker")
client.connect(broker_address, port=1883)

# fungsi publish secara parallel
def publishTopic():
    Thread(target = pubIpPublisher).start()
    Thread(target = exoPhoto).start()

# mulai loop client
client.loop_start()

# publish topic dengan loop
for i in range (5):
    # sleep 1 detik
    time.sleep(1)

    publishTopic()
    
# stop loop
client.loop_stop()