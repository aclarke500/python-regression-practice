import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'./Book1.csv', header=None) # import without cutting first row
# convert from data frame to list
data = pd.DataFrame(df).values.tolist()


x_values=[]
y_values=[]

# convert from list of list to 2 seperate lists
for d in data:
    x_values.append(d[0])
    y_values.append(d[1])

# estimate slop of 5 for starters
estimated_slope = 5

for k in range (10):
    # start regression line using first value
    y_intercept = y_values[0]
    regression_line_values =[]


    for i in range(len(y_values)):
        regression_line_values.append(estimated_slope*i+y_intercept)

    differences= []

    for i in range(len(y_values)):
        actual_value = y_values[i]
        estimated_value = regression_line_values[i]

        difference = (actual_value - estimated_value)
        differences.append(difference)

    average_difference = sum(differences)/len(differences)

    # if estimate was too high
    if average_difference < 0:
        estimated_slope /= 2






plot=plt.scatter(x_values, y_values, color="green")
plt.scatter(x_values, regression_line_values)

# to plot line
x = np.linspace(0, 50,1)
plt.plot(x, 5)
plt.show()