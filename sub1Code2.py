"""
PART-1: Design of the first sub-module 
The  Raspberry  Pi-1  here  receives  Ethernet  commands  as  inputs  through  an  Ethernet 
cable(Rj-45).  It  is  programmed  to  convert  the  commands  and  send  them  to  a  slave 
device(using Serial Communication) utilizing Pi-HAT. The Pi-HAT is fixed to 
Raspberry Pi-1 and using this the slave device receives the corresponding serial data 
to perform necessary actions as per the instructions. The Pi-HAT converts full duplex 
CMOS to full duplexRS422(4 wire) or half to duplex RS485(2 wire) using transceiver 
switching. It has the feature of adjustable controlling a transmitter/receiver via GPIO 
pin. 
   
The communication between PLC and Raspberry Pi-1 is setup by Socket 
programming.  The  PLC  acts  as  server  and  Raspberry  Pi-1  acts  as  client.  The  code 
used for server corresponds to code-1, similarly code-2 is used for Raspberry Pi-1. 
"""

#CODE 2

import time  
import serial   
import socket   
import RPi.GPIO as GPIO   
 
GPIO.setmode(GPIO.BOARD)  
GPIO.setwarnings(False)  
GPIO.setup(11,GPIO.OUT)  
 
#To establish serial connection   
ser = serial.Serial(port ='/dev/serial0', baudrate = 9600 , parity = serial.PARITY_NONE, stopbits =  
serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)  
temp=''   
while True:   
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    client.connect(('169.254.199.57',5005)) #Server IP adress  
    string = "Receiver is active"  
    msg = bytes(string,'utf-8')   
    client.send(msg)   
    from_server = client.recv(4096)   
    from_server = from_server.decode('utf-8')   
    if(from_server=='%#%#%#'):  
        client.close()   
        close1='%#%#%#'  
        close2=close1.encode('utf-8')   
        ser.write(close2)  
        ser.close()   
        break   
    else:   
        if(from_server=='onLed'):  
            GPIO.output(11,GPIO.HIGH)       #Testing the TTL output using Led 
        elif(from_server=='offLed'):   
            GPIO.output(11,GPIO.LOW)  
        from_server=from_server+'$' #'$' is just used to detect last byte of data  
        msgInBytes = from_server.encode('utf-8')   
        ser.write(msgInBytes) #sending serial data   
        mread=ser.read(1) #recieving from other side serially in bytes  
        temp=mread.decode('utf-8')   
        if(temp=='y'):   
            print('RECIEVED!')  
            continue   
        #time.sleep(0.13) 