import socket
import urllib
import json
import pickle
import numpy as np
import cv2

url = 'http://192.168.1.4:8080/shot.jpg'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="127.0.0.1"
port=1234

s.connect((ip,port))
#o , addr = s.accept()

cap = cv2.VideoCapture(1)
address='https://192.168.43.1:8080/video'
cap.open(address)

try:
    while True:

        x = s.recv(1000000)
        print("Recieved")

        ret , photo = cap.read()
        ret, buffer = cv2.imencode('.jpg',photo)
        bytedata = pickle.dumps(buffer)
        s.send(bytedata)

        try:
            data = pickle.loads(x)
            data = cv2.imdecode(data,cv2.IMREAD_COLOR)
            if data is not None :
                cv2.imshow('photo',data)
                if cv2.waitKey(10) == 13 :
                    break
        except: 
            print("Waiting for the server!")


    cv2.destroyAllWindows()
except:
    cv2.destroyAllWindows()