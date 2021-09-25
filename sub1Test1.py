"""
TESTING SUB-MODULE 1
To check the serial output at receiver’s end, the test Raspberry Pi is programmed with 
the following code: 
"""

#CODE 1

import time  
import serial   
ser=serial.Serial(port='/dev/serial0',baudrate=9600,parity=serial.PARITY_NONE,stopbits =  
serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = 1)  
)   
data2=''   
temp=''   
t2=''   
t1=''   
while 1:   
    data=ser.read() #reading from otherside serially in bytes   
    temp=data.decode('utf-8') #decoding into a string   
    if(temp=='$')  
        print(data2)   
        t1='y'   
        t2=t1.encode('utf-8')   
        sedr.write(t2) #sending feedback to mediator  
        continue   
    data2+=temp   
    if(data2=='%#%#%#')   
        print('connection is closed')   
        ser.close()   
        break  