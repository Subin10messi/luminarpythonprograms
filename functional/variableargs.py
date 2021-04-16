#def add(*args):
#    sum=0
#    for i in args:       #converts to tuple format
#        sum+=i
#    return sum
#res=add(10,20,30)
#print(res)

#lst=[10,8,23,46,34,90]
#lst.sort(reverse=True)
#print(lst)

def print_person_details(**kwargs):#kwargs converts it into dic format i.e,keyvalue pairs
    print(kwargs)
print_person_details(name="subin",bthplace="kollam",wrkplace="uk")
