'''14. Write a code to remove duplicates in an array of numbers.
'''


a=raw_input("Enter the list:").split(',')
print "The list with duplicate elements:",a
#to remove the duplicate elements in the list
b=set(a)
print "The list with unique elements:",b
