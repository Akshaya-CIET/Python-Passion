'''4. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.
'''

year=input("Enter the year to be checked")
if year%4==0 and year%100!=0 or year%400==0:	#leap year is divisible by 4 and not divisible by 100 or is divisible by 400
    print "It is a leap year"
else:
    print "It is not a leap year"
