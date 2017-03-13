def fib(x):
    if x < 0:
        return "fibonacci numbers are strictly non-negative"
    #base cases first (this is how our function terminates)
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        #recursive case (this how our function iterates)
        return fib(x-1) + fib(x-2)

