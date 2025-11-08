def fatoral (num=1):
    f =1
    for c in range(num, 0, -1):
        f= f * c
    return f


n = int(input('digite'))
print(fatoral(n))