'''8. Write a program rotates the elements of a list so that the element at the first index moves
to the second index, the element in the second index moves to the third index, etc., and the
element in the last index moves to the first index.
'''


l=raw_input("Enter the list:")
#removing last element and inserting it front
l.insert(0,l.pop())
print "The list after rotating:",l
