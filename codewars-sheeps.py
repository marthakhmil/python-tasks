def count_sheeps(arrayOfSheeps):
    sum=0
    for i in arrayOfSheeps:
        if i == True:
            sum += 1
    return sum

def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
