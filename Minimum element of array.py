a=[]
n=int(input())
for i in range(n):
    x=int(input())
    a.append(x)
minn=a[0]
for i in range(n):
    if a[i]<minn:
        minn=a[i]
print(minn)
