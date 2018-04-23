numbers = ['1','2','3','4','5','6','7','8','9']

pan_dig = 'N'
calc1 = 'Y'
calc2 = 'Y'
num1 = 2
pd_nums = []
pd_calc = []
pd_num1 = []
pd_num2=[]
while calc1 == 'Y':
    num2 = num1+1
    if len(str(num1)+str(num2)+ str(num1*num2))>9:
        calc1 = 'N'
        break
    calc2 = 'Y'
    while calc2 == 'Y':
        clean = 'Y'
        pandigits = str(num1)+str(num2)+ str(num1*num2)
        if len(pandigits)<9:
            num2+=1
            continue
        elif len(pandigits)>9:
            calc2 = 'N'
            break
        else:
            for char in numbers:
                if char not in pandigits:
                    clean = 'N'
                    break
            if clean == 'Y':
                if num1*num2 not in pd_calc:
                    pd_num1.append(num1)
                    pd_num2.append(num2)
                    pd_calc.append(num1*num2)
                    pd_nums.append(int(pandigits))
            num2+=1
    num1+=1
print pd_num1
print pd_num2
print pd_calc
print pd_nums
print sum(pd_calc)
