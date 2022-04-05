This entire process begins by install mongodb compass on my system and i then install the neccessary modules like pymongo in order to have access to the mongoclient and dnspythpn for proper connection to a remote mongodb database.

I then import the pymongo in order to set up my mongodb and create a collection(which is better known as table) for storing each records from the clean csv as a document, mind you one row on a table in a RDBMS is equivalent to a document in a NRDBMS.

connection was set up by instantiating the mongoclient from the pymongo library without passing a connection string argument since i'm using my local mongodb install through mongo compass.

Database was then created in the form of a key for example; clientdb = client['productdb']
the client was from the connection that was set up above and similarly our collection is created by calling the clientdb for example; product_collection = clientdb['pollution'].

I then transpose my dataframe and finally convert to a list of dictionary in order to save each dictionary in the collection as document.

Finally, i then iterate through each of the dictionary and save them into my mongodb collection called 'productdb' using the insert_one functionality on the product_collection variable 
i.e 'product_collection.insert_one()'