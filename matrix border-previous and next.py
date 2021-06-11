Matrix border- previous and next:
Input:
5 5
74 21 77 95 58
97 21 35 56 73
94 23 39 57 14
64 87 34 56 54
38 61 22 72 25
54

Output:
54 14 25 73 72 58 22 95 61 77 38 21 64 74 94 97

Code:

#include<stdio.h>
#include<stdlib.h>
int main()
{
int r,c,k;
scanf("%d %d",&r,&c):
int a[r][c],i,j:
for(i=0;i<r;i++)
{
for(j=0;j<c;j++)
{
scanf("%d",&a[i][j]);
}
}
scanf("%d",&k);
int row=-1,col=-1;
for(i=0;i<r;i++)
{
for(j=0;j<c;j++)
{
if(i==0||i==r-1||j==0||j==c-1)
{
if(a[i][j]==k && row==-1 && col==-1)
{
row=i;
col=j;
}
}
}
}
if(row==-1 && col==-1)
{
printf("-1");
exit(0);
}
int len=(r*2)+((c-2)*2);
int b[len],ind,l=0;
for(i=0;i<c;i++)
{
if(row==0 && col==i)
ind=l;
b[l++]=a[0][i];
}
for(i=1;i<r;i++)
{
if(row==i && col==c-1)
ind=l;
b[l++]=a[i][c-1];
}
for(i=c-2;i>=0;i--)
{
if(row==r-1 && col==i)
ind=l;
b[l++]=a[r-1][i];
}
for(i=r-2;i>0;i--)
{
if(row==i && col==0)
ind=l;
b[l++]=a[i][0];
}
int left=ind,right=ind,s=len;
while(len>0)
{
int i1=left%s;
int i2=right%s;
if(i1==i2)
{
printf("%d ",b[i1]);
len-=1;
}
else
{
printf("%d %d ",b[i1],b[i2]);
len-=2;
}
if(left==0)
left=s;
left--;
right++;
}
return 0;
}