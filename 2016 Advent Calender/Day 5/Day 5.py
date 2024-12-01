from utils.decorators import time_it
import hashlib


Day_5 = "How About a Nice Game of Chess?"


data = "abbhdwsy"
fun = "funpassword"
password = ""


def MD5_Hash(inputString):
    hash = hashlib.md5()
    hash.update(inputString.encode('utf-8'))
    hashHex = hash.hexdigest()
    return hashHex

@time_it
def Find_Password(data):
    digit = 0
    returnString = ""

    while len(returnString) < 8:
        inputString = data + str(digit)

        hash = MD5_Hash(inputString)

        if hash.startswith("00000"):
            returnString += hash[5]
            print(returnString)

        digit += 1

    return returnString

password = Find_Password(fun)

print(f"The password is: {password}")


#   Part 2

@time_it
def Find_Password_2(data):
    digit = 0
    passwordBuilder = [
        '-',
        '-',
        '-',
        '-',
        '-',
        '-',
        '-',
        '-'
        ]
    
    returnString = ""

    while "-" in passwordBuilder:
        inputString = data + str(digit)

        hash = MD5_Hash(inputString)


        if hash.startswith("00000"):
            if hash[5].isnumeric():
                hashPos = int(hash[5])
                if hashPos < 8:
                    if passwordBuilder[hashPos] == '-':
                        passwordBuilder[hashPos] = hash[6]

                        test = ''.join(map(str,passwordBuilder))
                        print(digit, test)

        digit += 1

        returnString = ''.join(map(str,passwordBuilder))


    return returnString

secondPassword = Find_Password_2(fun)

print(f"The second password is: {secondPassword}")

print(f"The combined password is: {password}{secondPassword}")