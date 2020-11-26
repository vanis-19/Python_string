s='vanisaddala'
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d) 

l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in sorted(l):
    print('{} occurs {} times.format(i, s.count(i))
   
