def fib_dp(x):
    fib_sequence = [0,1]
    for i in range(2,x+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[x]

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

import time

fib_timing = []
for i in range(3,40):
    start = time.time()
    fib(i)
    fib_timing.append(time.time()-start)
fib_dp_timing = []
for i in range(3,40):
    start = time.time()
    fib_dp(i)
    fib_dp_timing.append(time.time()-start)

import code
code.interact(local=locals())
