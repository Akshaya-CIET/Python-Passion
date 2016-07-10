'''16.The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all
the primes below two million.
'''


s=0
for num in xrange(1,2000000):
   # prime numbers are greater than 1
   if num > 1:
       for i in xrange(2,num):
       	#prime numbers are divisible by 1 and itself only
           if (num % i) == 0:
               break
       else:
           s=s+num

print "\nThe sum of prime numbers below 2000000:",s
