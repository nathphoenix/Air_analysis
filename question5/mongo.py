import pymongo  
from datetime import datetime 
import pandas as pd

clean_df = pd.read_csv('clean_data.csv')
clean_df = clean_df[clean_df['Location'] == 'AURN Bristol Centre']
air_pollution_dict  = clean_df.T.to_dict()
air_pollution_dict = [v for k, v in air_pollution_dict.items()]

client = pymongo.MongoClient()
clientdb = client['productdb']
#clientdb = client['Air_pollution']
product_collection = clientdb['pollution'] 

for items in air_pollution_dict:
    product_collection.insert_one({'Date Time':items['Date Time'], 'NOx':items['NO2'], 'NO':items['NO'], 'SiteID':items['SiteID'], 'PM10':items['PM10'], 'NVPM10':items['NVPM10'], 
                                   'VPM10':items['VPM10'], 'NVPM2_5':items['NVPM2.5'], 'PM2_5':items['PM2.5'], 'VPM2_5':items['VPM2.5'], 'CO':items['CO'], 'O3':items['O3'], 
                                   'SO2':items['SO2'], 'Temperature': items['Temperature'], 'RH':items['RH'], 
                                   'Air Pressure': items[ 'Air Pressure'], 'Location': items['Location'],
                                   'geo_point_2d':items['geo_point_2d'], 'DateStart':items['DateStart'], 'DateEnd':items['DateEnd'], 'Current':items['Current'],
                                   'Instrument Type':items['Instrument Type']})
client.close()
        
print('============SAVING COMPLETED=============')