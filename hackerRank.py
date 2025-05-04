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



s = input('Enter time in 12 hour Clock: ')
timeConversion(s)