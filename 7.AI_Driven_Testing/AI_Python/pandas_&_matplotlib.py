
''' in-build python packages are --> math, statistics, random
from math import cos, sin, pi, floor
from statistics import mean, stdev, median
from random import sample
[https://docs.python.org/3/library/random.html]
'''

''' user defined python packages are --> pandas, numby, matplotlib.plotpy
import pandas as pd
[https://pandas.pydata.org/]
import matplotlib.pyplot as plt
[https://matplotlib.org/]
'''

# Dataset adapted from here https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho
#data = pd.read_csv('car_data.csv')
#print(data)

# Code to show only the cars with a price >= 10000
   #print(data[data["Price"]>=10000])

# Show all the cars from the 2015
   #print(data[data["Year"]==2015])

#  median selling value for the cars from 2015. Here's the code:
    #filtered_data = data[data["Year"]==2015]
    #print(filtered_data["Price"].median())

# Plotting data with matplotlib
'''
plt.scatter(data["Kilometer"], data["Price"], color='red')
plt.title('Car Price vs. Kilometers Driven', fontsize=16)
plt.xlabel('Kilometers Driven')
plt.ylabel('Price (in USD)')

# Add the grid
plt.grid(True)

# Display the plot
plt.show()
'''

# Exercise 1 : Write code to create a filtered table of all the Honda Accords in the dataset.
    #print(data[data["Model"].str.contains('Honda', na=False)])

# Exercise 2 : Write code to display a scatter plot of sales price vs year.
'''
plt.scatter(data["Price"], data["Year"], color='green')
plt.title('Sale Price vs. Year of Sale', fontsize=16)
plt.xlabel('Sale Price (in USD)')
plt.ylabel('Year of Sale')

# Add the grid
plt.grid(False)

# Display the plot
plt.show()
'''

# Challenge exercise : Ask the LLM to help you create a pie chart of the data showing
# how many cars were sold each year.

'''
# WRITE YOUR CODE HERE
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for illustration
data = pd.DataFrame({
    'Year': [2010, 2010, 2011, 2011, 2011, 2012],
    'Price': [20000, 25000, 18000, 24000, 23000, 26500],
})

# Group by 'Year' and count the occurrences
yearly_sales = data['Year'].value_counts()

# Plot the pie chart
plt.pie(yearly_sales, labels=yearly_sales.index, autopct='%1.1f%%')
plt.title('Percentage of Cars Sold Each Year')
plt.show()
'''
print("-----------------------------------------------------------------")

'''
code with actual count
import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame
data = pd.DataFrame({
    'Model': [
        'Honda Amaze 1.2 VX i-VTEC', 'Honda Brio V MT', 'Honda WR-V VX MT Petrol',
        'Honda CR-V 2.4 AT', 'Honda Brio S MT', 'Honda Accord 2.4 iVtec AT',
        'Honda City SV Diesel', 'Honda City V', 'Honda City SV CVT', 'Honda City V'],
    'Price': [5050.00, 3510.00, 8199.99, 8600.00, 4400.00, 1950.00, 7500.00, 7300.00, 5900.00, 4800.00],
    'Year': [2017, 2014, 2018, 2013, 2016, 2008, 2018, 2016, 2015, 2015],
    'Kilometer': [87150, 39276, 27963, 67000, 50374, 57885, 75000, 51834, 116592, 49000]
})

# Grouping by 'Year' to get the count of sales each year
yearly_sales = data['Year'].value_counts()

# Plotting the pie chart
plt.pie(yearly_sales, labels=yearly_sales.index, autopct=lambda p: '{:.0f}'.format(p * yearly_sales.sum() / 100))
plt.title('Number of Cars Sold Each Year')
plt.show()
'''