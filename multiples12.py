'''12.If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 
6 and 9. The sum of these multiples is 23. write a program to find the sum of all the 
multiples of 3 or 5 below 1000.'''

a=xrange(1,1000)
sum=0
print "Numbers divisible by 3 or 5 below 1000"
for i in a:
	#to check divisibility of numbers
	if i%3==0 or i%5==0:
		print i
		sum=sum+i#summing up the numbers
print "Sum of the numbers:",sum


     
