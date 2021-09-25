"""
The  Raspberry  Pi-2  takes  analog  data  from  sensors  and  since  the  GPIOs  are  digital 
pins,  an  Analog  to  Digital  Converter(MCP  3208)  is  employed.  MCP3208  works 
through SPI protocol and hence it has high data transfer rate. To summarize,   
Raspberry Pi-2 is programmed to receive analog signals and respond accordingly. The 
code-3 corresponds to this function. 
"""

#CODE 1

import spidev 
import time 
import RPi.GPIO as GPIO 
 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup(11,GPIO.OUT) 
 
spi=spidev.SpiDev() 
spi.open(0,0)   
spi.max_speed_hz=1000000 
 
MAX_CH= 8 
adc_values = [0 for i in range(MAX_CH) ] 
 
 
def analog_read(ch): 
        if( (ch>MAX_CH-1) or (ch<0)): 
                return -1 
        r = spi.xfer2([1, (8+ch)<<4, 0]) 
        val = ((r[1]&3)<<8)+r[2] 
        return val         
                                                  
         
while True: 
  try: 
          time.sleep(0.1) 
          ch = 0 
          GPIO.output(11,GPIO.LOW)   
          #for ch in range(0,7): 
          adc_values[ch] = analog_read(ch) 
          if (adc_values[ch]>95): 
                        GPIO.output(11,GPIO.HIGH)       
          print(adc_values) 
          break 
  except KeyboardInterrupt: 
                break 
print("done") 