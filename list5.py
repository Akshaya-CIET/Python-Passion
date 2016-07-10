'''5. Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.'''

list=input("Enter the list elements:\n")
print "Number of elements in list"
print len(list)				#prints the length of the list
print "Last item in list"
print list[-1]				#list[-1] gives the last element of list
print "Reversed list: "
print list[::-1]			#prints the list in reverse
print "The list contains a 5 ?:"
if list.count(5)==0:			#checks whether the list has 5 as an element
    print "No"
else:
    print "Yes"
print "Number of fives in list:"
print list.count(5)			#counts the number of 5's in list
print "Removed first element"		#removes the first element
list.remove(list[0])
print "Removed last element"		#removes the last element 
list.remove(list[-1])
print "Sorted list"
list.sort()
print list				#prints the sorted list
