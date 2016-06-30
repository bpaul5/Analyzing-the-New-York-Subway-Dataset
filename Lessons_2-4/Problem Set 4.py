# Project 2 Lesson 4 

# visual cues (position, length, angle, 
# direction, area, volume, saturation, hue)

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from ggplot import * 
import scipy 

# ggplot 
print ggplot(data, aes('xvar', 'yvar'))+geom_point(color = 'coral')
+geom_line(color='coral')+ggtitle('title')+xlab('x-label')+ylab('y-label')

# ggplot for multiple lines 
print ggplot(df, aes('yearID', 'HR', color='teamID')) + 
geom_point() + geom_line() + ggtitle('Total HRs by Year') + 
xlab('Year') + ylab('HR')

# Project 2 Question 1 

dff = df[['ENTRIESn_hourly', 'Hour']].groupby('Hour', 
as_index=False).mean().astype('int')

byhour = turnstile_weather.groupby('Hour')
plot = ggplot(df, aes((byhour['Hour'].mean()),
byhour['ENTRIESn_hourly'].mean())) + geom_point() + geom_line() +
ggtitle('Average Subway Ridership by Hour') + 
xlab('Hour') + ylab('Entries Hourly') + xlim(0,25)

hourx = range(0,24)
plt.bar(hourx, rainn, label= 'Rain', color = 'red', width = .8)
plt.bar(hourx, norainn, label = 'No Rain', width = .6)
plt.xlabel('Hour')
plt.ylabel('Entries')
plt.legend(loc=2)
plt.title('Mean Entries per Hour for Rain/No Rain Days')

plt.hist((norain_list, rain_list), bins, histtype=u'bar', 
         color=('lime', 'red'), label=('No Rain', 'Rain'))         
plt.xlabel('Number of Entries')
plt.ylabel('Frequency of Entries')
plt.legend(loc=1)
plt.title('Frequency of Entries for Rain and No Rain Days')