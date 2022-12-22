dict = {"hi":[1,3,4,6,5,2,7], "no": [2,4,3,6,7,8], "yes": [10,34,21,34,16],"done":[10,7,3,4]}
def value_tuple(data):
    values = data.values()
    my_tuple = ()
    for i in values:
        for j in i:
            if j % 3 == 0:
                my_tuple += (j,)
    return my_tuple
print(value_tuple(dict))