#assignment 4 : given list of words and integer 'n' --> word which has length longer than 'n' 


li = ['aaa', 'python', 'abc', 'programming']
n = 6
li_op = []

for i in li:
    if len(i) > n:
        li_op.append(i)
print (li_op)