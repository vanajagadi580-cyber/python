def arms(num):
    sum=0
    n=num
    while num!=0:
        r=num%10
        num=num//10
        sum=sum+(r*r*r)
    if n==sum:
        return True
    else:
        return False
n=int(input())
a=[i for i in range(1,n+1) if arms(i)]
for i in a:
    print(i,end=' ')
