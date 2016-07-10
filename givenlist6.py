'''6. Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
'''

list=[8,9,10] 				#declaring list
print "List before replacing"
list[1]=17 				#replacing 9 by 17
print list 				#print list
					#adding 4,5,6 to end of list
list.append(4)
list.append(5)
list.append(6)
					#removing first element from list
list.remove(list[0])
					#sorting the list
list.sort()
print "The sorted list is :",list
					#doubling the list
list=list+list
print "Doubled list :",list
					#replacing list[3] by 25
list[3]=25
					#final list
print list
