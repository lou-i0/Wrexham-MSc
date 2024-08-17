#Assignment 5.1.6 -  Create your own recursive code
#==================================================
'''
The goal of this code is to create a recursive algorithmic
script, calculating the nth term (Fn) term in the Fibonacci Sequence.
The code will accept a positive numerical input from the user and return an
output representing the nth term in the sequence.

The Fibonacci sequence formula is defined as Fn = (Fn-1) + (Fn-2) for all n >=2

'''
import sys						# imported sys to deal with recursion limit
#print(sys.getrecursionlimit()) # find out recursion limit currently sert 
sys.setrecursionlimit(3000)		

try:# Wrap code in a try except clause to deal with errors
    
    # Create an empty list ready to store values from fibonacci function code
    #---------------------------------------------------
    fib_list = []
    
    # Create function instance to contain computation
    #---------------------------------------------------
    def fib_seq(n):
        # as 1 is a base class, the value will be returned as 1
        #---------------------------------------------------
        if n == 0:
            n = 1 
        if n == 1:
            value = 1

        # When n from user is 2 or less, return 1 as mirrored in the initial start (base classes) of sequence
        #------------------------------------------------
        elif n == 2:
            #return print('As n is less then 2, the answer will be ',1)
            value = 1
        
        # Code reproducing nth term of fibonacci sequence
        #------------------------------------------------
        elif n > 2 :
            value =  fib_seq(n-1) + fib_seq(n-2)
        # this section loops back the fucntions searching for previous numbers in sequence combining them together
            
        # Return the value to user showing what value of nth would be in the fibonacci sequence
        return value
        
# Handle errors when input is not a valid whole number (integer)
#------------------------------------------------
except ValueError:
    print(' Only valid whole numbers are allowed, please try again.')
# Handle any other errors
#------------------------------------------------
except Exception as e:
    print('Something went wrong: ', str(e), '. Please try again')
    
# Asks users to enter number that will be used in function3
#------------------------------------------------
try:# Wrap code in a try except clause to deal with errors
    n = int(input('Please enter the numbered term in the sequence to search for: '))
    print('') # extra line to space between outputs

    # Present number selected back to user 
    #------------------------------------------------
    print('You have selected: ',n)

    # Make call to created function providing nth term in Fibonacci sequence
    #------------------------------------------------
    print('The value of nth term ', n,' of the Fibonacci Sequence is:', fib_seq(n))
    # Handle errors when input is not a valid whole number (integer)
    
#------------------------------------------------
except ValueError:
    print(' Only valid whole numbers are allowed, please try again.')


13