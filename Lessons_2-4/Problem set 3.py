#Project 2 Lesson 3 
# machine learning, linear regression w/ gradient descent
import numpy as np
import pandas as pd
import scipy.stats
import csv

def compare_averages():
    df = pandas.read_csv(file) 
    Left = df[df['handedness'] == 'L']
    Right = df[df['handedness'] == 'R']
    # Preform welch's ttest (you need to have normal distribusion)
    result = scipy.stats.ttest_ind(Left['avg'], Right['avg'], equal_var = False)
    # confidence interval of 95%
    if result[1] <= .05:
        return (False, result)
    else: 
        return (True, result) 
 
# tests null hypothesis that 2 populations are the same
# for comparing non-parametric/non normal data
w,p = scipy.stats.shapiro(data)
# Mann Whitney U test
u,p = scipy.stats.mannwhitneyu(x,y)

#linear regression 
import statsmodels.api as sm 

# X is input data points and Y is output data points 
# add the intercept 
X = sm.add_constant(X)
model = sm.OLS(Y,X)
results = model.fit()
# intercept is added at the beginning of params 
intercept = results.params[0]
# include the rest of the values
params = results.params[1:]
return intercept, params
# intercept: 200 and parameters: [-4.44 0.91] means
# y = -4.44x1 + 0.91x2 + 200 

results.tvalues 

# coefficient of determination
# yi = data
# fi = predictions
# y* = average of data 
R^2 = 1 - (((yi - fi)**2).sum()) / (((yi - y*)**2).sum())

Top = ((data - predictions)**2).sum()
Bottom = ((data - np.mean(data))**2).sum()
r_squared = 1 - (Top / Bottom) 

## Problem Set 3.1
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv(data.csv)
rain = df[df['rain'] == 1]
no_rain = df[df['rain'] == 0]
hourly_rain = rain['ENTRIESn_hourly']
hourly_no_rain = no_rain['ENTRIESn_hourly']

## Problem Set 3.3
import scipy
import scipy.stats

np.mean(hourly_rain) 
np.mean(hourly_no_rain)
u,p = scipy.stats.mannwhitneyu(hourly_rain,hourly_no_rain)

## Problem Set 3.5
import statsmodels.api as sm

def linear_regression(features, values):
    features = sm.add_constant(features)
    model = sm.OLS(values,features)
    results = model.fit()
    intercept = results.params[0]
    params = results.params[1:]
    return intercept, params

def predictions(dataframe):
    features = dataframe[['Hour', 'meantempi']]
    # Delete dummy variable to make run faster 
    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    # Values
    values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
    intercept, params = linear_regression(features, values)

    predictions = intercept + np.dot(features, params)

    # Calculate R^2 value
    Top = ((values - predictions)**2).sum()
    Bottom = ((values - np.mean(values))**2).sum()
    r_squared = 1 - (Top / Bottom) 

    return r_squared

##Problem Set 3.6 













































