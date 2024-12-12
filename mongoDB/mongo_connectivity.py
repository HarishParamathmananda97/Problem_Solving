from pymongo.mongo_client import MongoClient
# import urllib.parse
# username = urllib.parse.quote_plus('harishparamathmananda')
# password = urllib.parse.quote_plus('Zombies@97')
# print(username, password)


from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://harishparamathmananda:zombies@jerry.yil7qvo.mongodb.net/?retryWrites=true&w=majority&appName=Jerry"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)