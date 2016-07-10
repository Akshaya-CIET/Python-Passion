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
print len(list)
print "Last item in list"
print list[-1]
print "Reversed list: "
print list[::-1]
print "The list contains a 5 ?:"
if list.count(5)==0:
    print "No"
else:
    print "Yes"
print "Number of fives in list:"
print list.count(5)
print "Removed first element"
list.remove(list[0])
print "Removed last element"
list.remove(list[-1])
print "Sorted list"
list.sort()
print list
