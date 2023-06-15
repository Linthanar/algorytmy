from cgitb import small


a = [1, 3, 4, 4, 3 ,7, 1 ]
b = [ 1, 2, 3]
simList = []
for x in b:
    print(x)
    for y in a:
        print(x)
        print(y)
        if x == y:
            simList.append(x)

print(simList)


def check(x):
    for i in b:
        if i == x:
            return True
fil = filter(check, a)

# if x in simList

print(list(fil))