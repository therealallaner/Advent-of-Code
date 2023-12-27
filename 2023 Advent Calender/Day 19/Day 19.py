
Day_19 = "Aplenty"

workflow = {}
xmas = ["x", "m", "a", "s"]
parts = []
part1 = 0

def file_to_list():
    return_list = []
    data = open("./2023 Advent Calender/Day 19/data.txt")
    #data = open("./2023 Advent Calender/Day 19/test.txt")
    for line in data:
        clean_data = filter(None,line.split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()

def read_rules(l):
    rules = []
    for r in l:
        r = r.replace("<", " < ").replace(">"," > ").replace(":"," ").split()
        rules.append(r)

    return rules


def read_workflow(p,l,s):
    status = s
    return_value = 0

    part = {}
    part["x"] = p[0]
    part["m"] = p[1]
    part["a"] = p[2]
    part["s"] = p[3]

    rules = read_rules(l)
    



    for r in rules:
        if "<" in r:
            x = int(part[r[0]])
            comp = int(r[2])
            if x < comp:
                status = r[3]
                if status == "A":
                    for a in p:
                        return_value += int(a)
                    return return_value
                elif status == "R":
                    return
                
                return read_workflow(p,workflow[status],status)

        elif ">" in r:
            x = int(part[r[0]])
            comp = int(r[2])
            if x > comp:
                status = r[3]
                if status == "A":
                    for a in p:
                        return_value += int(a)
                    return return_value
                elif status == "R":
                    return
                return read_workflow(p,workflow[status],status)
                

        else:
            status = r[0]
            if status == "A":
                for a in p:
                    return_value += int(a)
                return return_value
            elif status == "R":
                return
            return read_workflow(p,workflow[status],status)


for l in data:
    part = []
    wflow = []

    if l[0] == "{":
        l = l.replace("="," ").replace(","," ").replace("{","").replace("}","").split()
        for i, c in enumerate(l):
            if c in xmas:
                part.append(l[i+1])

        parts.append(part)

    else:
        l = l.replace(","," ").replace("{"," ").replace("}","").split()
        workflow[l[0]] = l[1:]


for p in parts:
    x = read_workflow(p,workflow["in"],"in")
    if x:
        part1 += x

    

print(part1)

# Part 2
    # I do not understand what it is asking for part 2 at all.