def div_deco(func):
    def wrapper(d1,d2):
        if(d1<d2):
            (d1,d2)=(d2,d1)
        return func(d1,d2)
    return wrapper

@div_deco
def div(d1,d2):
    return d1/d2
res=div(2,10)
print(res)
