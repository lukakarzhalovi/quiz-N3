dict = {"hi":[1,3,4,6,5,2,7], "no": [2,4,3,6,7,8], "yes": [10,34,21,34,16],"done":[10,7,3,4]}
def New_Dict(data):
    new_dict = {}
    for key,value in data.items():
        averrage = float(sum(value) / len(value))
        new_dict[key] = averrage
    return new_dict
print(New_Dict(dict))
