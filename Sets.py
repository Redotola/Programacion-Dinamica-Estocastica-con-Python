import time

'''
Eliminate the no odd number of list in less of 1 second
'''
list1 = list(range(1,1000001)) # list of pair numbers
list2 = list(range(1,1000001, 2)) # list of odd numbers

inicio = time.time() # initial time of execution

set1 = set(list1) # create set of lists
set2 = set(list2)

set1 = set1.difference(set2) # separate odd numbers form pair numbers

fin = time.time()

print(f"Finished : {set1}")
print(fin-inicio)
