


footballer={
    1000:{"name":"subin","desig":"footballer","club":"fc barcelona"},
    1001:{"name":"mathews","desig":"cricketer","club":"Mumbai indians"},
    1002:{"name":"rohan","desig":"basketballer","club":"Northeast WL"}

}
pid=int(input("enter player id"))
#if pid in footballer:
#    print(footballer[pid]["name"])
#else:
#    print("footballer doesnt exist")

#create a function
#emp_details(eid=1000)
def emp_details(**kwargs):
    id =kwargs["pid"]
    prop=kwargs["prop"]
    if id in footballer:
        print(footballer[pid]["name"])
        print(footballer[pid][prop])
    else:
        print("footballer doesnt exist")



emp_details(pid=1001,prop="club") #subin
#emp_details(eid=1000,prop="desig")  #subin,footballer



