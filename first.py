def marketcap_sort():
    f =  open("stocks (1).txt","r")
    lines = f.readlines()
    add = [lines[0]]
    for line in lines[1:len(lines)]:
        line_split = line.split(" ")
        if float(line_split[1]) <= 600:
            add.append(line)
    f.close()
    k = open("stocks_new","a")
    k.writelines(add)
    k.close()
    return 
marketcap_sort()