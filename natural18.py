'''18. The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 âˆ’ 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum. '''

s=0#to find sum of num
ss=0#to find sum of squares
for i in range(0,101):
	s+=i
for i in range(0,101):
	i=i*i #find square of i
	ss=ss+i#sum up squares of i
print "Sum of squares:",ss,"Square of sum:",s*s
print "Difference between sum of squares and square of sum:",ss-s
