def sum(*zahlen):
    sum = 0
    for i in zahlen:
        sum = sum + i
    return sum


s = sum(1,2,3,4,5,6,7,8,9, 10)
print(s)