Filling Can:

Input:
5
2
3

Output:
2

Code:

x=int(input())
y=int(input())
z=int(input())
s=0
c=0
m=max(x,y)
n=min(x,y)
while True:
  s+=1
  m=m-n
  if m==z:
    c=1
    break
  if m<=0:
    break
if s==0 or c==0 or(z>x and z>y):
   print(-1)
   exit()
print(s*2)