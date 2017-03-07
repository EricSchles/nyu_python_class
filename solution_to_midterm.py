#Question 1

def hello_world():
    print("Hello World!")

#Question 2
def greeting(name):
    print("Hello "+str(name))

name = str(input("What is your name"))
hello(name)

#Question 3
def age_plus_10(age):
    return age + 10

#Question 4
import datetime
def age_plus_10(age,birthday):
    """
    inputs:
    @age - an integer
    @birthday - a datetime object
    """
    today = datetime.today()
    ten_years_from_now = datetime.today()
    ten_years_from_now.year += 10
    
    if today.month > birthday.month:
        return age + 10
    else:
        return age + 9

#Question 5

def initialize(firstname,lastname):
    first_initial = firstname.upper()
    first_initial = first_initial[0]
    last_initial = lastname.upper()
    last_initial = last_initial[0]
    return first_initial+"."last_initial+"."

#Question 6

def wage_adjusted():
    current_wage = float(input("what is your current wage?"))
    for i in range(10):
        current_wage *= 1.04
    return current_wage

#Question 7

def weighted_average(numbers,weights):
    summation = 0
    for index,value in enumerate(numbers):
        summation += value*weights[index]
    return summation/float(len(numbers))

#Question 8
import statistics
import math

def kurtosis(listing):
    ave = sum(listing)/float(len(listing))
    numerator = 0
    denominator = 0
    for elem in listing:
        numerator += elem - ave
        denominator += math.pow(elem - ave, 2)
    return len(listing) * (float(numerator) / math.pow(denominator, 2))

#Question 9

def skew(listing):
    ave = sum(listing)/float(len(listing))
    numerator = 0
    denominator = 0
    for elem in listing:
        numerator += math.pow(elem - ave, 3)
        denominator += math.pow(elem - ave, 2)
    return math.pow(len(listing), 0.5) * (float(numerator) / math.pow(denominator, 1.5))

#Question 10
def maximum(listing):
    max_elem = 0
    for elem in listing:
        if elem > max_elem:
            max_elem = elem
    return max_elem

#Question 11
def minimum(listing):
    min_elem = 999999999999
    for elem in listing:
        if elem < min_elem:
            min_elem = elem
    return min_elem

#question 12
def next_largest(listing):
    listing.sort()
    return listing[-2]

def next_largest(listing):
    max_elem = 0
    for elem in listing:
        if elem > max_elem:
            max_elem = elem
            
    second_biggest = 0
    for elem in listing:
        if elem > second_biggest and elem != max_elem:
            second_biggest = elem
    return second_biggest

#question 13
class Trapezoid:
    def __init__(self, point_1, point_2, point_3, point_4):
        """
        Each of these points is a tuple
        """
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.point_4 = point_4

    def area(self):
        """
        A and D are on the same plane,
        B and C are on the same plane.
        """
        if self.point_1[1] == self.point_2[1]:
            A = self.point_1 
            D = self.point_2
            B = self.point_3
            C = self.point_4
        elif self.point_1[1] == self.point3[1] :
            A = self.point_1
            D = self.point_3
            B = self.point_2
            C = self.point_4
        else:
            A = self.point_1
            D = self.point_4
            B = self.point_2
            C = self.point_3
        
        base_1 = A[0] + D[0]
        base_2 = B[0] + C[0]
        if C[1] > D[1]:
            height = C[1] - D[1]
        else:
            height = D[1] - C[1]
        return height * ((base_1 + base_2)/2)

    def perimeter(self):
        if self.point_1[1] == self.point_2[1]:
            A = self.point_1 
            D = self.point_2
            B = self.point_3
            C = self.point_4
        elif self.point_1[1] == self.point3[1] :
            A = self.point_1
            D = self.point_3
            B = self.point_2
            C = self.point_4
        else:
            A = self.point_1
            D = self.point_4
            B = self.point_2
            C = self.point_3
        summation = 0
        summation += self._distance(A,B)
        summation += self._distance(B,C)
        summation += self._distance(C,D)
        summation += self._distance(D,A)
        return summation
    
    def _distance(self,point_one,point_two):
        internal = math.pow(point_two[1] - point_one[1], 2) + math.pow(point_two[0] - point_one[0], 2)
        return math.pow(internal, 0.5)

#Question 16

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def append(self,value):
        if not self.head.data:
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            new_node = Node(value)
            cur.next = new_node
            new_node.prev = cur
            
