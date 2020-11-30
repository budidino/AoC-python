import hashlib

string = "ugkcyxxp"
result = "        "

index = 0
while result.count(" ") > 0:
    stringEncoded = str.encode(f"{string}{str(index)}")
    stringHash = hashlib.md5(stringEncoded).hexdigest()
    if stringHash[:5] == "00000":
        position = stringHash[5]
        if position in "01234567" and result[int(position)] == " ":
            result = result[:int(position)] + stringHash[6] + result[int(position)+1:]
            print(f"'{result}'")
    index += 1

print(result) # f2c730e5