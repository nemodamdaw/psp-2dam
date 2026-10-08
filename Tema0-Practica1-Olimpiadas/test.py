lis=[]
lis.append(('B',23,12.9))
lis.append(('C',13,2.9))
lis.append(('A',25,9.9))
lis.append(('D',22,5.9))
print(lis)
print(max(lis))
print(max(lis, key=lambda t:t[0]))
print(max(lis, key=lambda t:t[1]))
print(max(lis, key=lambda t:t[2]))
d={'a':3,'b':1,'c':2}
print(d)
print(max(d))
print(max(d.items()))
print((d.items()))
print(max(d.items(),key = lambda t:t[0]))
print(max(d.items(),key = lambda t:t[1]))
print(max(d.items(),key = lambda t:t[1])[0])
lis=[2,3,4,5,6,7]
print(lis)
print(lis[0:])
print(lis[3:])
print(lis[3:5])
lis1=[2,3,4,5,6,7]
lis2=[12,3,0,1,1,-3]
print()
print(lis1)
print(lis2)
#print(list(zip(lis1,lis2)))
lis3=[]
for e1,e2 in zip(lis1,lis2):
    lis3.append(e1+e2)
print(lis3)
print()
lis2=[12,3,0,1,1,-3]
print(lis2)
lis4=[]
for e1,e2 in zip(lis2,lis2[1:]):
    lis4.append(e2-e1)
print(lis4)
