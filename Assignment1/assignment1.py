# Thomas Sonderman
# tsonderm@fau.edu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
#define header row names for reading the csv
headers = ['package_id', 'DataSet Title', 'Organization Name', 'Views','Date']
df = pd.read_csv('datagovdatasetsviewmetrics.csv',header=False,
                 names=headers)
#Run SQL Commands, Group the views by org name, sum the views, then sort the records by Total Views and grab the top 10
grouped = df[['Organization Name','Views']].groupby('Organization Name').sum().sort(columns='Views',ascending=False).head(10)
#Bar Chart Section
grouped.index.name = None
print grouped.to_string()
#add autolayout so labels aren't cutoff
rcParams.update({'figure.autolayout': True})
#initialize matplotlib
plt.figure()
#organize data layout for graph
my_plot = grouped.plot(kind='barh',legend="Views",title="Total Views",figsize=(10, 7))
my_plot.set_xlabel("Organizations")

#display graph
plt.show()
plt.close()



