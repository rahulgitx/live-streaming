
import socket
import json
import pickle
import cv2

cap = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="127.0.0.1"
port=1234
socket_address = (ip,port)

try:
    s.bind((ip,port))
    print("Binded")
    s.listen()
    print("LISTENING AT:",socket_address)

    o , addr = s.accept()
    print(o)
    print("Connected to {}".format(addr))
    while True:
        ret , photo = cap.read()
        ret, buffer = cv2.imencode('.jpg',photo)
        bytedata = pickle.dumps(buffer)
        o.send(bytedata)

        x = o.recv(1000000)

        data = pickle.loads(x)
        data = cv2.imdecode(data,cv2.IMREAD_COLOR)
        if data is not None :
            cv2.imshow('serverphoto',data)
            if cv2.waitKey(10) == 13 :
                break

    cv2.destroyAllWindows()
    cap.release()
except:
    cap.release()
    cv2.destroyAllWindows()