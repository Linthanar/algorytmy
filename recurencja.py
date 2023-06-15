def recur(x):
    if x > 1:
        return print('hello recursive world')
    else: 
        print('test')
        recur(x-1)

recur(5)