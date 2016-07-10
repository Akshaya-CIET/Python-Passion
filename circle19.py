'''19. write a program ( in any programming language ) to Compute the area and perimeter of a 
circle with radius 3 using function .[Given pi= 3.14, Area= pi*(r*r) , perimeter= 2*pi*r]'''

global pi #pi,r needs to be used everywhere
pi=3.14
global r
r=3
def area(): #global r need not be given if the value is only accessed and not changed
	a=r*r*pi
	return a

def perimeter():
    p=2*pi*r
    return p

print "Circle's radius:",r
print "The area is:",area()
print "The perimeter is:",perimeter()
