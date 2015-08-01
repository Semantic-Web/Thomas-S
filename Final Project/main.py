__author__ = 'semanticweb'
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

columns = ['state','deaths']
index = np.arange(57) # array of numbers for the number of samples
df = pd.DataFrame(columns=columns, index = index)


headers = ['Area', 'Year','Deaths']
df = pd.read_csv('deaths.csv',header=False,
                      names=headers)
df['Area'] = df['Area'].astype(str)
df['Area'] = df['Area'].str[-2:]


byState_df = pd.DataFrame(states.items())
byState_df['Deaths'] = 0
byState_df['Hospitals'] = 0
byState_df['StatePop'] = 0
byState_df['DeathPercentage'] = 0.0
byState_df['HospitalPercentage'] = 0.0
byState_df['PovertyPercentage'] = 0.0
df['Deaths'] = df['Deaths'].convert_objects(convert_numeric=True)

#print byState_df
for index, row in df.iterrows():
    if row['Area'] in states:
            if not math.isnan(row['Deaths']):
                byState_df.loc[byState_df[0] == row['Area'], 'Deaths'] = byState_df.loc[byState_df[0] == row['Area'], 'Deaths'] + row['Deaths']
#print byState_df

headers = ['Provider ID','Hospital Name','Address','City','State','ZIP Code','County Name','Phone Number','Hospital Type','Hospital Ownership','Emergency Services','Location']
hospitals_df = pd.read_csv('hospitals.csv',header=False,
                      names=headers)
#print hospitals_df['State']
for index, row in hospitals_df.iterrows():
    if row['State'] in states:
                byState_df.loc[byState_df[0] == row['State'], 'Hospitals'] = byState_df.loc[byState_df[0] == row['State'], 'Hospitals'] + 1

#print byState_df


headers = ['SUMLEV','REGION','DIVISION','STATE','NAME','POPESTIMATE2014','POPEST18PLUS2014','PCNT_POPEST18PLUS']
statepop_df = pd.read_csv('state_populations.csv',header=False,
                      names=headers)
#print hospitals_df['State']
for index, row in statepop_df.iterrows():
    if row['NAME'] in states:
                byState_df.loc[byState_df[0] == row['NAME'], 'StatePop'] = row['POPESTIMATE2014']

#print byState_df

for index, row in byState_df.iterrows():
    if row['Deaths'] > 0 and row['StatePop'] > 0 and row['Hospitals'] > 0:
              byState_df.loc[byState_df[0] == row[0], 'DeathPercentage'] = 1000 * float(row['Deaths']) / float(row['StatePop'])
              byState_df.loc[byState_df[0] == row[0], 'HospitalPercentage'] = 100000 * float(row['Hospitals']) / float(row['StatePop'])


headers = ['StateCode','State','Poverty']
statepop_df = pd.read_csv('poverty.csv',header=False,
                      names=headers)
for index, row in statepop_df.iterrows():
    if row['State'] in states:
                byState_df.loc[byState_df[0] == row['State'], 'PovertyPercentage'] = row['Poverty']

print byState_df

byState_df.to_csv('output_v2.csv')
