input
AnuTdS

output
AdSnTu



s=input().strip()
u,lo,l=[],[],[]
l[:-1]=s
for i in range(len(l)):
   if l[i].isupper():
      u.append(l[i])
   else:
      lo.append(l[i])
u.sort()
lo.sort()
l1,l2=len(u),len(lo)
m=l1 if(l1>l2) else l2
i=0
while(i<m):
  if m<l1:
    print(u[i],end="")
  if m<l2:
    print(lo[i],end="")
      
