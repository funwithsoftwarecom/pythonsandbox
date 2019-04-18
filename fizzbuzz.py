'''
A very basic implementation of FizzBuzz

'''

for x in range(1,101):
    output = x
    
    #Determine if it is a multiple of 3
    if(x%3) == 0:
        output = "Fizz"
        
    #Determine if it is a multiple of 5
    if(x%5) == 0:
        output = "Buzz"
        
    #Determine if it is a multiple of both 3 and 5.
    if((x%3 == 0) and (x%5 == 0)):
        output = "FizzBuzz"
        
       
    
    print(output)
    