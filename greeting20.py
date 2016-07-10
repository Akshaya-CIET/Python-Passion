'''20. greeting = "Hello Google!" number of character in greeting stored in the variable 
'number_of_char' and repeat the greetings based on the number of character in 'greeting'''


greeting="hello world!"			#given string
number_of_chars=len(greeting)		#length of string greeting
print "Greeting:",greeting,"\nLength of greeting:",number_of_chars
greetings=greeting*number_of_chars	#appending greeting length times
print "Greetings:",greetings
