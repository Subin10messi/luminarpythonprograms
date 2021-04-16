a=[10,13,20,30,19]
b=[12,20,30,55,60]
def common(a,b):
    c = [num for num in a if num in b]
    return c
d=common(a,b)
print(d)