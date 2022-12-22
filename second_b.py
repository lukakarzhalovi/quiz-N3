dict = {"hi":[1,3,4,6,5,2,7], "no": [2,4,3,6,7,8,6], "yes": [10,34,21,34,16],"done":[10,7,3,4]}
def key(data):
    name = ""
    count = 0
    for key,value in data.items():
        if len(value) > count:
            name = key
            count = len(value)
        elif len(value) == count:
            name += (" " + str(key))
    return name
print(key(dict))