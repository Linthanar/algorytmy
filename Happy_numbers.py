Happy_num = 2
aux = str(Happy_num)
l_num = []
l_happy = []

i = 0
add = 0
num_search = True

for z in range(30):
    num_search = True
    Happy_num = z
    bank = z
    l_num = []
    i = 0
    print("Happy number", z)

    while num_search == True:
        aux = str(Happy_num)
        add = 0

        for num in aux:
            add = add + int(num)**2

        Happy_num = add
        aux = str(Happy_num)

        if Happy_num == 1:
            l_happy.append(bank)
            num_search = False

        if Happy_num in l_num:
            num_search = False
        l_num.append(Happy_num)

        i += 1
        aux2 = str(i)
        count = 0
        for x in aux2:
            count += 1
        print(i, " "*(4-count), ": ", add)

    print("_________________________________")

print(l_happy)
