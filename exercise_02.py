#assignment 2 : aaaabbbbabaaabccc --> abababc

def uniqe_once(st):
    stI = st[0]
    newSt= st[0]
    for i in st[1:]:
        if i != stI:
            newSt =  newSt + i
            stI=i
    return (newSt)

string = 'aaaabbbbabaaabccc'
print (uniqe_once(string))