'''16.The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all
the primes below two million.
'''


# number to find summation of all primes below number
no = 2000000

# create a set excluding even numbers
numbers = set(xrange(3, no + 1, 2)) 

for number in xrange(3, int(no ** 0.5) + 1):
    if number not in numbers:
        #number must have been removed because it has a prime factor
        continue

    num = number
    while num < no:
        num += number
        if num in numbers:
            # Remove multiples of prime found
            numbers.remove(num)

print 2 + sum(numbers)
