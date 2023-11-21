from sys import setrecursionlimit # package to set a the recursion limit

'''
Fibonacci implementation 
'''
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

'''
Dinamic implementation of fibonacci
'''
def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        
        result = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
        memo[n] = result
        return result
        
if __name__ == '__main__':
    setrecursionlimit(10002)
    n = int(input('Type a number to generate fibonacci numbers: '))
    
    result = fibonacci_dinamico(n)
    print (result)