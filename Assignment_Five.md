# Question 1

Write a function that opens a file reads the contents of the file into memory and then closes the file.  It should return the contents.

# Question 2

Write a function that opens a file, appends some text at you passed in and then closes the file.

# Question 3

For this question we are going to start learning libraries in Python.  The os module comes in handy for lots of things.

To use it do the following:

`import os`

I want you to use the os module to traverse your entire file system, starting at `~` (your home directory).  You'll write a function to do this, and append every filename to a list, with it's absolute path.  The os module has all the function's you'll need.  Note:  You cannot use `os.walk`.  You'll need to use recursion for this code to be compact.

How this function should work:

traverse_file_system() -> returns list of files

# Question 4

Now we are going to write a line counting function!

You are going to use the traversal method you wrote in the last question to first traverse the file system for all your python files (files ending in `.py`).  Then you'll need to write a second method that loops through the list you get back from the first function, filter for python files in some way (this can be done during this loop or before) and then open the file, count the number of lines, close the file and move on.

# Question 5

Now that we can traverse our file system, we are going to learn how to work with web pages.  In this question you'll be scraping the web.  We'll be scraping https://www.python.org/ 

For this we'll be using the `requests` module.  This module, is awesome.

Use requests to download the python.org homepage and save it to a file.  Your function shouldn't return anything.

# Question 6

Write a method that uses requests and downloads all the links from https://www.python.org/ (homepage only) and saves them to a list.  Return the list.

# Question 7

Write a new version of the above function that takes in any page and downloads all the links from the page.  You should return the set of links. Use lxml to do this.  The xpath part of the library is your friend here.

# Question 8

Write a second method that traverses all the webpages on the website (using the requests module) and then uses the funtion you wrote in question 7 to get more webpages to traverse.  These methods should be recursive in nature.  

# Question 9

Write a function that takes the output of the method in question 8 and prunes any repeat urls.

# Question 10

Write a function that verifies a url is correct (actually goes to a page).

