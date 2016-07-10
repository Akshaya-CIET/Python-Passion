'''23. Read two numbers M and N indefinitely. Calculate and write the sum of their factorial. Be 
carefull, because the result can have more than 15 digits.

Input
The input file contains many test cases. Each test case contains two integer 
numbers M (0 â‰¤ M â‰¤ 20) and N (0 â‰¤ N â‰¤ 20).
Sample Input
4 4 
0 0 
0 2
Sample Output
48
2
3'''

ch=1
while 1:				#executes any no of times
    if ch==1: 				#if the user wants to continue for the second time the block is executed
        m=input("Enter m:")
        n=input("Enter n:")
        def facto(i):			#user defined function
            if i==0:
                return 1		#fact of 0 is 1
            else:
                return i*facto(i-1)	#recursively calls facto()
        lm=facto(m)
        ln=facto(n)
        print "The factorial of ",m," is:",lm
        print "The factorial of ",n," is:",ln
        print "The sum of factorials:",lm+ln
    else:
        break
    ch=input("Do you want to continue ?[1-yes,0-no]")
