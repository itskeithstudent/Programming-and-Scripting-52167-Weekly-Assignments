#   Keith Ryan
#   Week 8 Assignment
#   plot three mathematical functions using matplot.pyplot: f(x), g(x) and h(x)
#   where f(x)=x, g(x)=x**2 and h(x)==x**3

import matplotlib.pyplot as plt
import numpy as np

#These functions aren't necessary, could direcly use x**2 and x**3 in plt.plot arguments for the y axis
#but i think declaring each of these as functions improves readability
#f(x) simply returns x
def f(x):
    return(x)

#g(x) returns x squared
def g(x):
    return(x**2)

#f(x) returns x cubed
def h(x):
    return(x**3)

#in order to get line I shouldn't be assigning points in a for loop
#instead I define x as being a list using np.arange and then use that directly in plt.plot
#x = np.linspace(4,1000) makes it seem as if f(x) and g(x) are same values, such is the difference in scale between g(x) and h(x)
#x = np.linspace(4,100) gives a distinction between f(x) and g(x) but not much
#logic below was largely taken from what was shown in this weeks 2nd lecture video
x = np.linspace(0,4,25) #linspace gives us 25 steps between 0 and 4

plt.figure("Figure Name") #add figure name, when initially added placed beside plt.title, but this has unintended effect of making a new plot
#plt.figure seems like handy way to make a new plot/multiple plots
#all plot's show on same axis
plt.plot(x, f(x), 'g.', linestyle='-', label="f(x)") #plot f(x), x=[0,1,2,3], y or f(x)=[0,1,2,3]
plt.plot(x, g(x), 'r.', linestyle='-', label="g(x)") #plot g(x), x=[0,1,2,3], y or g(x)=[0,1,4,9]
plt.plot(x, h(x), 'b.', linestyle='-', label="h(x)") #plot g(x), x=[0,1,2,3], y or h(x)=[0,1,8,27]

#took a look at available pyplot functions to add title x/y axis label and whatever else looked useful
plt.title("Week 8 Assignment: f(x), g(x), h(x)") #title for figure
plt.xlabel("X: Function Input") #x axis label
plt.ylabel("Y: Function Result") #y axis label
plt.legend() #handily the legend uses both the dot and linestlye
plt.show() #show the final plot


