import hashlib

with open('file.json', 'rb') as file:
    buf = file.read()
    hashedFile = hashlib.sha256(buf)

hexFile = open("hash.txt", "w")
hexFile.write(hashedFile.hexdigest())
hexFile.close()

print(hashedFile.hexdigest())
