##(HERO'S FORMULA IS GIVEN AS : AREA = SQRT(S*(S-a)*(S-b)*(S-c)))
a = int(input("Enter the first side of the trianggle: "))
b = int(input("Enter the second side of the trianggle: "))
c = int(input("Enter the third side of the trianggle: "))
print(a,b,c)
S = (a+b+c)/2
area =(S*(S-a)*(S-b)*(S-c))
print("Area =" +str(area))
