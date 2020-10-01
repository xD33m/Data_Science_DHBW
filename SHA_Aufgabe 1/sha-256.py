import hashlib
import json

data = ""
with open('file.json', 'r') as file:
    data = json.load(file)
    for idx, person in enumerate(data):
        data[idx]['firstname'] = hashlib.sha256(person['firstname'].encode()).hexdigest()
        data[idx]['lastname'] = hashlib.sha256(person['lastname'].encode()).hexdigest()

hexFile = open("hashed.json", "w")
hexFile.write(str(data))
hexFile.close()