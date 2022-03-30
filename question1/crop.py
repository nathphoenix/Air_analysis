from operator import index
import pandas as pd
import os
from datetime import datetime

csv_data = os.path.join(os.getcwd(), '../bristol-air-quality-data.csv')
print(csv_data)
df = pd.read_csv(csv_data, sep = ';')
df = df.dropna(how='all')

'''
DATAFRAME TRANSFORMATION AND CLEANING
'''

def date_transform(df):
  df['Date Time'] = pd.to_datetime(df['Date Time'])
  df['Date Time'] = df['Date Time'].dt.tz_localize(None)
  return df

clean_date_df = date_transform(df)

crop_csv = clean_date_df[clean_date_df['Date Time'] >= "2010-01-01" ]
print('Total quantity of crop records is {}'.format(len(crop_csv)))

'''
saving dataframe to a file
'''
crop_csv.to_csv('crop.csv', index=False)

# print(clean_date_df.head(2))

