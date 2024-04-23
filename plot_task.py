#plot_task.py
# Creates a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range 0 to 10
#Author: Aoife Flavin

#Import matplolib and numpy
#Use numpy to generate the 1000 values within the mean an standard deviation
# plot it

#import
import numpy as np
import matplotlib.pyplot as plt

#set up the functiom
xpoints = np.array(range(0,10))
ypoints = (xpoints * xpoints) * xpoints

#plot the function
plt.plot(xpoints, ypoints)
plt.show()