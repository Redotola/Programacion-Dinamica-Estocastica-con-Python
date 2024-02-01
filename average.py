'''
Variability: refers to the extent to which values in a dataset change or vary. It is a statistical property that provides information about the dispersion, spread, or diversity of values in a sample or population.

'''

import random
import math

def average(x):
    return sum(x) / len (x)

def variability(X):
    mu = average(X)
    accum = 0
    
    for x in X:
        accum += (x-mu)**2
    
    return accum / len(X)

def standard_deviation(X):
    return math.sqrt(variability(X))

if __name__ == '__main__':
    x = [random.randint(1,21) for _ in range(20)]
    mu = average(x)
    Var = variability(x)
    sigma = standard_deviation(x)

    print(f"Array x: {x}")
    print(f"Average: {mu}")
    print(f"Variability: {Var}")
    print(F"Standard Deviation: {sigma}")
    
    