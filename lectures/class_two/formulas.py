import statistics

def func_one(listing):
    summation = 0
    for i in listing:
        summation += i
    return summation

#0+x=x
def func_two(list_one,list_two):
    summation = 0
    for i in list_one:
        for j in list_two:
            summation += i*j
    return summation

#1*x = x
def func_three(listing):
    product = 1
    for i in listing:
        product *= i
    return product


def func_four(list_one,list_two,list_three):
    accumulation = 0
    for i in list_one:
        product = 1
        for j in list_two:
            summation = 0
            for k in list_three:
                summation += statistics.mean([i,j,k])
            product *= summation
        accumulation += product
    return accumulation

def func_five(list_one,list_two):
    summation = 0
    for x in list_one:
        for y in list_two:
            summation += x+y
    product = 1
    for x in list_one:
        product *= x
    return summation / float(product)
    
def average(listing):
    summation = 0
    for i in listing:
        summation += i
    n = float(len(listing))
    return summation / n
