#Question 1

import math

def correlation(x,y):
    """
    @x - is assumed to be a list of numbers
    @y - is assumed to be a list of numbers
    it's assuemd the length of x and y are the same
    """
    N = len(x)
    mulitplications_of_xy = []
    for index in range(len(x)):
        multiplications_of_xy.append(x[index]*y[index])
    sum_of_xy = sum(mulitplications_of_xy)
    sum_x = sum(x)
    sum_y = sum(y)
    numerator = N*sum_of_xy - (sum_x * sum_y)

    square_x = []
    for value in x:
        square_x.append(math.pow(value, 2))
    sum_squared_x = math.pow(sum(x), 2)
    square_y = []
    for value in y:
        square_y.append(math.pow(value, 2))
    sum_squared_y = math.pow(sum(y), 2)
    denominator = math.pow((N*square_x - sum_squared_x) * (N*square_y - sum_squared_y), 2)
    return float(numerator) / denominator


#Question 2

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return repr(self.data)

#Question 3
class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def insert(self, value):
        if self.head.data != None:
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(value)

    def contains(self, value):
        if self.head.data == value:
            return True
        else:
            cur = self.head
            while cur:
                if cur.data == value:
                    return True
                cur = cur.next
            return False
        
    def deletion(self, index_to_delete):
        if index_to_delete == 0:
            if self.head.next:
                cur = self.head
                self.head = cur.next
            else:
                self.head = Node(None)
        else:
            count = 0
            cur = self.head
            while cur.next:
                count += 1
                cur = cur.next
            
            if index_to_delete > count:
                print("index out of range")
                return
            if count == index_to_delete:
                cur = self.head
                while cur.next:
                    cur = cur.next
                cur.next = None
            
            cur = self.head
            counter = 0
            while counter+1 != index_to_delete:
                cur = cur.next
                counter += 1
            new_next = cur.next.next 
            to_delete = cur.next 
            cur.next = new_next
            to_delete = None


#Question 4

#Given x = [1,2,3,4,5,6,7]
assert x[0] == 1
assert x[-1] == 7
assert x[:3] == [1,2,3]
assert x[:] == [1,2,3,4,5,6,7]
# x[:27] raises an error

#Question 5

def multiplication(x,y):
    result = 1
    for _ in range(y):
        result += x
    return result

#Question 6

#read x/y
def division(x,y):
    result = x
    count = 0
    while result >= 0:
        result -= y
        count += 1
    return count

#Question 7

class Triangle:
    def __init__(self, point_one, point_two, point_three):
        self.point_one = point_one
        self.point_two = point_two
        self.point_three = point_three

    def _length(self,a,b):
        return math.pow(math.pow(b[1] - a[1], 2),math.pow(b[0]- a[0], 2), 0.5)
    # source of calculation - http://www.mathwarehouse.com/geometry/triangles/area/herons-formula-triangle-area.php

    def area(self):
        length_one = self._length(self.point_one, self.point_two)
        length_two = self._length(self.point_two, self.point_three)
        length_three = self._length(self.point_three, self.point_one)
        S = (length_one + length_two + length_three)/2.0
        return math.pow(S*(S-length_one)*(S-length_two)*(S-length_three),0.5)
    
    def perimeter(self):
        length_one = self._length(self.point_one, self.point_two)
        length_two = self._length(self.point_two, self.point_three)
        length_three = self._length(self.point_three, self.point_one)
        return length_one + length_two + length_three
    
#Question 8
class Circle:
    def __init__(self, point, radius):
        self.point = point
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def perimeter(self):
        return math.pi * self.radius * 2.0
    
#Question 9

import time

start = time.time()
linked = LinkedList()
for i in range(10000):
    linked.insert(i)
print("insert time for linkedlist")
print(time.time() - start)

start = time.time()
listing = []
for i in range(10000):
    listing.append(i)
print("insert time for python list")
print(time.time() - start)

start = time.time()
listing.remove(random.randint(0,len(listing)))
print("delete time for python list")
print(time.time() - start)

start = time.time()
linked.deletion(random.randint(0,10000))
print("delete time for linkedlist")
print(time.time() - start)

start = time.time()
listing.count(random.randint(0,10000))
print("contains method for python list")
print(time.time() - start)

start = time.time()
linked.contains(random.randint(0,10000))
print("contains method for linked list")
print(time.time() - start)

#Question 10
def fib(x):
    if n == 2:
        return 1
    if n == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

