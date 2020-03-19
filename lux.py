import commands
status_temp,temp_reg=commands.getstatusoutput('i2cget -f -y 1 0x40 0x03')
status_humd,humd_reg=commands.getstatusoutput('i2cget -f -y 1 0x40 0x05')
print ("Register temp:",temp_reg)
print ("Register humd:",humd_reg)
temp_int = int(temp_reg,16)
humd_int = int(humd_reg,16)
 
temp = (temp_int<<8)|temp_int
humd = (humd_int<<8)|humd_int
T=-46.85 + 175.72/65536*temp
RH=-6.0+125.0/65536*humd
print ("Current Temperature=",T)
print ("Relative Humidity=",RH)
