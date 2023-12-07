import sys
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

try:
    n = int(input("Write the number of factorial: "))
    sys.setrecursionlimit(n+2)
    print(factorial(n))
except Exception as e:
    print("Error: " + str(e))
    
