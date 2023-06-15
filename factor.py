def factor(x):
    if x <= 1:
        return x
    else:
        return x*factor(x-1)

#print(factor(4))

def fib(x):
    if x == 1 or x==0:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(18))