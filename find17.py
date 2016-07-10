'''17. Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in
the second array.
'''

a=[1,2,3,4,5]
b=[2,3,1,0,5]
print "The given lists a:",a,"\nb:",b
a1=list(set(a)-set(b))			#returns no that is not in a
b2=list(set(b)-set(a))			#returns no that is not in b
print "The number not in a;",a1,"\nThe number not in b:",b2
