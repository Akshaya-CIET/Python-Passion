'''3. Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
 (a) If the temperature is less  than -273.15, print that the temperature is invalid because it is
below absolute zero.
 (b) If it is exactly -273.15, print that the temperature is absolute 0.
 (c) If the temperature is between -273.15 and 0, print that the temperature is below freezing.
 (d) If it is 0, print that the temperature is at the freezing point.
 (e) If it is between 0 and 100, print that the temperature is in the normal range.
 (f) If it is 100, print that the temperature is at the boiling point.
 (g) If it is above 100, print that the temperature is above the boiling point.'''


temp1=input("Enter temperature in celsius:")
temp=temp1+273.15  				#converts temperature to kelvin
print "Temperature in Kelvin"
print temp
if (temp<-273.15):				#checks the temperature value
    print "Temperature is invalid"
elif temp==-273.15:
    print "Temperature is absolute zero"
elif -273.15<temp<0:
    print "Temperature is below freezing point"
elif temp==0:
    print "Temperature is at the freezing point"
elif 0<temp<100:
    print "Temperature is in the normal range"
elif temp==100:
    print "Temperature is at the boiling point"
elif temp>100:
    print "Temperature above boiling point"
