import hashlib

string = "ugkcyxxp"
result = ""
index = 0

while len(result) < 8:
    stringEncoded = str.encode(f"{string}{str(index)}")
    stringHash = hashlib.md5(stringEncoded).hexdigest()
    if stringHash[:5] == "00000":
        result += stringHash[5]
    index += 1

print(result) # d4cd2ee1