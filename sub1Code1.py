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

#CODE 1

import socket   
 
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating server object of socket type  
serv.bind(('169.254.199.57',5005))  
serv.listen(999)  
string=''   
while True:   
    print("\n in loop ")   
    conn, addr = serv.accept() #accepts the connection from client   
    from_client = ''  
    data = conn.recv(4096) #max no.of bytes   
    data=data.decode('utf-8') #decoding the bytes information encoded in utf-8 uni-code   
    from_client += data   
    print (from_client)  
    choice=input("\n1)To Enter the command\n2)To exit\t") #Menu driven, user specific  
    if(choice=='1'):  
        string=input()   
        msg=bytes(string,'utf-8')#UTF-8variable width character encoding in Unicode  
        conn.send(msg)   
    elif(choice=='2'):  
        string = '%#%#%#'   # a random flag to understand the termination  
        msg=bytes(string,'utf-8')   
        conn.send(msg)   
        conn.close()   
        break   
    else:   
        print("invalid input")   
print ('client disconnected') 