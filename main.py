import subfunctions

dataframe = {}

class GroupExpenseTracker:
    # create groups in dataframe
    def create_group(group_name, members=[]):
        if group_name in dataframe.keys():
            return {"Error": "Group already created before"}

        else:
            dataframe[group_name] = {}
            dataframe[group_name]["name"]=group_name
            dataframe[group_name]["items"] = []
            dataframe[group_name]["members"] = members
            return dataframe

    # add expenses to group name present in dataframe
    def add_expense(group_name,name,value,paidby={},owedby={}):

        if group_name not in dataframe.keys() or (subfunctions.check(value,paidby) or subfunctions.check(value,owedby)):
            return {"Error": "Create the Group First"}

        else:
            expenserecord = {"name": name, "value": value, "paidby": paidby, "owedby": owedby}
            dataframe[group_name]["items"].append(expenserecord)
            membersarr = dataframe[group_name]["members"]
            dataframe[group_name]["members"] = subfunctions.addmembers(membersarr, paidby.keys())
            dataframe[group_name]["members"] = subfunctions.addmembers(membersarr, owedby.keys())
            return dataframe

    # update the already added expense in the dataframe
    def update_expense(group_name,name,value=None,paidby=None,owedby=None):
        if group_name not in dataframe.keys():
            return {
                "Error": "Create the Group First and add an Expense to Update it"
            }
        else:
            tempitems_var=dataframe[group_name]["items"]
            N = len(tempitems_var)

            for i in range(N):
                if tempitems_var[i]["name"] == name:
                    if value != None and tempitems_var[i]["value"] != value:
                        tempitems_var[i]["value"] = value

                    if (paidby != None and tempitems_var[i]["paidby"] != paidby) and subfunctions.check(value,paidby) :
                        tempitems_var[i]["paidby"] = paidby
                        membersarr = dataframe[group_name]["members"]
                        dataframe[group_name]["members"] = subfunctions.addmembers(membersarr, paidby.keys())

                    if (owedby != None and tempitems_var[i]["owedby"] != owedby) and subfunctions.check(value,owedby):
                        tempitems_var[i]["owedby"] = owedby
                        membersarr = dataframe[group_name]["members"]
                        dataframe[group_name]["members"] = subfunctions.addmembers(membersarr, owedby.keys())

                    return dataframe
            return {"Error": "Expense is not in Group. Please add it first"}

    # delete the already added expense in the dataframe
    def delete_expense(group_name,name):
        if group_name not in dataframe.keys():
            return {
                "Error": "Create the Group First and initialize it by adding expenses"
            }
        else:
            N = len(dataframe[group_name]["items"])
            for i in range(N):
                if dataframe[group_name]["items"][i]["name"] == name:
                    del dataframe[group_name]["items"][i]
                    return dataframe
            return dataframe

    # give total balance, owes_to, owed_by for each member if the group
    def balance(group_name):
        balancerecord = {}
        if group_name not in dataframe.keys():
            return {
                "Error": "Create the Group First, initialize it by adding expenses and then get the summary of expenses"
            }
        else:

            balancerecord["name"]=group_name
            balancerecord["balance"]={}
            k=balancerecord["balance"]
            membersarr = dataframe[group_name]["members"]
            for i in membersarr:
                k[i]={"total_balance":0,"owes_to":[],"owed_by":[]}
            itemsarr=dataframe[group_name]["items"]
            for i in itemsarr:
                for j in k.keys():
                    t1=0
                    if j in i["paidby"].keys():
                        t1=i["paidby"][j]
                    t2=0
                    if j in i["owedby"].keys():
                        t2=i["owedby"][j]

                    k[j]['total_balance']+=t1-t2
            lista = []
            for j in k.keys():
                lista.append([k[j]['total_balance'],j])
            lista.sort(reverse=True,key= lambda x:x[0])
            leftp=0
            rightp=len(lista)-1
            while leftp < rightp:
                if lista[leftp][0] + lista[rightp][0] < 0:
                    k[lista[rightp][1]]["owes_to"].append({lista[leftp][1]: abs(lista[leftp][0])})
                    k[lista[leftp][1]]["owed_by"].append({lista[rightp][1]: abs(lista[leftp][0])})
                    lista[rightp][0] = lista[leftp][0] + lista[rightp][0]
                    leftp += 1
                elif lista[leftp][0] + lista[rightp][0] > 0:
                    k[lista[leftp][1]]["owed_by"].append({lista[rightp][1]: abs(lista[rightp][0])})
                    k[lista[rightp][1]]["owes_to"].append({lista[leftp][1]: abs(lista[rightp][0])})
                    lista[leftp][0] = lista[rightp][0] + lista[leftp][0]
                    rightp -= 1
                else:
                    k[lista[leftp][1]]["owed_by"].append({lista[rightp][1]: abs(lista[rightp][0])})
                    k[lista[rightp][1]]["owes_to"].append({lista[leftp][1]: abs(lista[rightp][0])})
                    leftp+=1
                    rightp-=1
        print(balancerecord)

if __name__ == "__main__":
    GroupExpenseTracker.create_group("pokemon",["A"])
    GroupExpenseTracker.create_group("pikachu")
    GroupExpenseTracker.add_expense("pokemon","milk",50,{"A": 40, "B": 10}, {"A": 20,"B": 20, "C": 10})
    GroupExpenseTracker.add_expense("pokemon","bread",90,{"A": 70, "B": 20}, {"A": 20,"B":10, "C": 60})
    GroupExpenseTracker.add_expense("pikachu","milk",50,{"A": 40, "B": 10}, {"A": 20,"B": 20, "C": 10})
    GroupExpenseTracker.add_expense("pikachu","butter",120,{"A": 90, "B": 30}, {"A": 120,"B":0, "C": 0})
    GroupExpenseTracker.add_expense("pokemon","jam",260,{ "B": 100,"C":160}, {"A": 100,"B":160, "C": 0})
    GroupExpenseTracker.add_expense("pikachu","bread",90,{"A": 70, "B": 20}, {"A": 20,"B":10, "C": 60})
    GroupExpenseTracker.add_expense("pokemon","butter",120,{"A": 90, "B": 30}, {"A": 120,"B":0, "C": 0})
    GroupExpenseTracker.add_expense("pikachu","jam",260,{ "B": 100,"C":160}, {"A": 100,"B":160, "C": 0})
    GroupExpenseTracker.update_expense("pokemon","milk",60,{"A": 40, "B":50},{"A": 40, "B":60,"C":96})
    GroupExpenseTracker.delete_expense("pokemon","milk")
    GroupExpenseTracker.balance("pokemon")
    GroupExpenseTracker.balance("pikachu")
