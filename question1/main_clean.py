import pandas as pd
import os
import numpy as np
from datetime import datetime

csv_data = os.path.join(os.getcwd(), 'crop.csv')
print(csv_data)
df = pd.read_csv(csv_data)
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


def match_location(df):
  match_details = df
  site_data = [{'SiteID':188,  'Location':'AURN Bristol Centre'},
  {'SiteID':203, 'Location':'Brislington Depot'},
  {'SiteID':206, 'Location':'Rupert Street'},
  {'SiteID':209, 'Location':'IKEA M32'},
  {'SiteID':213, 'Location':'Old Market'},
  {'SiteID':215, 'Location':'Parson Street School'},
  {'SiteID':228, 'Location':'Temple Meads Station'},
  {'SiteID':270, 'Location':'Wells Road'},
  {'SiteID':271, 'Location':'Trailer Portway P&R'},
  {'SiteID':375, 'Location':'Newfoundland Road Police Station'},
  {'SiteID':395, 'Location':"Shiner's Garage"},
  {'SiteID':452, 'Location':'AURN St Pauls'},
  {'SiteID':447, 'Location':'Bath Road'},
  {'SiteID':459, 'Location':'Cheltenham Road \ Station Road'},
  {'SiteID':463, 'Location':'Fishponds Road'},
  {'SiteID':481, 'Location':'CREATE Centre Roof'},
  {'SiteID':500, 'Location':'Temple Way'},
  {'SiteID':501, 'Location':'Colston Avenue'}]
  site_data_df = pd.DataFrame(site_data)

  location_site = site_data_df['SiteID'].to_list()
  location_list = site_data_df['Location'].to_list()
  location_dict = dict(zip(location_site, location_list))

  match_details['New_Location'] = df['SiteID'].map(location_dict)

  match_details['status'] = np.where(match_details['New_Location'] == match_details['New_Location'], 
                                            'Match', 'Mismatch')
  mis_match_data = match_details[match_details['status'] == 'Mismatch']
  mis_match_count = 'Quantity of  mismatch records is {}'.format(len(mis_match_data))
  match_data = match_details[match_details['status'] == 'Match']
  final_clean_data = match_data[['Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 
                                'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'Location', 'geo_point_2d', 'DateStart', 
                                'DateEnd', 'Current', 'Instrument Type']]
  return final_clean_data, mis_match_count

final_clean_data, mis_match_count = match_location(clean_df)
print(mis_match_count)

nan_status = Nan_check(final_clean_data)
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

