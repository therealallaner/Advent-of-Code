

input = "1113222113"
test = "211"

def look_say(string):
    temp = string[0]
    return_string = ""
    copies = 1

    for char in string:
        if char == temp:
            copies += 1
    
    return return_string

print(look_say(input))