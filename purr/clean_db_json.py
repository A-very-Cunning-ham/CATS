import json
import sys
from itertools import groupby
from math import pow

db_json_path = sys.argv[1]
with open(db_json_path) as db_json_file:
    db_json = json.load(db_json_file)

# sample json array element {"_id": "6434d16a0000000000000000", "camera": "test-camera", "filename": "1681197480-WGI_0046-000031-Full-00.jpg", "object-detected": "cat", "catIDs": [], "objects-found": [{"confidence": 0.833984375, "class": "Cat Ear", "left-top": [1093, 159], "right-bottom": [1133, 231]}, {"confidence": 0.841796875, "class": "Cat Ear", "left-top": [1198, 159], "right-bottom": [1256, 227]}, {"confidence": 0.97021484375, "class": "Cat Face", "left-top": [1094, 154], "right-bottom": [1250, 326]}]}
# group by the first 27 characters of filename
db_json_groups = groupby(db_json, lambda x: x['filename'][:27])
# extract the image with the most objects where faces = ears/2 found, if there is a tie, extract the image with the highest confidence for each object
db_json_filtered = []
for _, group in db_json_groups:
    group = list(group)
    group.sort(key=lambda x: len([od for od in x['objects-found']]))  # if od['class'] == 'Cat Face']) - len([od for od in x['objects-found'] if od['class'] == 'Cat Ear'])/2)
    db_json_filtered.append(group[-1])

# write the filenames of each best frame filename to a file
db_json_filtered.sort(key=lambda db_doc: max(db_doc['objects-found'], key=lambda object_found: object_found["confidence"])["confidence"], reverse=True)
with open('best_frames.txt', 'w') as best_frames_file:
    for item in db_json_filtered:
        best_frames_file.write(f"{item['filename']}\n")
