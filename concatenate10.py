'''10. Given a string s, return a string made of the first 2 and the last 2 chars of the 
original string,  so 'spring' yields 'spng'. However, if the string length is less than 2, return 
instead the empty string.'''

str1=raw_input("Enter the string:")
l=len(str1)
#function to check len and then form new string
def fun1(l,str1):
	if l<=2:
		return "NULL"
	else:
		s1=str1[0]+str1[1]+str1[-2]+str1[-1]
		return s1
s2=fun1(l,str1) #function call
print "The string formed:",s2
