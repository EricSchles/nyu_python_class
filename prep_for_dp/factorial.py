def factorial(x):
    #base case
    if x == 0:
        return 1
    else:
        #recursive case
        return x * factorial(x-1)


