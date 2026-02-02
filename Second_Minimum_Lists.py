l=[]
n=int(input())
for i in range(n):
    x=int(input())
    l.append(x)
first=min(l)
l.remove(first)
second=min(l)
print(second)
