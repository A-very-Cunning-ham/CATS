import paho.mqtt.client as mqtt
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import os
import detection


# MongoDB code
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb://{os.environ['MONGODB_USER']}:{os.environ['MONGODB_PASSWORD']}@mongodb"
    #       CONNECTION_STRING = f"mongodb://{os.environ['MONGODB_USER']}:{os.environ['MONGODB_PASSWORD']}@localhost/test?retryWrites=true&w=majority"
    print(CONNECTION_STRING)
    #    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    #    # Create the database for our example (we will use the same database throughout the tutorial
    return client[os.environ['MONGODB_DATABASE']]


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("frigate/+/+/snapshot")


def on_message(client, userdata, msg):
    print(msg.topic + " @ " + str(datetime.datetime.now()) + " image payload")

    camera = msg.topic.split("/")
    newID = ObjectId()
    filepath = f"{camera[1]}-{newID}.jpeg"
    objects_detected, image = detection.process_image(msg.payload)

    with open("/images/" + filepath, 'wb') as file_handler:
        file_handler.write(msg.payload)

    mongo_object = {'_id': newID, 'camera': camera[1], 'filename': filepath, 'object-detected': camera[2], 'catIDs': [],
                    'objects-found': objects_detected}
    collection.insert_one(mongo_object)


db = get_database()
collection = db['cat_images']
print("python running!")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mosquitto", 1883, 60)
client.loop_forever()
