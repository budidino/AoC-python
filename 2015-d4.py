import hashlib

key = "yzbqklnj"

def md5_starting_with_string(string):
    index = 0
    while True:
        if hashlib.md5(f"{key}{str(index)}".encode('utf-8')).hexdigest()[:len(string)] == string:
            return index
        index += 1

print(f"part 1: {md5_starting_with_string('00000')}")
# 282749

print(f"part 2: {md5_starting_with_string('000000')}")
# 9962624
