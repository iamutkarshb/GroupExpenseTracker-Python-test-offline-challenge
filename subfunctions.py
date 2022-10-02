def addmembers(membersarr,arr):
    for i in arr:
        if i not in membersarr:
            membersarr.append(i)
    return membersarr

def check(value,paidby={}):
    j=0
    for i in paidby.keys():
        j+=paidby[i]
    if j!= value:
        return True
