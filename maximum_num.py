m=[]
n=int(input())
for i in range(0,n):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(0,n):
    a=m[0][i]
    for j in range(0,n):
        if m[j][i]>a:
            a=m[j][i]
    print(a,end=' ') 
    
