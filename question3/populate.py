import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

csv_data = '../question1/clean.csv'
clean_df = pd.read_csv(csv_data)

try:
  engine = create_engine('mysql+pymysql://nathaniel:church75@localhost/pollution', echo=False)
  clean_df.to_sql(name='air_sample', con=engine, if_exists = 'append', index=False)
except:

  #establishing the connection
  conn = mysql.connector.connect(host="localhost", user="nathaniel", password="church75")

  #Creating a cursor object using the cursor() method
  cursor = conn.cursor()

  #Droping database MYDATABASE if already exists.
  cursor.execute("DROP database IF EXISTS pollution")

  #Preparing query to create a database
  sql = "CREATE database pollution";

  #Creating a database
  cursor.execute(sql)

  engine = create_engine('mysql+pymysql://nathaniel:church75@localhost/pollution', echo=False)
  clean_df.to_sql(name='air_sample', con=engine, if_exists = 'append', index=False)
  print('Data Insertion Completed')