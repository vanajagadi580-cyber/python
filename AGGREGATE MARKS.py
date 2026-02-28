marks1 = int(input("Enter the marks in mathemetics:"))
marks2 = int(input("Enter the marks in science:"))
marks3 = int(input("Enter the marks in social studies:"))
marks4 = int(input("Enter the marks in computer:"))
total = marks1+marks2+marks3+marks4
avg = float(total)/4
print("Total",total, "\t Aggregate = ",avg)
if(avg>=75):
    print("Distinction")
elif(avg>=60 and avg<75):
    print("First distinction")
elif(avg>=50 and avg<60):
    print("Second distinction")
elif(avg>=40 and avg<50):
    print("Thrid ditinction")
else:
    print("Fail")
