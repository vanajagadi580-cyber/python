m=[]
n=int(input())
for i in range(0,n):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(0,n):
    csum=0               
    for j in range(0,n):
        csum=csum+m[j][i]
    print(csum,end=' ')
