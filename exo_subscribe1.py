# import paho mqtt
import paho.mqtt.client as mqtt

# import time for sleep()
import time

# buat callback on_message; jika ada pesan
# maka fungsi ini akan dipanggil secara asynch
########################################
def on_message(client, userdata, message):
    print("Message Received " ,
        str(message.payload.decode("utf-8")))
########################################
    
# buat definisi nama broker yang akan digunakan
broker_address = "broker.hivemq.com"

# buat client baru bernama P1
print("Creating new instance") 
client = mqtt.Client("P1")

# kaitkan callback on_message ke client
client.on_message = on_message

# buat koneksi ke broker
print("Connecting to broker") 
client.connect(broker_address, port = 1883)

# jalankan loop client
client.loop_start()

# print topik yang disubscribe (dalam konteks ini, "waktu")
print("Subscribing to topic","photo") 

# client melakukan subscribe ke topik "waktu"
client.subscribe("photo")

#stop loop
client.loop_stop()