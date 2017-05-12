Question 1

Write a class that counts the number of times mergesort gets called when sorting various lengths of lists of numbers.  What can you infer about it's Big-O notation?  Is it Logarithmic, Linear, or Exponential?

Make use of the following implementation of mergesort in order to test this:

https://github.com/EricSchles/stanford_algo_class/blob/master/first_pass/merge_sort.py

Question 2

Do the same analysis as question 1, except with quicksort.

Use this implementation:

https://github.com/EricSchles/stanford_algo_class/blob/master/first_pass/random_quicksort.py

Question 3

Do the same thing as question 1, except with bubble sort.

Use this implementation:

```
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
```

Question 4

Do the same thing as question 1, except for appending elements to a binary search tree.

Use this implementation:

https://github.com/EricSchles/BinarySearchTree/blob/master/bst_pure.py

Question 5:

Given the algorithm:

def algo1(x):
	if x == 1:
		return 0
	if x == 2:
		return 1
	if x == 3:
		return 1
	else:
		return algo1(x-3) + algo1(x-2) * algo1(x-1)

What do you think the Big-O notation will be?  Write a class similar to question 1, wrapping this method.  Confirm your assumptions (or prove them wrong).  What is the actual Big-O notation for this algorithm?

Question 6:

import math
def algo2(x,y):
	if x == 1:
		return x+y
	else:
		return algo2(x-algo2(1,y),y-algo2(x,1)) * math.pow(algo2(x,y), 2)

Does algo2 always complete?  Can you think of any cases when it doesn't?  What other statement might ensure it always completes?

Question 7:

Finding a Cycles: 

In Linked Lists it's possible to get a cycle.  That's when an element creates a loop, so that the list points back to it's self and never finishes.  Here is an example of such a list:

```
class Node:
	def __init__(self,data,next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return repr(self.data)

head = Node(None)
cur = head

for i in range(3):
	cur.next = Node(i)
	cur = cur.next

point_of_loop = Node(4)
cur.next = point_of_loop
cur = head
cur = cur.next.next
point_of_loop.next = cur

cur = head
count = 0
while cur:
	print(cur)
	cur = cur.next
	count += 1
	if count == 1000:
		break
```

Clearly the list is only 4 elements long, yet it goes on forever!  Write a method that detects loops in a linked list.  Note: the internet is your friend here.  Research the solution.  In this case, it's fine to steal someone else's code (not from the class though).  The goal is to understand how to find loops in linked lists and what to do about them.

Question 8:

Write a method that flattens a binary search tree.  It should store all the elements of the tree in a linked list.

Question 9:

Write a method that compares if two binary search trees have the same structure (and elements).  

Question 10:

Write a method that inserts the 1st 1000 integers into a binary search tree in ascending order, so the first element inserted should be 0.  Then write another method that inserts the 1st 1000 integers into a binary search tree, in descending order, so the first element inserted should be 999.  Both methods should return the resulting trees.

Now write a method to inspect the structure of a binary search tree.  Compare the pictures of the two resultant trees.  Why do they look the way they look?



