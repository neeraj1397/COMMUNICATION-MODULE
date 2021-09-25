# COMMUNICATION-MODULE
A module should be designed that takes analog inputs from sensors, Ethernet  commands  from  PLC  and  produces  required  outputs  in  the  form  of  TTL  logic  for  former input and serial output for latter input. The proposed solution is realized using  Raspberry Pis as central parts of module which is equipped with other peripherals to  behave  as  a  complete  working  module.  The  module  is  intended  to  be  used  in  submarines to communicate between PLCs and antennas and also drive large relays in  response to sensor data.

# APPROACHES 
1. An  Arduino(Micro  controller)  based  solution  was  proposed  earlier.  It  has  some problems. Arduino boards don’t have Ethernet compatible port so it requires external Ethernet  shield.  In  order  to  get  the  serial  output(rs232/422)  the  smart  boards  have  to be  stacked  on  the  Arduino  which  requires  PHPOC  shield  to  be  attached  externally. This  makes  the  hardware  more  complex.  Even  after  completion  of  module(COTS), Arduino could not be compatible with further enhancements of the product.   
2. A  Raspberry  Pi(SoC)  based  solution.  It  has  a  built-in  Ethernet  port,  several  GPIO pins.  It(python)  has  also  got  huge  library  to  make  the  code  simple  and  efficient compared to the C/C++ based Arduino software. There are many serial output shields available that can be directly stacked upon the Raspberry Pi. Further, any modification in future could be easily made. These features made us to proceed with the Raspberry Pi based solution. 

# COMPONENTS USED 
The following are the components of the module designed: 
1. Raspberry Pi 3 Model B+ (2 Nos) 
2. MCP3208-Analog to Digital Converter 
3. Isolated RS485/RS422 Raspberry Pi HAT 
4. CMOS to TTL(TXS0108E) high speed full duplex 8 channel logic level converter 
