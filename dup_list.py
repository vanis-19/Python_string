l=[1,2,3,4,5,4,3,6,5,8]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)        
s=set(l)
print(s)