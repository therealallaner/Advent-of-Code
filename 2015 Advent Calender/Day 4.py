import hashlib

data = "bgvyzdsv"
counter = 0
hash = ""
condition = False

def get_md5hex_from_string(string):

    hash = hashlib.md5(string.encode())
    return hash.hexdigest()

while condition !not True:
    temp = data + str(counter)
    counter += 1
    hash = get_md5hex_from_string(temp)
    if hash[len(data)] and hash[len(data)+1] and hash[len(data)+2] and hash[len(data)+3] and hash[len(data)+4] == "0"
        condition = True