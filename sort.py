from selenium import webdriver
import keyboard
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def read_password(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return ''.join(line.strip() for line in lines)

uri = "mongodb+srv://snipeAdmin:" + read_password(".mongo_password") + "@cluster0.jgcudmg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["cluster0"]
websites_backup = db['websites_json_backup']
relevant = db['relevant']
non_relevant = db['non_relevant']
random_docs = websites_backup.aggregate([{ "$sample": { "size": 5000 } }])




for doc in random_docs:
    driver = webdriver.Edge()
    driver.get(doc.get("url"))
    key_event = keyboard.read_event()
    if key_event.event_type == keyboard.KEY_DOWN:
        key = key_event.name
        if key == 'right':
            print("Pressed:", key)
            relevant.insert_one(doc)
        else:
            non_relevant.insert_one(doc)
        if driver:
            driver.quit()

    if key_event.event_type == keyboard.KEY_UP:
        if key_event.name == 'q':
            break
if driver:q
    driver.quit()





