'''22. Write a function that validates the password. It should be 6-8 characters long. It consists of 
alphanumeric characters with a mixture of digits and letters.'''


#importing regular expression library
import re
p=raw_input("Enter the password:")
#searching for letters
t=re.search('[a-zA-Z]', p)
#searching for digits
n=re.search('[0-9]',p)
#length of password
l=len(p)
#checking the password length
if 6<=l<=8:
    print "The password length is good"
    #checking whether password contains digits and numbers
    if t and n:
        print "The password is valid"
    else:
        print "The password must have alphabets and numbers"
else:
    print "The password must be between 6 and 8"

