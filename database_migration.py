
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def read_password(filename):
    with open(filename, 'r') as f:
        lines = f.readlines();
    return ''.join(line.strip() for line in lines)





uri = "mongodb+srv://snipeAdmin:" + read_password(".mongo_password") + "@cluster0.jgcudmg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)