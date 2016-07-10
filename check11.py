'''11.Given a list of strings, return the count of the number of strings where the string
length is 2 or more and the first and last chars of the string are the same.'''

ls=[]
ls=raw_input("Enter the list of strings:").split(',')
no=0
for i in ls:
	l=len(i)
	#checking first and last word 
	if l>=2 and i[0]==i[-1]:
		print i
		no=no+1
print "Number of strings with same last and first letters and length>=2 :\n Number:",no
