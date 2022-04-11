from sqlalchemy import MetaData
from sqlalchemy import create_engine
import pandas as pd


meta = MetaData()

'''
READING CLEAN CSV FILE
'''
csv_name = '../question1/clean.csv'
clean_df = pd.read_csv(csv_name)

'''
CREATING A CONNECTION TO MYSQL DATABASE AND GENERATE INSERT QUERY
'''
engine = create_engine('mysql+pymysql://nathaniel:church75@localhost/air_pollution', echo=False)
meta.reflect(bind=engine)
insert_query = 'INSERT INTO pollution ({}) VALUES\n{};'.format(', '.join([repr(c) for c in clean_df.columns]), ',\n'.join([str(row[1:]) for row in engine.execute(meta.tables['pollution'].select(limit=100))]))

'''
Saving generated insert query to a sql file
'''

f = open('insert-100.sql', "w",  errors="ignore")
f.write(insert_query)
f.close()