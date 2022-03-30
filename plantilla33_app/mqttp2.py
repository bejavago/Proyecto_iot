from paho.mqtt import client as mqtt_client
import random
import json





broker = '127.0.0.1'
#broker = '192.168.1.11'
port = 1883
topic = "api/request"
topic_sub = "api/notification/37/#"
# generate client ID with pub prefix randomly
client_id = f'username{random.randint(0, 100)}'
#client_id = 'username0001'
username = 'MQTT_username'
password = '12345678'
deviceId = "s3s9TFhT9WbDsA0CxlWeAKuZykjcmO6PoxK6"


def connect_mqtt():

    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)

    print(client_id)
    client = mqtt_client.Client(client_id)
    clean_session=True
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, status):
    msg = "{\"action\":\"command/insert\",\"deviceId\":\""+deviceId+"\",\"command\":{\"command\":\"LED_control\",\"parameters\":{\"led\":\""+status+"\"}}}"
    result = client.publish(msg,topic)
    msg_status = result[0]
    if msg_status ==0:
        print(f"message : {msg} sent to topic {topic}")
    else:
        print(f"Failed to send message to topic {topic}")

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        y = json.loads(msg.payload.decode())
        temp = y["notification"]["parameters"]["temp"]
        hum = y["notification"]["parameters"]["humi"]
        print("temperature: ",temp,", humidity:",hum)
        
        return y
        
    print('prueba suscribe2')    
    client.subscribe(topic)
    client.on_message = on_message
    #on_message(client)



def main():
    client = connect_mqtt()
    subscribe(client)
    
    client.loop_forever()
    

if __name__ == '__main__':
    main()