Sub-Palindrome count:

Input:

everest

Output:

2
(eve,ere)

Code:

x=input().strip()
count=0
for i in range(len(x)):
  for j in range(i+2,len(x)+1):
     temp=x[i:j]
     if temp==temp[::-1]
        count+=1
print(count)