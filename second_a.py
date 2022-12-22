dict = {"hi":[1,3,4,6,5,2,7], "no": [2,4,3,6,7,8], "yes": [10,34,21,34,16],"done":[10,7,3,4]}
def value_Sum(data):
    value = data.values()    
    Max = 0
    for i in value:
        sum = 0
        for j in i:
            sum+=j
        if sum > Max:
            Max = sum
    return Max
print(value_Sum(dict))