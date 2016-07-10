'''21. Write a program that reads an integer N (1 < N < 1000). This N is the number of output lines 
printed by this program.
Input
The input file contains an integer N. (Sample Input : 5)
sample output
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
***********'''

n=input("Enter number from between 1 and 1000:::")
if (1<n<1000):
    print "Entered valid input" 
    for i in range(1,n+2):
        if i!=n+1:
    	    print i,"\t",i*i,"\t",i*i*i
    	else:
    		print "***********************"
else:
    print "Enter a valid number between 1 and 1000"
