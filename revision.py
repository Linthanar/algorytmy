from unittest import result


a, b = 1, 2
print("{0}{1}".format(b,a))
print("string" + str(a), b)
t = 'txt'
# print(t * (2**20) )


myList = [1,2,'2','223',{'age' : 50, 'name' : 'Simon'}]
print(myList)

myTouple = (1,3,4)

myTouple = (4,5,6)


print(myTouple[0])

myDict = { '1' : 'HArry Potter', '2' : 'Pan Samochodzik' }
print(myDict['2'])

for x in 'abc':
    print(x)

for x in range(2):
    print(x)

if 1 == 1:
    print('1==1',True)

if '2' in myList:
    print('1 in mylist',True)

twoDimm = []
Dimm = []
for x in range(0,5):
        Dimm.append(x)
for y in range(0,5):
    twoDimm.append(Dimm)

print(twoDimm)

#print(twoDimm)

simonsList = [1,2,3,4,5,6]

def square(x):
    return x*2

def filTer(x):
    if x % 2 ==0:
        return True
    return False
result = []
# for x in twoDimm:
#     # newList = map(square, x)
#     # print(list(map(square, x)))
#     result.append(list(map(square, x)))

# print(result)
# # print(list(newList))
result1 =[]
for column in twoDimm:
    # print(column)
    result1.append(list(filter(filTer, column)))

print(result1)

    # for row in column:
    #     # print(list(filter(filTer,twoDimm[x][y])))
    #     print(row)

