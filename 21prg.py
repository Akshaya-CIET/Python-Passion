'''A program that reads an integer N (1 < N < 1000). This N is the number of output lines 
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

n=input("Enter number from between 1 and 1000:::")          #to get number as input from the user
if (1<n<1000):                                              #checks whether the input is greater than 1 and less than 1000
    print "Entered valid input"                             #notifies user that the input is valid
    for i in range(1,n+2):                                  #loop to print the output, excutes till range lies between 1 and n+2
        if i!=n+1:                                          #checks whether i is equal to n+1
    	    print i,"\t",i*i,"\t",i*i*i                     #prints the values if i!=n+1
    	else:
    		print "***********************"                 #prints the line if i==n+1
else:
    print "Enter a valid number between 1 and 1000"         #notifies the user to enter a valid number
