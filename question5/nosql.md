This entire process begins by install mongodb compass on my system and i then install the neccessary modules like pymongo in order to have access to the mongoclient and dnspythpn for proper connection to a remote mongodb database.

At the complemention of all neccessary installation, i then import the pymongo in order to set up my mongodb and create a collection(which is better known as table) for storing each records from the clean csv as a document, mind you one row on a table in a RDBMS is equivalent to a document in a NRDBMS.

connection was set up by instantiating the mongoclient from the pymongo library without passing a connection string argument since i'm using my local mongodb install through mongo compass.

Database was then created in the form of a key for example; clientdb = client['pollutiondb']
the client was from the connection that was set up above and similarly our collection is created by calling the clientdb for example; pollution_collection = clientdb['pollution_data']. There are two ways of creating both database and the collection which is more of function call approach instead of the dictionary approach as done above.

After successfully creating the database and collection, i then transpose my dataframe and finally convert to a list of dictionary in order to save each dictionary in the collection as document because only a dictionary records is acceptable by mongodb or other NRDBMS.

Finally, i then iterate through each of the dictionary and save them into my mongodb collection called 'pollution_data' using the insert_one functionality on the pollution_collection variable 
i.e 'pollution_collection.insert_one()'

after  i'm done inserting all records to the mongodb i then close my mongodb connection in order to avoid external attack on my database using the 'close()' functionality.