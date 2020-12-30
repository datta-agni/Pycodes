# Python program to find LCM of two numbers
 
# Recursive function to return gcd of a and b
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
# Function to return LCM of two numbers
def lcm(a,b):
    return (a / gcd(a,b))* b
 
# Driver program to test above function
a = int(input("ENTER THE 1st NUMBER")
b = int(input("ENTER THE 2nd NUMBER")
print('LCM of', a, 'and', b, 'is', lcm(a, b))
 