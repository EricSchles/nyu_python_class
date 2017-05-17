import math
import statistics as st


class DescribeData:
    def __init__(self, List): #stands for initialize
        self.List = List

    def describe(self):
        print("Here are some statistics about our data")
        print("---------------------------------------")
        print("Our list has ",len(self.List),"many elements")
        print("The mean is ",self.average()) #automatic type casting to string
        print("The median is ",self.median())
        if self.average() > self.median():
            print("And the mean is ",abs(self.average()-self.median()),"greater than the median")
    
    def average(self):
        return st.mean(self.List)

    def median(self):
        return st.median(self.List)

    def standard_deviation(self):
        return st.stdev(self.List)
        

def describe(List):
    ave = st.mean(List)
    middle_number = st.median(List)
    std_dev = st.stdev(List)

    print("Here are some statistics about our data")
    print("---------------------------------------")
    print("Our list has ",len(List),"many elements")
    print("The mean is ",ave) #automatic type casting to string
    print("The median is ",middle_number)
    if ave > middle_number:
        print("And the mean is ",abs(ave-middle_number),"greater than the median")
    
if __name__ == '__main__':
    import random
    List = []
    for i in range(200):
        List.append(random.randint(0,100))
    describer = DescribeData(List)
    import code
    code.interact(local=locals())
