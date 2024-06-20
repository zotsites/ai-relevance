
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import psycopg2
import json 
from psycopg2.extras import RealDictCursor

def read_password(filename):
    with open(filename, 'r') as f:
        lines = f.readlines();
    return ''.join(line.strip() for line in lines)





uri = "mongodb+srv://snipeAdmin:" + read_password(".mongo_password") + "@cluster0.jgcudmg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    posgress_database = psycopg2.connect(host='anthill.postgres.database.azure.com', dbname='zotsites', user='circinus', password='Admin123', port=5432)
    postgres_cursor = posgress_database.cursor(cursor_factory=RealDictCursor)
    query = "SELECT * FROM webpage;"
    postgres_cursor.execute(query)
    rows = postgres_cursor.fetchall()
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["cluster0"]
    collection = db['websites_json']
    print(type(rows[1]))
    if isinstance(rows, list):
        collection.insert_many(rows)


except Exception as e:
    print(e)
