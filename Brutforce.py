import string
secret = 'password'
print(string.ascii_lowercase)
'abcdefghijklmnopqrstuvwxyz'
crackTheCode = False
while crackTheCode == False:
    for q in string.ascii_lowercase:
        if q == secret:
            print(q+w)
            crackTheCode = True
            break
        print(q)
        for w in string.ascii_lowercase:
            if q+w == secret:
                print(q+w)
                crackTheCode = True
                break
            print("-")
            for e in string.ascii_lowercase:
                if q+w+e == secret:
                    print(q+w+e)
                    crackTheCode = True
                    break
                for r in string.ascii_lowercase:
                    if q+w+e+r == secret:
                        print(q+w+e+r)
                        crackTheCode = True
                        break
                    for t in string.ascii_lowercase:
                        if q+w+e+r+t == secret:
                            print(q+w+e+r+t)
                            crackTheCode = True
                            break
                        for y in string.ascii_lowercase:
                            if q+w+e+r+t+y == secret:
                                print(q+w+e+r+t+y)
                                crackTheCode = True
                                break
                            for u in string.ascii_lowercase:
                                if q+w+e+r+t+y+u == secret:
                                    print(q+w+e+r+t+y+u)
                                    crackTheCode = True
                                    break
                                for i in string.ascii_lowercase:
                                    if q+w+e+r+t+y+u+i == secret:
                                        print(q+w+e+r+t+y+u+i)
                                        crackTheCode = True
                                        break