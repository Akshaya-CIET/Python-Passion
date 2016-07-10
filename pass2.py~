'''22. Write a function that validates the password. It should be 6-8 characters long. It consists of 
alphanumeric characters with a mixture of digits and letters.'''


def validpass(pass1):
    l=len(pass1)
    if (6<=l<8):
        print "Length good enough"
        for i in range(0,l-1):
            if pass1[i].isalnum():
                d=1
                i=i+1
            else:
            	d=0
        a=1
    else:
    	print "Length is not enough"
    	a=0
    if d==1 and a==1:
            print "The password is valid"
        else:
        	print "The password is not valid"
p=raw_input("Enter password")
validpass(p)
