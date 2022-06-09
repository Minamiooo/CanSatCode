# MQTT Functions for Team 1076
import paho.mqtt.client as mqtt
import time, random, csv

broker = 'broker.emqx.io' # 'cansat.info'
port = 1883
topic = '/python/mqtt' #'teams/1076'

def connect_mqtt():
    
    client = mqtt.Client()
    client.username_pw_set('emqx','public') # user and pass for CanSat is 1076 and Ceajpevy493
    client.connect(broker,port)
    return client

def publish(client,data):
    result = client.publish(topic,payload = data)
    status = result[0]
    if status == 0:
        print(f"Sent `{data}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def run(data):
    client = connect_mqtt()
    # client.loop_start()
    publish(client,data)
