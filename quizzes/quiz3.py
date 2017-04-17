#Question 1

#Write a method to open a file and read its contents.  Return total numbe of lines in the file.

def line_count(filename):
    with open(filename,"r") as f:
        return len(f.read().split("\n"))

#Question 2

#Write a recursive method to traverse a file system.  Assume you start at "~" always.
import os

def filesystem_traverse(folder):
    files_and_folders = [os.path.abspath(elem) for elem in os.listdir()]
    for file_obj in files_and_folders:
        if os.path.isdir(file_obj):
            filesystem_traverse(file_obj)
    
#Question 3

def count_lines(folder,total_lines):
    files_and_folders = [os.path.abspath(elem) for elem in os.listdir()]x
    for file_obj in files_and_folders:
        if os.path.isdir(file_obj):
            total_lines += count_lines(file_obj)
        else:
            if file_obj.endswith(".py"):
                total_lines += line_count(file_obj)
    return total_lines

count_lines("~",0)
