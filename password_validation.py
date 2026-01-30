n=input()
s=len(n)
a=0
b=0
c=0
d=0
for i in n:
    if i.islower():
        a+=1
    elif i.isupper():
        b+=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
if a>0 and b>0 and c>0 and d>0 and s>=8:
    print("Password is valid and Strong")
elif (a>0 or b>0 and d>0) and s>=8:
    print("Password is valid and Medium")
elif s>=8:
    print("Password is valid and weak")
else:
    print("Password is invalid")
