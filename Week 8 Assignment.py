#   Keith Ryan
#   Week 8 Assignment
#   plot three mathematical functions using matplot.pyplot: f(x), g(x) and h(x)
#   where f(x)=x, g(x)=x**2 and h(x)==x**3

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return(x)

def g(x):
    return(x**2)

def h(x):
    return(x**3)

#my first pass is just to loop through and print, will add matplot.pyplot next pass
for i in range(4):
    print(f(i))
    print(g(i))
    print(h(i))

#plot the results of the functions from 0 to 3
myPlot = plt.plot()
for i in range(4):
    plt.plot(f(i), i, 'g.')
    plt.plot(g(i), i, 'b.')
    plt.plot(h(i), i, 'r.')
    
#show the final plot
plt.show()