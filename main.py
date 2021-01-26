from random import randrange

n = 10

mydict = {}
for i in range(1, n):
    values = []
    for j in range(1, randrange(1, n)):
        if(i != j):
            values.append(str(j))
    mydict[str(i)] = values
    

print(mydict)
