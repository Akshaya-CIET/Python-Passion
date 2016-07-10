'''8. Write a program rotates the elements of a list so that the element at the first index moves
to the second index, the element in the second index moves to the third index, etc., and the
element in the last index moves to the first index.
'''
				#to shift list[0] to list[1]
list=[1,2,3,4,5,6,7,8,9,10]
print "List before sifting:",list
				#rotate-user defined function
def rotate(l, y=1):
      if len(l) == 0:
          return l
      else:
          y = -y % len(l)     	# flip rotation direction
          return l[y:] + l[:y]

#function call
print rotate(list,1)

