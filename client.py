import socket
import urllib
import json
import pickle
import numpy as np
import cv2


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                 # creating socket
ip="127.0.0.1"                                                       # IP address of destination
port=1234                                                            # port of destination IP address

s.connect((ip,port))                                                 #creating the connection
#o , addr = s.accept()

cap = cv2.VideoCapture(1)
address='https://192.168.43.1:8080/video'                            # using the ip of the external webcam for using it in cap
cap.open(address)

try:
    while True:

        x = s.recv(1000000)              #receiving from the socket connected
        print("Recieved")

        ret , photo = cap.read()                              # -------sending part-------------
        ret, buffer = cv2.imencode('.jpg',photo)              # compressing the .jpf file and storing it in the memory buffer that is resized to fit the result
        bytedata = pickle.dumps(buffer)                       # pickle serialises the object file. Serializing and saving it in bytedata
        s.send(bytedata)                                      # sending over s socket

        try:                                                  #--------receiving part-----------
            data = pickle.loads(x)                            # serializing back the deserialized data that was received in x.
            data = cv2.imdecode(data,cv2.IMREAD_COLOR)        # doing reverse of what is done in line 27. Uncompressing and getting the info from memory buffer
            if data is not None :
                cv2.imshow('client',data)
                if cv2.waitKey(10) == 13 :
                    break
        except: 
            print("Waiting for the server!")


    cv2.destroyAllWindows()
except:
    cv2.destroyAllWindows()
