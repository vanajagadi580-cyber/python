for i in range(1,6):
    for j in range(0,6):
        print(i*j,end="  ")
    print()
    
    
for i in range(0,6):
    for j in range(0,6):
        if i==0:
            if j==0:
                print("*",end=" ")
            else:
                print(j, end=" ")
        else:
            if j==0:
                print(i,end=" ")
            else:
                print(i*j,end=" ")
    print()
    
    a=int(input())
for i in range(1,11):                                 #printing a table
    print(a ,"*", i," = ", a*i)
    
    for i in range(1,101):
        if(i%10==0):  
           print(i)                 #printing 1 to 100 numbers each row 10                    
    else:
        print(i,end="     ")

for i in range(1,11):
    if(i==5):
        continue                                  # printing numbers 1 to 10 except 5
    else:
        print(i)     
        
        a=1
while(a<=10):
    if(a==5):
        a+=1                                       # printing numbers 1 to 10 upto 5
        break                                     
    print(a)
    a+=1
    
    for j in range(1,11):
        
     for i in range(1,11):                          # printing 1 to 10 tables
        print(i,"*",j,"=",i*j,end=" ")           
    print()
