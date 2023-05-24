def sum(*, list):
    result = 0
    for i in list:
        result = result+i
    return result

def average(*, list):
    result = 0
    for i in list:
        result = result + i
    result = result/len(list)
    return result

