import pymongo  
from datetime import datetime 
import pandas as pd

clean_df = pd.read_csv('clean_data.csv')
#MODELLING THE DATA FOR A PARTICULAR LOCATION
clean_df = clean_df[clean_df['Location'] == 'AURN Bristol Centre']
#CONVERTING THE DATAFRAME TO A LIST OF DICTIONARY
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


'''
QUERYING OUR MONGODB DATABASE TO RETURN CERTAIN RECORDS BASE ON OUR QUERY 
'''

name = 'Fishponds Road'

#RECORDS OF WHERE NITROGEN OXIDE IS NOT EQUAL TO ZERO
reported = product_collection.find({'NO': { "$ne" : 0}}, {"_id": 0}).limit(5)
for items in reported:
    print(items)
    
#getting records where siteID is 215 and 270
reported = product_collection.find({"SiteID" : { "$in" : [ 215, 270] }}, {"_id": 0}).limit(5)
for items in reported:
    print(items)
    
#getting records where siteID is not 215 and 270 using 'NIN' operator
reported = product_collection.find({"SiteID" : { "$nin" : [ 215, 270] }}, {"_id": 0}).limit(5)
for items in reported:
    print(items)
    
#gt represnt greater than
reported = product_collection.find({"SiteID" : { "$gt" :  315 }}, {"_id": 0}).limit(5)
for items in reported:
    print(items)
    
#COMBINING TWO OR MORE QUERIES

reported = product_collection.find({
    "$and" : [{
                 "SiteID" : { "$eq" : 215}
              },
              {
                   "NO" : { "$ne" : 0}
              },]
}, {"_id": 0}).limit(10)
for items in reported:
    print(items)
    
    
reported = product_collection.find({
    "$and" : [{
                 "SiteID" : { "$eq" : 215}
              },
              {
                   "NO" : { "$ne" : 0}
              },
        {'Location': 'Parson Street School'}]
}, {"_id": 0}).limit(10)
for items in reported:
    print(items)
    
    
reported = product_collection.aggregate([
    ## stage 1
    {
        "$match" : 
                 {'Location': name }
    },
    ## stage 2
    {
        "$count" : "total_rows"
    }
])
for items in reported:
    print(items)
    

reported = product_collection.aggregate([
    ## stage 1
    {
        "$match" : 
                 {'Location': name }
    },
    ## stage 2
    {
    "$group" : { "_id" : 0 ,
                     "average_NOx": { "$avg" : "$NOx"},
                     "unique_SiteID" : {"$addToSet" : "$SiteID"}} 
    }
])
for items in reported:
    print(items) 
