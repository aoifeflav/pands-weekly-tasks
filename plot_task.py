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

#set variables
mean = 5
std_dev = 2

#generate numbers
hist_data = np.random.normal(loc=mean, scale=std_dev, size=1000)

#Plot histogram, set colour, edges, bins and transparency
plt.hist(hist_data, color='#C9E4DE', bins=40, edgecolor='black')

#add labels
plt.xlabel('X', fontsize=12, fontweight='bold')
plt.ylabel('Frequency', fontsize=12, fontweight='bold')
plt.title('Standard Distribution of Data and $y = x^3$ Function', fontsize=14, fontweight='bold')

#Remove top and right side spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Change the background colour
plt.gca().set_facecolor('#F7F7F7')

#set up the function
xpoints = np.array(range(0,10))
ypoints = (xpoints * xpoints) * xpoints

#plot the function and style it
plt.plot(xpoints, ypoints, color='orange', linewidth=2, label='$y = x^3$')
plt.legend()

#Adjust the Y axis
plt.ylim(0, 100)

plt.show()
