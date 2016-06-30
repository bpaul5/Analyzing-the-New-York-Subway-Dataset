###Problem 1
q = '''
    SELECT 
    count(rain)
    FROM 
    data
    WHERE 
    rain = 1
'''

a = pandasql.sqldf(q.lower(), locals())

###Problem 2
q = '''
    SELECT 
    fog, maxtempi
    FROM 
    data
    GROUP BY
    fog
'''

a = pandasql.sqldf(q.lower(), locals())

###Problem 3
q = '''
    SELECT
    AVG(meantempi)
    FROM
    data
    WHERE 
    cast(strftime('%w', date) as integer) = 0 OR
    cast(strftime('%w', date) as integer) = 6
'''

a = pandasql.sqldf(q.lower(), locals())

###Problem 4 
q = '''
    SELECT
    AVG(mintempi)
    FROM
    data
    WHERE
    mintempi > 55 and rain = 1
    '''

a = pandasql.sqldf(q.lower(), locals())

###Problem 5
import csv 
import pandasql 

f_in = open('/Users/bindupaul/Documents/Classes/Udacity/Project 2/data.webarchive', 'r')
f_out = open('out_data.csv', 'w')
reader_in = csv.reader(f_in, delimiter=',')
writer_out = csv.writer(f_out, delimiter=',')

for line in reader_in:
    count = len(line)/5
    header = line[0:3]
    x = 3
    y = 8
    while count > 0:
        body = line[x:y]
        x = (x + 5)
        y = (y + 5)
        count = (count - 1)
        writer_out.writerow(header + body)
        
f_in.close()
f_out.close()

###Problem 6
with open('out_data2.csv', 'w') as master_file:
    master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
    writer_out = csv.writer(master_file)
    for 'out_data.csv' in master_file:
        with open('out_data.csv', 'r') as f_in:
            reader_in = csv.reader(f_in)
            for row in reader_in:
                a = row[0:8]
                writer_out.writerow(a)

      
###Problem 7
data = pandas.read_csv('/Users/bindupaul/Documents/Classes/Udacity/Udacity Data/Master.csv')

# need this step 
q = '''
    SELECT
    *
    FROM
    data
    '''
print pandasql.sqldf(q, locals())

q = '''
    SELECT
    playerID
    FROM
    data
    WHERE
    bats = 'R'
    '''
print pandasql.sqldf(q, locals())

# import turnstile data 
q = '''
    SELECT
    *
    FROM
    turnstile_data
    WHERE
    DESCn = 'REGULAR'
    '''
print pandasql.sqldf(q, locals())


###Probem 8 
# how to delete columns in dataframe
del df['UNIT']
# rename column UNIT to unit
df.rename(columns={'UNIT':'unit'}, inplace = True)
# create new column of differences b/w other columns 
df['H-L'] = df.high - df.low
df['H-L'] = df['High'] - df['Low']
# moving average or rolling mean 
df['100MA'] = pd.rolling_mean(df['Close'], 100) # 100 = periods
# defference of a col and its next value
df['difference'] = df['Close'].diff()

df['ENTRIESn_hourly'] = df['ENTRIESn'].diff()
df.fillna(1, inplace=True)

###Problem 9 
df['EXITSn_hourly'] = df['EXITSn'].diff()
df.fillna(0, inplace=True)


###Problem 10 
import pandas as pd
import csv
import time 
import datetime
import calendar
time.time()
time.loacaltime(time.time())
time.asctime()
time.mktime()
print (calendar.month(2015,3))

# works on python 
def time_to_hour(df):
    time = df['TIMEn']
    newtime = pd.to_datetime(time)
    hours = newtime.dt.hour
    df['Hour'] = hours
    for i in df['Hour']:
        int(i)

# works for udacity answer
newtime = pd.to_datetime(time)
return newtime.hour


###Problem 11
from datetime import datetime 
from time import time 

# for year 'y' is 11 and 'Y' 2011 
# strptime provide string and return datetime object 
# strftime provide datetime object and return string
datetime.strftime(datetime.strptime(date, '%m-%d-%y'), '%Y-%m-%d')



















