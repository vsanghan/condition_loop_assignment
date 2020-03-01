#assignment 1 : aaaabbbbabaaabccc --> {'a':8, 'b':6, 'c':3}


st = 'aaaabbbbabaaabccc'

stI = st[0]
di = {}
c = 0

for i in st :
    if i == stI:
        if i in di.keys():
            di[i] += 1
            c = di[i]
            #print("counter set to di[index]")
        else :
            c = c + 1
            di[i] = c

    elif i != stI:
        if i not in di.keys():
            stI = i
            c = 1
            di[i] = c
            #print('di not in key')
        elif i in di.keys():
            di[i] += 1
            c = di[i]
            #print("counter set to di[index] again")


    #print (i,c,di)
print (di)