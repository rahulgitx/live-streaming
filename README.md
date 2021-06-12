# live-streaming
Live streaming video from one server to another with TCP on python
In this code I used my phone camera as an external camera as I tested the codes on the same computer using two different codes running on two different ports. The port for the server is specified by us while the port for the client will be automatically created.
### How to use phone camera as an external webcam.
* First download the app IP webcam on your phone from google playstore or this [link](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN&gl=US)
* On the home page, go to the bottom and tap on start server.
* Your camera will be opened and an IP address along with the port will be displayed.
* Open your web browser and go to that IP address.
* It will give a warning of IP being unsecure, just go to the advance settings and proceed.
* On the fron screen you will see Video renderer written with multiple tab options. Click on Javascript and you'll start seeing you're phone camera's input on your browser screen.
* In your python code use 

```
import cv2
cap = cv2.VideoCapture(1)
address='https://your_hotspot_ip:8080/video'
cap.open(address)
```
* You can now use this cap variable to view image or videos in you python code.

### Server.py
* Although I've described most of the steps along with the code but let me give you an overview what this file will be doing.
* First, it will be creating a TCP socket of the local host IP address and a port of our choice.
* It will bind this onto the socket and wait for the client to connect.
* After making a connection further steps will be proceeded.
* Now as we know that video is just a continuous stream of images we create a while loop that will run infinitely sending and receiving image data.
* Both the sending part of the code and receiving part of the code runs one after the other sending and receiving data once during the loop which creates a simultaneous scenario for both sending and receiving the images.
* Maximum size of a TCP packet is enough to send the whole image data once so there is no need to break the image into pieces.  

### Client.py
* In client.py too we first created a socket and in the connect function gave the IP address of the server. 
* Now, as I used mobile camera as an external webcam a few code of lines from "How to use phone camera as an external webcam" are added.
* We received and send the image data in the same as in the client by running both process' loop inside the infinite while loop.

Run Server.py function first as the client would obviosly first need a server to connect to.

After the streaming is done just press "Enter" and the window which is selected will close along with the socket. The other one will act strange as the program is no longer connected to other program's socket. This part is on improvement. Thank you.
