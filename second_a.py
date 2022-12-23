dict = {"hi":[1,3,4,6,5,2,7], "no": [2,4,3,6,7,8], "yes": [10,34,21,34,16],"done":[10,7,3,4]}
def value_Sum(data):
    value = data.values()  
    sum = 0
    for i in value:
        for j in i:
            sum+=j
    return sum
print(value_Sum(dict))
