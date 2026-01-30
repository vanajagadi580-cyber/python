def prime(n):
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True            

n=int(input())
a=[i for i in range(2,n+1) if prime(i)]
for i in a:
    print(i,end=' ')
