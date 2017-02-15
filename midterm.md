#Question 1

Write a method that prints "Hello World!"

#Question 2

Write a method that takes expects a variable called name, and prints Hello + [NAME]

Example:

greeting("Eric") -> returns "Hello, Eric"

#Question 3

Write a method that asks a user how old they are and then prints out how old they will be in 10 ten years. 
Hint - this is not as simple as adding ten years to their current age, you need to figure out the current date and how old they will be in 10 years, exactly.  Assume their birthday was today

#Question 4

This question will be the same as question 3, except now we ask for their birthday and figure out how old they will be ten years from today.

So you need to ask for their birthday, you need to figure out how old they are now and then you need to figure out how old they will be 10 years from today.

#Question 5

Write a method where a user will provide their first name and last name, and you'll return their initials, captialized, with periods inbetween

#Question 6

Write a method that asks a user how much they make today and returns how much they'll make in 10 years, assuming their wages keep up with inflation and inflation is set at 4%.

#Question 7

Write a method that calculates the weighted average of a list of numbers.  The method should expect two lists, the numbers and their weights.  

#Question 8

Write a method that calculates the kurtosis of a a list of numbers.

#Question 9

Write a method that calculates the skew of a list of numbers.

#Question 10

Write a method that finds the maximum of a list of numbers (you cannot use the bultin method)

#Question 11

Write a method that finds the minimum of the list of numbers (you cannot use the builtin method)

#Question 12

Write a method that finds the second largest number of a list of numbers

#Question 13

Write a class called trapezoid that takes in 4 points and methods that calculate the area and perimeter of a trapezoid.

#Question 14

Write a class called hexagon that takes in 6 points and methods that calculate the area and the perimeter of a hexagon.

#Question 15

Write a class called polygon that takes in a number of points.  You should record the number of points included as an internal variable.  Use this to calculate the area and perimeter for the polygon.

#Question 16

Write a doubly linked list class.  It should include insert, delete, contains methods.  In a doubly linked list each element is connected in both directions to the node before and after it.

Here is the node class for such a linked list:

```
class Node:
	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

	def __str__(self):
		return repr(self.data)
```

#Question 17

Write a method that makes use of the doubly linked list to store the first 1000 numbers in the insert method.  Record how long this takes with time.time() like so:

```
start = time.time()
# running code goes here
print(time.time() - start)
```

#Question 18

Write a method that makes use of a builtin list and store the first 1000 numbers in it.  Record how long it takes with time.time() as before.

#Question 19

Which object stores the information faster?  Your linked list or the builtin?  Run the above code 100 times and record the average, standard deviation and median of the running of both (you should have code that shows this).  For this example you can use the statistics module.  To use it call `import statistics`.  

The `statistics` module has methods for mean, median and standard deviation. Makes use of these to record your analysis.

What do these descriptive statistics tell you about the running time of both methods? 

Make an inference as to why the code worked as it did.

#Question 20

Write a method called `analysis` that takes in a list of numbers and prints the mean, median, mode, standard deviation and variance.  

You can make use of `statistics` to do this. 

#Question 21

Write a method that calculates the nth fibonacci number.

Fibonacci numbers are of the form

fib(N) = fib(N-1) + fib(N-2) 

So the nth fibonacci number is a summation of the previous two numbers.