
from openai import OpenAI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#reads the api keys from a local file

def read_password(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return ''.join(line.strip() for line in lines)

#create client connection for openai
client = OpenAI(
  api_key= read_password('.openai_key'),  
)

#set up mongodb database collection to iterate through

uri = "mongodb+srv://snipeAdmin:" + read_password(".mongo_password") + "@cluster0.jgcudmg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_client = MongoClient(uri, server_api=ServerApi('1'))
db = db_client["cluster0"]
websites_backup = db['websites_json_backup']
relevant = db['relevant']
non_relevant = db['non_relevant']
all_docs = websites_backup.find()

#for loop to sort the documents into relevant and non-relevant


for doc in all_docs:
    response = client.chat.completions.create(
        model="gpt-4o", # model = "relevance".
        messages=[
            {"role": "system", "content": "You answer with either 'yes' or 'no' about weather a website is directly realated to the University of California Irvine."},
            {"role": "user", "content": doc.get('url')},  
        ]
    )
    
    if 'yes' in response.choices[0].message.content.lower():
        relevant.insert_one(doc)
        print(doc.get('url') + ": Yes")
    else:
        non_relevant.insert_one(doc)
        print(doc.get('url') + ": No")


