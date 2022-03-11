import pandas as pd 
import datetime 
import pytz
import numpy as np

now = datetime.datetime.now()
now = now.astimezone(pytz.timezone("Australia/Sydney")).strftime("%Y-%m-%d %H:%m:00")

df = pd.read_csv('input/wilsons.csv')

# 'date', 'Water Level (m)', 'Minor flood', 'Moderate flood',
#        'Major flood'

# hawk = pd.read_csv('input/wilsons.csv')

max = df['date'].max()

min = df['date'].min()

df['date'] = pd.to_datetime(df['date'])

# df.set_index('date', inplace=True)

# resampled = df.resample('60min', on='date')

# df

new_range = pd.date_range(max, now, freq="H")

new = pd.DataFrame({
    'date': new_range,
    'Water Level (m)': np.nan,
   'Minor flood': np.nan,
    'Moderate flood': np.nan,
    'Major flood': np.nan})

tog = df.append(new)

tog['date_dup'] = tog['date'].dt.strftime("%Y/%m/%d %H")
tog.drop_duplicates(subset=['date_dup'], inplace=True, keep='first')

tog['Minor flood'] = tog['Minor flood'].ffill()
tog['Moderate flood'] = tog['Moderate flood'].ffill()
tog['Major flood'] = tog['Major flood'].ffill()

tog = tog[['date', 'Water Level (m)', 'Minor flood', 'Moderate flood',
       'Major flood']]

with open('input/wilsons_reindexed.csv', 'w') as f:
    tog.to_csv(f, index=False, header=True)

p = tog

print(p)
print(p.columns)



print(now)