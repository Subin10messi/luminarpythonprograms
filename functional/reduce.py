from functools import reduce      # to reduce to a single value like sum max min etc...
                                  # we import reduce function from functools which means its not builtin

lst=[10,20,30,50,80]

total=reduce(lambda no1,no2:no1+no2,lst)   # here we pass two arguments unlike map and filter
print(total)
mx=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(mx)
mini=reduce(lambda no1,no2:no2 if no1>no2 else no1,lst)
print(mini)


