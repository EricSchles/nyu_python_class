import math
#Question 1
#Write a python function that greets a person with their name

#Solution 1:
def greeting(name):
    return "Hello,",name

def greeting_two(name):
    return "Hello, "+str(name)

def greeting_three(name):
    print("Hello, "+name)

#Question 2
#Write a python function implementing the arthematic mean

#Solution 2:
def mean(List):
    return sum(List)/float(len(List))

#Question 3:
#Write a python function implementing median

#Solution 3:
def median(List):
    if len(List) == 0:
        return None
    if len(List) == 1:
        return List[0]
    #assumes we have a list of semantically orderable elements (aka numbers)
    List.sort()
    index_of_a_middle_number = len(List)//2 #integer value in python 3
    if len(List) % 2 == 0:
        return mean([ List[index_of_a_middle_number-1], List[index_of_a_middle_number] ])
    else:
        return List[index_of_a_middle_number]

#Question 4

#Write a python function implementing the mode

#Solution 4:

def mode(List):
    unique_elements = set(List)
    dicter = {}
    for elem in unique_elements:
        dicter[elem] = List.count(elem)
    max_elem = unique_elements[0]
    max_count = 0
    for elem in unique_elements:
        if max_count < dicter[elem]:
            max_elem = elem
            max_count = dicter[elem]
    return max_elem

#Question 5

#Write a python function implementing the geometric mean
def geometric_mean(List):
    if len(List) == 0:
        return None
    if len(List) == 1:
        return List[0]
    product = 1
    for elem in List:
        product *= elem
    nth_root = 1/float(len(List))
    return math.pow(product,nth_root)

#Question 6

#Write a python function implementing the variance
def variance(List):
    if len(List) == 0:
        return None
    if len(List) == 1:
        return List[0]
    summation = 0
    for elem in List:
        summation += math.pow(elem,2)
    interim_value = summation / float(len(List))
    mean_of_list = mean(List)
    return interim_value - mean_of_list

#Question 7

#Write a python function implementing the standard deviation
def standard_deviation(List):
    return math.pow(abs(variance(List)), 0.5)

#Note I meant quartile, not quantile - everyone gets full credit
#Question 8

#Write a python function implementing a function that returns the first quantile of a set of numbers
def first_quartile(List):
    if len(List) >= 4:
        List.sort()
        if len(List) % 2 != 0:
            middle_number = median(List)
            return median(List[:List.index(middle_number)])
        else:
            middle_index = len(List)//2
            middle_number = List[middle_index]
            return median(List[:List.index(middle_number)])
    else:
        return None    

#Question 9
#Write a python function implementing a function that returns the first quantile of a set of numbers
def third_quartile(List):
    if len(List) >= 4:
        List.sort()
        if len(List) % 2 != 0:
            middle_number = median(List)
            return median(List[List.index(middle_number):])
        else:
            middle_index = len(List)//2
            middle_number = List[middle_index]
            return median(List[List.index(middle_number):])
    else:
        return None    

