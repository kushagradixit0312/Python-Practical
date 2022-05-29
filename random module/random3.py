import random
 
print("A random number from list is : ", end="")
print(random.choice([1, 4, 8, 10, 3]))
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
print("A random number from range is : ", end="")
print(random.randrange(20, 50, 3))
