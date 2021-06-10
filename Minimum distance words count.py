Minimum Distance Between Words:

Input:

the count of the birds in the world 
the 
count

Output:
1

Code:

x=list(input().strip().split(" "))
y=input().strip()
z=input().strip()
r=0
minc=200
for i in range(len(x)):
  if x[i]==y or x[i]==z:
    c=1
    for j in range(i+1,len(x)):
       if j==len(x)-1:
         r=1
       if x[j]==y or x[j]==z:
         break
       else:
         c+=1
    if minc>c:
       minc=c
  if r==1:
    break

print(minc)
    