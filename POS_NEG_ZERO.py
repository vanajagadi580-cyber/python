negative = positive = zeroes = 0
print("Enter -1 to exits-----")
while(1):
    num = int(input("Enter the number: "))
    if (num == -1):
        break
    elif(num == 0):
        zeroes += 1 
    elif(num>0):
        positive+= 1
    else:
        negative +=1
print("Count of positive numbers entered : ",positive)
print("Count of negative  numbers entered: ",negative)
print("Count of zeroes of numbers entered: ",zeroes)
