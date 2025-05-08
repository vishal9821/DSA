#time conversion

def timeConversion(s:str):
    if 'P' in s:
        ns = s.replace('PM','')
        temp = ns.split(':')
        if temp[0] == '12':
            return(':'.join(temp))
        else:
            temp[0]=str(int(temp[0])+12)
            return(':'.join(temp))
    else:
        ns = s.replace('AM','')
        temp = ns.split(':')
        if temp[0] == '12':
            temp[0]='00'
        return(':'.join(temp))

# sparse array 

def matchingStrings(strings, queries):
    count = []
    for i in queries:
        oc = 0
        for j in strings:
            if j == i:
                oc+=1
        count.append(oc)
    return count

#lonely integer

def lonelyinteger(a:list):
    for i in range(len(a)):
        count = 0
        un = a[i]
        for j in range(len(a)):
            if un == a[j]:
                count+=1
        if count == 1:
            return un
    return None

                
        


        

a = [1,2,3,4,1,2,3,]
print(lonelyinteger(a))



                
