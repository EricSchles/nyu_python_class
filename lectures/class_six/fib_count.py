import plotly
from plotly.graph_objs import Bar,Layout,Scatter, Box, Annotation,Marker,Font,XAxis,YAxis 
import shutil

class FibCount:
    def __init__(self):
        self.count = 0
    def fib(self,n):
        if n == 0:
            self.count += 1
            return 0
        if n == 1:
            self.count += 1
            return 1
        else:
            self.count += 1
            return self.fib(n-1) + self.fib(n-2)

    def reset_count(self):
        self.count = 0

from functools import lru_cache
import time
@lru_cache(maxsize=1000)
def calculate():
    results = []
    fib_counter = FibCount()
    
    for i in range(30):
        start = time.time()
        fib_counter.fib(i)
        results.append(fib_counter.count)
        fib_counter.reset_count()
        print(i,"took",time.time() - start)
    return results

x_vals = list(range(30))
y_vals = calculate()

plotly.offline.plot({
    "data":[Scatter(x=x_vals,y=y_vals)],
    "layout":Layout(
        title="growth in operations of fibonacci"
    )
    },auto_open=False)

shutil.move("temp-plot.html","/Users/ericschles/Documents/projects/nyu_python_class/lectures/class_six/fibonacci_growth.html")     

