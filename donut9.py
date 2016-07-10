'''9. Given an int count of a number of donuts, return a string of the form 'Number of 
donuts: <count>', where <count> is the number passed in. However, if the count is 10 or
more, then use the word 'many'  instead of the actual count. So donuts(5) returns
'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many' '''

def c1(no): 		#method to check the conditions
    if no<10:
        print "Number of donuts:",no
    else:
        print "Number of donuts: many"
    return;

n1=input("Enter the number of donuts:")
c1(n1)
