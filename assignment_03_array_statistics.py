# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
Size = int (input("Enter your Array size"))

Numbers = [0] * Size

for i in range(Size):
    Numbers[i] = int(input(f"Enter number {i + 1}: "))
    
    
def Summation(Numbers):
        Total = 0
        for i in range(len(Numbers)):  
            Total = Total + Numbers[i]
        return Total   
    
result = Summation(Numbers)
print(f"Sum: {result}")     




def Mean(Numbers):
    Average = result / Size
    print(f"Average: {Average}")
    
Mean(Numbers)


def Maxi(Numbers):
    Biggest = Numbers [0]
    for i in range(len(Numbers)):
       if  Numbers[i] > Biggest: 
           Biggest = Numbers[i]
    return Biggest

Maximun = Maxi(Numbers)
print(f"Maximum: {Maximun}")     



def Mini(Numbers):
    Smallest = Numbers[0]
    for i in range(len(Numbers)): 
        if Numbers[i] < Smallest:
            Smallest = Numbers[i]
            
            
    return Smallest 

Minimum = Mini(Numbers)
print (f"Minimum: {Minimum}")          
        
# =============================================================================

