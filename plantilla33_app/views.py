# django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

# modelos
from plantilla33_app.models import Device, User
from plantilla33_app.forms import DeviceForm

# otros
from paho.mqtt import client as mqtt_client
import random
import json
import time

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



class Dashboard(View):
    def get(self, request):
        
        # obtenemos el usuario de la sesion
        user = User.objects.get(id=request.session['id'])
        devicess= Device.objects.all()

        context = {
            'user': user,
            'all_devicess':devicess
        }
        
        return render(request, 'dashboard.html', context)



####################################################################

class AddNewDev(View):
    
    
    
    def get(self, request):
        user = User.objects.get(id=request.session['id'])
        form = DeviceForm()
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'create.html', context)

    def post(self, request):
        print(request.POST)
        form = DeviceForm(request.POST)
        
        if form.is_valid():
            new_device = form.save(commit=False)
            new_device.added_by = User.objects.get(id=request.session['id'])
            form.save()
            return redirect(reverse('dashboard'))
        else:
            context = {
                'form': form,
            }
            return render(request,'create.html', context)


def ViewDev(request, id): # GET /wall/<id>

        
    context = {
        'device': Device.objects.get(id=id),
        'temp' : sensor()

    }
    return render(request, 'DevShow.html', context)

class EditDev(View):
    def get(self, request, id):
        user = User.objects.get(id=request.session['id'])
        device = Device.objects.get(id=id)
        form = DeviceForm(instance=device)
        context = {
            'form': form,
            'user': user,
            'device': device,
        }
        return render(request, 'EditDev.html', context)

    def post(self, request, id):
        device = Device.objects.get(id=id)
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard'))
        else:
            context = {
                'form': form,
                'device': device,
            }
            return render(request, 'EditDev.html', context)
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

