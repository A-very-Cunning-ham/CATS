import threading
import time

import torch
from pymongo.collection import Collection

print("booting up!")
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import os
import detection
import numpy as np
from queue import Queue
import torchvision

# Queue and Threads code
image_ingest_queue = Queue()
decoded_image_queue = Queue()
detected_objects_queue = Queue()
SENTINEL = "SENTINEL"
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')


def image_decode_ingest_worker():
    while True:
        image_encoded_bytes, camera = image_ingest_queue.get()
        if image_encoded_bytes == SENTINEL:
            # signal next thread that we are done
            decoded_image_queue.put((SENTINEL, None))
            # signal other threads using this queue that we are done
            image_ingest_queue.put((SENTINEL, None))
            break
        image_encoded_bytes_tensor = torch.ByteTensor(image_encoded_bytes)
        image_tensor = torchvision.io.decode_image(image_encoded_bytes_tensor, torchvision.io.image.ImageReadMode.RGB)
        image_ingest_queue.task_done()
        decoded_image_queue.put((image_tensor, camera))

def image_recognize_worker():
    while True:
        image_tensor, camera = decoded_image_queue.get()
        if image_tensor == SENTINEL:
            # signal next thread that we are done
            detected_objects_queue.put((SENTINEL, None, None))
            # signal other threads using this queue that we are done
            decoded_image_queue.put((SENTINEL, None))
            break
        objects_detected, image = detection.process_image(image_tensor)
        decoded_image_queue.task_done()
        detected_objects_queue.put((objects_detected, image, camera))


def objects_detected_to_mongo_worker(mongo_db_collection: Collection):
    while True:
        objects_detected, image, camera = detected_objects_queue.get()
        if objects_detected == SENTINEL:
            # signal other threads using this queue that we are done
            detected_objects_queue.put((SENTINEL, None, None))
            break
        newID = ObjectId()
        timeObjectID = ObjectId.from_datetime(datetime.datetime.now())
        finalID = timeObjectID[:8] + newID[8:]
        mongo_object = {'_id': finalID, 'camera': camera, 'filename': f"/images/{finalID}.jpg",
                        'object-detected': "cat", 'catIDs': [], 'objects-found': objects_detected}
        detected_objects_queue.task_done()
        mongo_db_collection.insert_one(mongo_object)
        torchvision.io.write_jpeg(image, f"/images/{finalID}.jpg")


# MongoDB code
def get_database():
    
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb://{os.environ['MONGODB_USER']}:{os.environ['MONGODB_PASSWORD']}@mongodb"
    # CONNECTION_STRING = "mongodb://root:123456@mongodb:7017/"
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

    # old code
    # camera = msg.topic.split("/")
    # newID = ObjectId()
    # filepath = f"{camera[1]}-{newID}.jpeg"
    # objects_detected, image = detection.process_image(msg.payload)
    #
    # with open("/images/" + filepath, 'wb') as file_handler:
    #     img_encode = cv2.imencode('.jpg', image)[1]
    #     data_encode = np.array(img_encode)
    #     byte_encode = data_encode.tobytes()
    #     file_handler.write(byte_encode)
    #
    # mongo_object = {'_id': newID, 'camera': camera[1], 'filename': filepath, 'object-detected': camera[2], 'catIDs': [],
    #                 'objects-found': objects_detected}
    # collection.insert_one(mongo_object)

    # New Thread based code
    camera = msg.topic.split("/")
    image_ingest_queue.put((msg.payload, camera[1]))
    print("image_ingest_queue size: ", image_ingest_queue.qsize())


print("python running before db!")
db = get_database()
collection = db['cat_images']
print("DB connected!")
# Start Threads
all_threads = []
for i in range(1):
    image_decode_ingest_thread = threading.Thread(target=image_decode_ingest_worker)
    image_decode_ingest_thread.start()
    all_threads.append(image_decode_ingest_thread)
for i in range(1):
    image_recognize_thread = threading.Thread(target=image_recognize_worker)
    image_recognize_thread.start()
    all_threads.append(image_recognize_thread)
for i in range(1):
    objects_detected_to_mongo_thread = threading.Thread(target=objects_detected_to_mongo_worker, args=(collection,))
    objects_detected_to_mongo_thread.start()
    all_threads.append(objects_detected_to_mongo_thread)
print("Threads started!")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mosquitto", 1883, 60)
try:
    client.loop_forever()
except KeyboardInterrupt:
    image_ingest_queue.put(SENTINEL)
    last_queue_size = image_ingest_queue.qsize()
    queue_list = [image_ingest_queue, decoded_image_queue, detected_objects_queue]
    for current_queue in queue_list:
        while time.sleep(1):
            if current_queue.qsize() == last_queue_size:
                continue
            print("Queue size: ", current_queue.qsize())
            last_queue_size = current_queue.qsize()
    for thread in all_threads:
        thread.join()
