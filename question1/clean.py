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

def data_cleaning(df):
  df['Date Time'] = pd.to_datetime(df['Date Time'])
  df['Date Time'] = df['Date Time'].dt.tz_localize(None)
  df[['NOx', 'NO2', 'NO','PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5',
      'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure']] = df[['NOx', 'NO2', 'NO','PM10', 
      'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure']].fillna(0.0)

  # #int
  df[['SiteID']] = df[['SiteID']].fillna(0)

  # # #bool
  df[['Current']] = df[['Current']].fillna('No Response')
  df[['Date Time']] = df[['Date Time']].fillna(datetime.now())
  # #string
  df[['Location', 'geo_point_2d', 'DateStart', 'DateEnd', 'Instrument Type']] = df[['Location', 
          'geo_point_2d', 'DateStart', 'DateEnd', 'Instrument Type']].fillna('No records')
  
  return df



clean_df = data_cleaning(df)

def Nan_check(data_df):
  '''
  This checks if there is any columns with nan
  '''
  nan_check = df.isnull().sum().values
  print(nan_check)
  max_value = max(nan_check)
  min_value = min(nan_check)
  check = 'No more Nan values' if max_value == min_value else 'Nan still exist in the dataframe'
  return check

nan_status = Nan_check(clean_df)
print(nan_status)

'''
Generating the clean csv data
'''

if nan_status == 'No more Nan values':
  clean_df[:3].to_csv('clean.csv', index=False)
  data_quantity = len(clean_df)
  print('csv file generated successfully')
  print('Total quantity of clean records is {}'.format(data_quantity))
else:
  print('Unable to generate data due to some NAN in the data')

#print(clean_df.head(2))

