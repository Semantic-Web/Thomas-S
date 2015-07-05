#Thomas Sonderman
import pandas as pd
import numpy as np


def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


#define header row names for reading the csv
headers = ['Name', 'Time','Date','DataPoint1','DataPoint2']
df = pd.read_csv('thomastime.csv',header=False,
                      names=headers)

#print_full(df)

#Make sure data is in numerica format to not cause errors, force numeric if not
df['DataPoint1'] = df[df.columns[4]].convert_objects(convert_numeric=True)


#df['DataPoint1'][df['DataPoint1']=='-'] = None

#Cover Datapoints that are not numeric with a zero'd value of 0.0
df['DataPoint1'] = df['DataPoint1'].astype(float).fillna(0.0)

#Process all calculated averages and noise
df['Moving_Avg'] = pd.rolling_mean(df['DataPoint1'], 100, 50)
df['Noise'] = df['DataPoint1'] - df['Moving_Avg']
df['Average100'] = pd.rolling_mean(df['DataPoint1'], 100, 1)
print_full(df)


#send output to csv
df.to_csv('output.csv')
