# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# import datetime untuk mendapatkan waktu dan tanggal
from datetime import datetime

from requests import get

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

def on_message_bytes(client, userdata, message):
    ip_address = get('https://api.ipify.org').text

    f = open('myidol.jpg', 'wb')
    f.write(message.payload)
    now = datetime.now()
    date_time = now.strftime("%d %m %Y, %H:%M:%S")
    print("Image received by "+ip_address+" at "+date_time+"\n")
    f.close()
    
# buat definisi nama broker yang akan digunakan
broker_address = "broker.hivemq.com"

# buat client baru bernama P2
print("Creating New Instance")
client = mqtt.Client("P2")

# menambahkan callback 
client.message_callback_add("exo/log", on_message)
client.message_callback_add("exo/photo", on_message_bytes)

# kaitkan callback on_message ke client
client.on_message=on_message

# buat koneksi ke broker
print("Connecting to Broker")
client.connect(broker_address, port=1883)

# jalankan loop client
client.loop_start()

# print topik yang disubscribe (dalam konteks ini adalah "exo/photo")
print("Subcribing to topic", "exo/photo")

# loop forever
while True:
    # client melakukan subscribe ke topik "exo/photo" dan "exo/log"
    client.subscribe("exo/log")
    client.subscribe("exo/photo")

    # berikan waktu tunggu 1 detik
    time.sleep(1) 

#stop loop
client.loop_stop()