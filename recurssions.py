

"""
def factorial_iterative(n):
    fac = 1
    for i in range (n):
        fac = fac * (i+1)
    return fac


print (" Enter a number ")
n = int(input ())
print ("Factorial of number via iterative approach=", factorial_iterative(n))"""

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n* factorial_recursive (n-1)

print("Enter a number")
c =int(input())
print(factorial_recursive(c))