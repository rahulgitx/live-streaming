
import socket
import pickle
import cv2

cap = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)                                    # creating socket
ip="127.0.0.1"                                                                          # own IP 
port=1234                                                                               # own port
socket_address = (ip,port)                                                                

try:
    s.bind((ip,port))                                                                  # binding port
    print("Binded")
    s.listen()                                                                         # waiting for client to connect
    print("LISTENING AT:",socket_address)

    o , addr = s.accept()
    print(o)
    print("Connected to {}".format(addr))
    while True:                                                                       # -----------sending part ------------
        ret , photo = cap.read()                                                      #
        ret, buffer = cv2.imencode('.jpg',photo)                                      #  compressing the .jpf file and storing it in the memory buffer that is resized to fit the result
        bytedata = pickle.dumps(buffer)                                               #  pickle serialises the object file. Serializing and saving it in bytedata
        o.send(bytedata)                                                              # sending to client                                                        
                                                                                      # --------------receiving part----------
        x = o.recv(1000000)                                                           # receiving bytes from the socket
  
        data = pickle.loads(x)                                                        # serializing back the deserialized data that was received in x.
        data = cv2.imdecode(data,cv2.IMREAD_COLOR)                                    # doing reverse of what is done in line 27. Uncompressing and getting the info from memory buffer
        if data is not None :
            cv2.imshow('serverphoto',data)
            if cv2.waitKey(10) == 13 :
                break

    cv2.destroyAllWindows()
    cap.release()
except:
    cap.release()
    cv2.destroyAllWindows()
