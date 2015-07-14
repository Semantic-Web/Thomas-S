# Thomas Sonderman
# tsonderm@fau.edu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams


columns = ['area_name','poverty_level','crimes']
index = np.arange(80) # array of numbers for the number of samples
df = pd.DataFrame(columns=columns, index = index)
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
counter = 0
with open("socioeconomic_chicago.rdf") as f:
    
    for line in f:
        s = df.xs(counter)
        if "<ds:community_area_name>" in line:
            areaName = find_between( line, "<ds:community_area_name>", "</ds:community_area_name>" )
            areaName = areaName.rstrip()
            s.area_name = areaName
            #print areaName
        if "<ds:percent_households_below_poverty>" in line:
            povertyLevel = find_between( line, "<ds:percent_households_below_poverty>","</ds:percent_households_below_poverty>")
            s.poverty_level = povertyLevel
            s.crimes=0
            df.append(s)
            counter += 1
            #print povertyLevel

with open("crimes_chicago.rdf") as f:
    
    for line in f:
        if "<ds:community_area>" in line:
            areaNumber = find_between( line, "<ds:community_area>", "</ds:community_area>" )
            areaNumber = int(areaNumber)
            #print df['crimes'][areaNumber-1]
            df['crimes'][areaNumber-1]=df['crimes'][areaNumber-1]+1


df2 = df.ix[:77]            
print df2
my_plot = df2.sort(columns='crimes',ascending=False).plot(kind='bar',legend=None,title="Crimes vs Poverty Level",figsize=(15, 7))

my_plot.set_xlabel("Poverty Level")
my_plot.set_ylabel("Crimes")   

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



