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

#in order to get line I shouldn't be assigning points in a for loop
#instead I define x as being a list using np.arange and then use that directly in plt.plot
x = np.arange(4)
plt.plot(x, f(x)) #plot f(x), x=[0,1,2,3], y or f(x)=[0,1,2,3]
plt.plot(x, g(x)) #plot g(x), x=[0,1,2,3], y or g(x)=[0,1,4,9]
plt.plot(x, h(x)) #plot g(x), x=[0,1,2,3], y or h(x)=[0,1,8,27]

plt.show() #show the final plot