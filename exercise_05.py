#assignment 5 : 78512567 --> Rs.7,85,12,567

x = input("Indian number format : ")
y = ''
#x = str(x)

if len(x) > 3:
    a = ','+(x[-3:])
else :
    a = x
    
b= (x[:-3])
c = 0
for i in b[::-1]:
    c+=1
    y = y+str(i)
    #print (i, c, y)
    if c == 2:
        c=0
        y = y+','
y = y[::-1]
y = y + a
print ("Final value for y in Rs." + y)