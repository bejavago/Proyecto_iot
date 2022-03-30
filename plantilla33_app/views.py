from turtle import delay
from django.shortcuts import render, redirect
# from apps.wall_app.models import User
from plantilla33_app.models import Device, User
import time

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
datoss = {}

# Create your views here.
def dashboard(request):
    user = User.objects.get(id=request.session['id'])
    devicess= Device.objects.all()

    context = {
        'user': user,
        'all_devicess':devicess
    }
    return render(request,'dashboard.html', context)

####################################################################

def AddNewDev(request):
    if request.method == 'GET':
        return render(request,'create.html' )
    elif request.method == 'POST':
        print(request.POST)
        userss = User.objects.get(id=request.session['id'])
        item1= Device.objects.create(type=request.POST['type'],placed=request.POST['placed'],details=request.POST['details'], added_by=userss )
        return redirect('/dashboard')

def ViewDev(request, id): # GET /wall/<id>

        
    context = {
        'device': Device.objects.get(id=id),
        'temp' : sensor()

    }
    return render(request, 'DevShow.html', context)
# *********************************************
# 5 GET /shows/<id>
def EditDev(request, id):
    context = {
        'device': Device.objects.get(id=id)
    }
    return render(request, 'EditDev.html', context)
# *********************************************
# 6 POST shows/<id>/update
def UpdateDev(request, id):
    device = Device.objects.get(id=id)
    device.type = request.POST['type']
    device.placed = request.POST['placed']
    device.details = request.POST['details']
    device.save()
    return redirect('/dashboard')
# *********************************************
# 7 POST Device/<id>/destroy
def DeleteDev(request, id):
    device = Device.objects.get(id=id)
    device.delete()
    return redirect('/dashboard')
# *********************************************

def Logout(request):
    request.session.clear()
    print("Logged Out")
    return redirect('/')

#************************************************


def sensor():
    client = connect_mqtt()
    subscribe(client)
    
    #client.loop_forever()
    client.loop_start()
    time.sleep(3)
    client.loop_stop()
    
    
    
    #datoss={'temp':19 ,'hum':80}
    print('retunn',datoss)
    return datoss

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
        print('prueba suscribe1')
        y = json.loads(msg.payload.decode())
        temp = y["notification"]["parameters"]["temp"]
        hum = y["notification"]["parameters"]["humi"]
        print("temperature: ",temp,", humidity:",hum)
        global datoss
        datoss = {'temp':temp ,'hum':hum}
        print('onmessage',datoss)
        

        
    print('prueba suscribe2')    
    client.subscribe(topic)
    client.on_message = on_message
    #on_message(client)

